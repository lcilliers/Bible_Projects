"""aiclient -- the one route to the AI models on zeta-assist (escalation #2361, stage 4).

Every call to the Ollama server goes through AiClient.call(); no module calls the server any other way. The client
  - takes the model of a ROLE (judge, embed, embed_fast, quick, reviewer) from cfg_ai_model: exactly one row of that role must be active;
  - takes the prompt of a KEY from cfg_ai_prompt: exactly one version must be active, and its stored hash must equal the hash of its text;
  - refuses a variable the prompt does not name, a placeholder no variable fills, and an option outside setting ai.allowed_options;
  - checks the server before the first call (it answers within ollama.connect_timeout_seconds and has the model) and opens the ssh tunnel
    (lib/surfacejudge.server_route, settings ollama.*);
  - halts after ai.max_consecutive_failures calls in a row with no usable answer (B:124);
  - writes ONE ai_call row for every attempt: module, step, role, model and digest, prompt version, options, request hash, the request, the raw
    answer, the result, the outcome, the error, tokens and seconds. outcome answered = a usable answer; refused = the server answered and
    the caller's check found the answer not usable; failed = the call itself failed (network, timeout, unparsable); halted = the halt rule.
A refused model, prompt or option writes nothing and raises AiError: the call was never made. Every answer is inferential (B:4).
The transport is injectable, for tests and for replay; the default is the Ollama chat route of lib/surfacejudge.ask.
"""
from __future__ import annotations

import contextlib
import hashlib
import json
import re
import time

from . import surfacejudge as sj

SETTING_KEYS = ["ai.allowed_options", "ai.retries", "ai.max_consecutive_failures", "ai.embed_batch"]
OLLAMA_KEYS = ["ollama.host", "ollama.timeout_seconds", "ollama.keep_alive", "ollama.num_ctx", "ollama.temperature", "ollama.connect_timeout_seconds"]


class AiError(Exception):
    """A model, prompt, option or setting is refused: the call was not made and nothing is written."""


class AiHalted(Exception):
    """ai.max_consecutive_failures calls in a row had no usable answer: the run stops, what was answered is kept."""


def text_hash(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()[:16]


def read_settings(cfg) -> dict:
    vals = {k: cfg.setting(k) for k in SETTING_KEYS + OLLAMA_KEYS}
    missing = [k for k, v in vals.items() if v is None]
    if missing:
        raise AiError(f"cfg_setting missing: {missing}")
    if not isinstance(vals["ai.allowed_options"], list):
        raise AiError("cfg_setting ai.allowed_options is a JSON list of option names")
    vals["ssh_target"], vals["ssh_key"] = cfg.setting("ollama.ssh_target"), cfg.setting("ollama.ssh_key")
    vals["tunnel_local_port"] = cfg.setting("ollama.tunnel_local_port")
    return vals


def default_transport(route: dict, model: str, text: str, options: dict):
    """One chat call to the Ollama server. Returns (parsed JSON answer, raw answer text, server counts)."""
    vals = {"model": model, "host": route["host"], "keep_alive": options["keep_alive"], "temperature": options["temperature"],
            "num_ctx": options["num_ctx"], "timeout_seconds": route["timeout_seconds"]}
    obj, meta = sj.ask(vals, text)
    return obj, json.dumps(obj, ensure_ascii=False), {"tokens_out": meta.get("out_tokens"), "tokens_in": meta.get("prompt_tokens")}


def default_embedder(route: dict, model: str, texts: list):
    """One embedding call (the Ollama /api/embed route). Returns the list of vectors, one per text."""
    import urllib.request
    body = {"model": model, "input": texts, "keep_alive": route.get("keep_alive", "30m")}
    req = urllib.request.Request(route["host"] + "/api/embed", json.dumps(body).encode(), {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=route["timeout_seconds"]) as r:
        return json.loads(r.read())["embeddings"]


class AiClient:
    def __init__(self, cfg, module: str, step: str, run_id: str | None = None, batch_id: int | None = None, transport=None, embedder=None):
        self.cfg, self.conn = cfg, cfg.conn
        self.module, self.step, self.run_id, self.batch_id = module, step, run_id, batch_id
        self.vals = read_settings(cfg)
        self.transport = transport or default_transport
        self.embedder = embedder or default_embedder
        self.live = transport is None and embedder is None
        self.route = {"host": self.vals["ollama.host"], "timeout_seconds": self.vals["ollama.timeout_seconds"]}
        self.streak = 0

    # ---- the registers -------------------------------------------------------------------------------------------------------
    def model(self, role: str):
        rows = self.conn.execute("SELECT id, name, digest FROM cfg_ai_model WHERE role=? AND status='active' AND inactive=0", (role,)).fetchall()
        if len(rows) != 1:
            raise AiError(f"role {role!r} needs exactly one active model in cfg_ai_model, found {len(rows)}")
        return rows[0]

    def prompt(self, key: str):
        rows = self.conn.execute("SELECT id, version, text, hash, role FROM cfg_ai_prompt WHERE prompt_key=? AND status='active'", (key,)).fetchall()
        if len(rows) != 1:
            raise AiError(f"prompt {key!r} needs exactly one active version in cfg_ai_prompt, found {len(rows)}")
        if text_hash(rows[0][2]) != rows[0][3]:
            raise AiError(f"prompt {key!r} v{rows[0][1]}: the stored hash does not match its text (the register was edited outside the prompt step)")
        return rows[0]

    def options(self, overrides: dict | None = None) -> dict:
        opts = {"temperature": self.vals["ollama.temperature"], "num_ctx": self.vals["ollama.num_ctx"], "keep_alive": self.vals["ollama.keep_alive"]}
        for k, v in (overrides or {}).items():
            if k not in self.vals["ai.allowed_options"]:
                raise AiError(f"option {k!r} is not in cfg_setting ai.allowed_options {self.vals['ai.allowed_options']}")
            opts[k] = v
        return opts

    def render(self, prompt_row, variables: dict) -> str:
        text = prompt_row[2]
        named = set(re.findall(r"\{(\w+)\}", text))
        extra = set(variables) - named
        if extra:
            raise AiError(f"prompt {prompt_row[0]} has no place for the variable(s) {sorted(extra)}")
        for k, v in variables.items():
            text = text.replace("{" + k + "}", str(v))
        if "{{" in text:       # a prompt written for str.format keeps its JSON braces doubled: send them single
            text = text.replace("{{", "{").replace("}}", "}")
        return text

    # ---- the server ----------------------------------------------------------------------------------------------------------
    @contextlib.contextmanager
    def session(self, roles: list[str]):
        """The server check and the tunnel for the length of the block. Not used with an injected transport."""
        models = [self.model(r)[1] for r in roles]
        if not self.live:
            yield self
            return
        with sj.server_route(self.vals_for_route()) as route:
            sj.preflight(dict(route, model=models[0]))
            self.route = {"host": route["host"], "timeout_seconds": self.vals["ollama.timeout_seconds"]}
            try:
                yield self
            finally:
                self.route = {"host": self.vals["ollama.host"], "timeout_seconds": self.vals["ollama.timeout_seconds"]}

    def vals_for_route(self) -> dict:
        v = self.vals
        return {"host": v["ollama.host"], "connect_timeout_seconds": v["ollama.connect_timeout_seconds"], "ssh_target": v["ssh_target"],
                "ssh_key": v["ssh_key"], "tunnel_local_port": v["tunnel_local_port"], "timeout_seconds": v["ollama.timeout_seconds"]}

    # ---- the call ------------------------------------------------------------------------------------------------------------
    def _log(self, role, model, prompt, opts, text, subject, outcome, raw=None, result=None, error=None, meta=None, secs=None) -> int:
        meta = meta or {}
        cur = self.conn.execute(
            "INSERT INTO ai_call (batch_id, module, step, role, model_id, model_digest, prompt_id, options, request_hash, subject_kind, subject_id, "
            "request, answer, result, via, outcome, error, tokens_in, tokens_out, secs, run_id, created_by) "
            "VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            (self.batch_id, self.module, self.step, role, model[0], model[2], prompt[0] if prompt else None, json.dumps(opts, sort_keys=True),
             text_hash(text), subject[0], subject[1], text, raw, result, "aiclient", outcome, error, meta.get("tokens_in"), meta.get("tokens_out"),
             round(secs, 2) if secs is not None else None, self.run_id, "aiclient"))
        self.conn.commit()
        return cur.lastrowid

    def call(self, role: str, prompt_key: str, variables: dict, subject: tuple, check=None, result_of=None, overrides: dict | None = None, step: str | None = None) -> dict:
        """One question, up to 1 + ai.retries attempts, one ai_call row per attempt. check(answer) -> list of reasons the answer is not usable;
        result_of(answer) -> the short result stored in ai_call.result. Returns {call_id, outcome, answer, error}. Raises AiError (nothing written)
        for a refused model, prompt, variable or option; AiHalted after the halt rule."""
        saved_step = self.step
        if step:
            self.step = step
        try:
            return self._call(role, prompt_key, variables, subject, check, result_of, overrides)
        finally:
            self.step = saved_step

    def _call(self, role, prompt_key, variables, subject, check, result_of, overrides):
        model = self.model(role)
        prompt = self.prompt(prompt_key)
        if prompt[4] != role:
            raise AiError(f"prompt {prompt_key!r} is for role {prompt[4]!r}, not {role!r}")
        opts = self.options(overrides)
        text = self.render(prompt, variables)
        last = None
        for attempt in range(1 + int(self.vals["ai.retries"])):
            t0 = time.time()
            try:
                obj, raw, meta = self.transport(self.route, model[1], text, opts)
            except Exception as exc:  # network, timeout, unparsable JSON
                cid = self._log(role, model, prompt, opts, text, subject, "failed", error=f"call failed: {exc}"[:500], secs=time.time() - t0)
                last = {"call_id": cid, "outcome": "failed", "answer": None, "error": str(exc)}
                continue
            bad = check(obj) if check else []
            if bad:
                cid = self._log(role, model, prompt, opts, text, subject, "refused", raw=raw, error="; ".join(bad)[:500], meta=meta, secs=time.time() - t0)
                last = {"call_id": cid, "outcome": "refused", "answer": obj, "error": "; ".join(bad)}
                continue
            cid = self._log(role, model, prompt, opts, text, subject, "answered", raw=raw, result=result_of(obj) if result_of else None, meta=meta,
                            secs=time.time() - t0)
            self.streak = 0
            return {"call_id": cid, "outcome": "answered", "answer": obj, "error": None}
        self.streak += 1
        if self.streak >= int(self.vals["ai.max_consecutive_failures"]):
            self._log(role, model, prompt, opts, text, subject, "halted", error=f"{self.streak} questions in a row with no usable answer")
            raise AiHalted(f"{self.streak} questions in a row with no usable answer; what was answered is kept")
        return last

    def replay(self, call_id: int) -> dict:
        """Send a stored request again (the same model, options and text) and compare. Recorded as step 'replay' so no resolve step reads it."""
        row = self.conn.execute("SELECT role, model_id, request, options, answer, subject_kind, subject_id, result FROM ai_call WHERE id=?", (call_id,)).fetchone()
        if row is None:
            raise AiError(f"ai_call {call_id} does not exist")
        role, mid, text, opts, old, sk, sid, old_result = row
        model = self.conn.execute("SELECT id, name, digest FROM cfg_ai_model WHERE id=?", (mid,)).fetchone()
        if not text:
            raise AiError(f"ai_call {call_id} has no stored request to replay")
        saved = self.step
        self.step = "replay"
        t0 = time.time()
        try:
            obj, raw, meta = self.transport(self.route, model[1], text, json.loads(opts or "{}"))
            self._log(role, model, None, json.loads(opts or "{}"), text, (sk, sid), "answered", raw=raw, meta=meta, secs=time.time() - t0)
        except Exception as exc:
            self._log(role, model, None, json.loads(opts or "{}"), text, (sk, sid), "failed", error=str(exc)[:500], secs=time.time() - t0)
            raise AiError(f"the replay call failed: {exc}") from None
        finally:
            self.step = saved
        try:
            before = json.loads(old) if old else None
        except ValueError:
            before = None
        return {"same": before == obj, "before": before, "after": obj}

    def embed(self, role: str, texts: list, subject: tuple = (None, None)) -> list:
        """Vectors for texts, in batches of ai.embed_batch, with the model of the role (embed or embed_fast). One ai_call row per batch (step embed:
        request = the count and the hash of the texts, result = the count and the size of the vectors). Raises AiError when a batch fails (what was
        embedded is kept in the rows already written)."""
        model = self.model(role)
        size = int(self.vals["ai.embed_batch"])
        out: list = []
        for i in range(0, len(texts), size):
            chunk = texts[i:i + size]
            t0 = time.time()
            saved, self.step = self.step, "embed"
            try:
                try:
                    vecs = self.embedder(dict(self.route, keep_alive=self.vals["ollama.keep_alive"]), model[1], chunk)
                except Exception as exc:
                    self._log(role, model, None, {}, f"{len(chunk)} texts", subject, "failed", error=f"embed failed: {exc}"[:500], secs=time.time() - t0)
                    raise AiError(f"the embedding call failed: {exc}") from None
                if len(vecs) != len(chunk):
                    self._log(role, model, None, {}, f"{len(chunk)} texts", subject, "refused", error=f"{len(vecs)} vectors for {len(chunk)} texts", secs=time.time() - t0)
                    raise AiError(f"the server returned {len(vecs)} vectors for {len(chunk)} texts")
                self._log(role, model, None, {}, f"{len(chunk)} texts, hash {text_hash(chr(10).join(chunk))}", subject, "answered", result=f"{len(vecs)} vectors of {len(vecs[0]) if vecs else 0}",
                          secs=time.time() - t0)
            finally:
                self.step = saved
            out.extend(vecs)
        return out
