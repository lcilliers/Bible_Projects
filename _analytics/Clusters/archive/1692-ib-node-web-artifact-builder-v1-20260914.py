"""
Builds the "IB Node Web" HTML artifact (force-directed graph of ib_node rows) from a JSON
file shaped like {"ib_node": [...], "_phantom_observations"/"observations": [...]}.

Original run (2026-09-14, escalation #1692/#1699): DATA_PATH pointed at the phantom mockup
(1692-ib-node-mockup-generator-v1-20260914.py's own output). TO REUSE WITH REAL DATA: point
DATA_PATH at a real export of ib_node + ib_observation (same two-array shape -- rename the
observations key or adjust the loader below) and re-run; the template/JS need no other change,
since it only assumes the column names already in #1692's finalized schema.
"""
import json

DATA_PATH = r"C:\Bible_study_projects\_analytics\Clusters\1692-ib-node-phantom-mockup-100-v1-20260914.json"
OUT_PATH = r"C:\Bible_study_projects\_analytics\Clusters\1692-ib-node-web-v1-20260914.html"

with open(DATA_PATH, encoding="utf-8") as f:
    data = json.load(f)

nodes_json = json.dumps(data["ib_node"], indent=2)
obs_json = json.dumps(data["_phantom_observations"], indent=2)

TEMPLATE = """<!doctype html>
<title>The Node Web</title>
<style>
:root {
  --bg: #eceee8;
  --surface: #ffffff;
  --surface-2: #f5f6f1;
  --ink: #1c2430;
  --ink-2: #55606c;
  --ink-3: #838d82;
  --border: #d8dbd1;
  --accent: #2b4a5e;
  --accent-ink: #ffffff;
  --focus: #2b4a5e;

  --t-observation: #1baf7a;
  --t-strong: #eb6834;
  --t-verse: #2a78d6;
  --t-cluster: #008300;
  --t-subgroup: #e87ba4;
  --t-question: #eda100;

  --edge: #b9bfae;
  --edge-trace: #2b4a5e;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #14171a;
    --surface: #1b1f23;
    --surface-2: #20252a;
    --ink: #f1f2ee;
    --ink-2: #c4c8c2;
    --ink-3: #8b9098;
    --border: #33383d;
    --accent: #7fb8d6;
    --accent-ink: #10181d;
    --focus: #7fb8d6;

    --t-observation: #199e70;
    --t-strong: #d95926;
    --t-verse: #3987e5;
    --t-cluster: #2fae2f;
    --t-subgroup: #d55181;
    --t-question: #c98500;

    --edge: #3a4046;
    --edge-trace: #7fb8d6;
  }
}
:root[data-theme="dark"] {
  --bg: #14171a;
  --surface: #1b1f23;
  --surface-2: #20252a;
  --ink: #f1f2ee;
  --ink-2: #c4c8c2;
  --ink-3: #8b9098;
  --border: #33383d;
  --accent: #7fb8d6;
  --accent-ink: #10181d;
  --focus: #7fb8d6;

  --t-observation: #199e70;
  --t-strong: #d95926;
  --t-verse: #3987e5;
  --t-cluster: #2fae2f;
  --t-subgroup: #d55181;
  --t-question: #c98500;

  --edge: #3a4046;
  --edge-trace: #7fb8d6;
}

* { box-sizing: border-box; }

body {
  background: var(--bg);
  color: var(--ink);
  font-family: "Source Sans 3", system-ui, -apple-system, "Segoe UI", sans-serif;
  height: 100vh;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.mono { font-family: "IBM Plex Mono", ui-monospace, SFMono-Regular, monospace; }

h1, h2, h3 { font-family: "Fraunces", Georgia, serif; text-wrap: balance; margin: 0; }

/* ---------- header ---------- */
header {
  display: flex;
  align-items: center;
  gap: 16px;
  padding: 12px 20px;
  border-bottom: 1px solid var(--border);
  background: var(--surface);
  flex: 0 0 auto;
}
header h1 { font-size: 1.35rem; font-weight: 600; letter-spacing: 0.01em; }
header .subtitle { color: var(--ink-2); font-size: 0.82rem; margin-top: 2px; }
.phantom-badge {
  font-family: "IBM Plex Mono", monospace;
  font-size: 0.68rem;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: var(--t-strong);
  border: 1px solid color-mix(in srgb, var(--t-strong) 45%, transparent);
  background: color-mix(in srgb, var(--t-strong) 10%, var(--surface));
  padding: 3px 9px;
  border-radius: 999px;
  white-space: nowrap;
}
.stat-strip {
  margin-left: auto;
  display: flex;
  gap: 18px;
  font-family: "IBM Plex Mono", monospace;
  font-variant-numeric: tabular-nums;
}
.stat-strip .stat { text-align: right; }
.stat-strip .stat b { display: block; font-size: 1.05rem; color: var(--ink); line-height: 1.1; }
.stat-strip .stat span { font-size: 0.66rem; color: var(--ink-3); text-transform: uppercase; letter-spacing: 0.06em; }

/* ---------- layout ---------- */
.shell {
  flex: 1 1 auto;
  display: grid;
  grid-template-columns: 260px 1fr 320px;
  min-height: 0;
}
@media (max-width: 980px) {
  .shell { grid-template-columns: 1fr; grid-template-rows: auto 1fr auto; overflow-y: auto; }
  #canvas-wrap { min-height: 60vh; }
}

aside {
  background: var(--surface);
  overflow-y: auto;
  padding: 16px;
  display: flex;
  flex-direction: column;
  gap: 18px;
}
#rail-left { border-right: 1px solid var(--border); }
#rail-right { border-left: 1px solid var(--border); }

.panel-title {
  font-size: 0.7rem;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--ink-3);
  font-weight: 600;
  margin-bottom: 8px;
}

.legend-row {
  display: flex;
  align-items: center;
  gap: 9px;
  padding: 5px 0;
  cursor: pointer;
  user-select: none;
  border-radius: 6px;
}
.legend-row:hover { background: var(--surface-2); }
.legend-row.off { opacity: 0.35; }
.legend-swatch { width: 15px; height: 15px; flex: 0 0 auto; }
.legend-label { flex: 1 1 auto; font-size: 0.86rem; }
.legend-count { font-family: "IBM Plex Mono", monospace; font-size: 0.74rem; color: var(--ink-3); }

fieldset { border: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 6px; }
.chip-row { display: flex; flex-wrap: wrap; gap: 6px; }
.chip {
  font-size: 0.76rem;
  padding: 4px 10px;
  border-radius: 999px;
  border: 1px solid var(--border);
  background: var(--surface-2);
  color: var(--ink-2);
  cursor: pointer;
}
.chip.active { background: var(--accent); border-color: var(--accent); color: var(--accent-ink); }

input[type="search"] {
  width: 100%;
  padding: 7px 10px;
  border-radius: 8px;
  border: 1px solid var(--border);
  background: var(--surface-2);
  color: var(--ink);
  font-size: 0.86rem;
}
input[type="search"]:focus { outline: 2px solid var(--focus); outline-offset: 1px; }

.note {
  font-size: 0.78rem;
  line-height: 1.5;
  color: var(--ink-2);
  background: var(--surface-2);
  border: 1px solid var(--border);
  border-radius: 8px;
  padding: 10px 12px;
}
.note b { color: var(--ink); }

#canvas-wrap { position: relative; background: var(--surface-2); min-width: 0; }
#graph { width: 100%; height: 100%; display: block; cursor: grab; }
#graph:active { cursor: grabbing; }

.tooltip {
  position: absolute;
  pointer-events: none;
  background: var(--ink);
  color: var(--bg);
  font-size: 0.78rem;
  padding: 7px 10px;
  border-radius: 7px;
  max-width: 240px;
  line-height: 1.4;
  opacity: 0;
  transition: opacity 0.08s;
  z-index: 5;
}
.tooltip b { font-family: "IBM Plex Mono", monospace; }

.zoom-controls {
  position: absolute;
  right: 14px;
  bottom: 14px;
  display: flex;
  flex-direction: column;
  gap: 6px;
}
.zoom-controls button {
  width: 30px; height: 30px;
  border-radius: 7px;
  border: 1px solid var(--border);
  background: var(--surface);
  color: var(--ink);
  font-size: 1rem;
  cursor: pointer;
}
.zoom-controls button:hover { background: var(--surface-2); }

/* inspector */
#inspector-empty { color: var(--ink-3); font-size: 0.85rem; line-height: 1.6; }
.insp-type {
  display: inline-flex; align-items: center; gap: 6px;
  font-size: 0.7rem; text-transform: uppercase; letter-spacing: 0.07em;
  color: var(--ink-2); margin-bottom: 6px;
}
.insp-title { font-size: 1.15rem; margin-bottom: 4px; word-break: break-word; }
.insp-meta { font-size: 0.8rem; color: var(--ink-2); margin-bottom: 14px; }
.insp-section-title {
  font-size: 0.68rem; text-transform: uppercase; letter-spacing: 0.07em;
  color: var(--ink-3); margin: 14px 0 6px;
}
.link-list { display: flex; flex-direction: column; gap: 3px; }
.link-item {
  display: flex; align-items: center; gap: 7px;
  font-size: 0.82rem; padding: 5px 7px; border-radius: 6px;
  cursor: pointer; border: 1px solid transparent;
}
.link-item:hover { background: var(--surface-2); border-color: var(--border); }
.link-item .dot { width: 9px; height: 9px; border-radius: 50%; flex: 0 0 auto; }
.row-card {
  font-size: 0.76rem;
  border: 1px solid var(--border);
  border-radius: 7px;
  padding: 7px 9px;
  margin-bottom: 6px;
  line-height: 1.5;
}
.row-card .rid { color: var(--ink-3); }

::-webkit-scrollbar { width: 9px; height: 9px; }
::-webkit-scrollbar-thumb { background: var(--border); border-radius: 5px; }
</style>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600&family=Source+Sans+3:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">

<header>
  <div>
    <h1>The Node Web</h1>
    <div class="subtitle">ib_node relational prototype &mdash; escalation #1692</div>
  </div>
  <span class="phantom-badge">Phantom data</span>
  <div class="stat-strip">
    <div class="stat"><b id="stat-nodes">&mdash;</b><span>entities</span></div>
    <div class="stat"><b id="stat-edges">&mdash;</b><span>relations</span></div>
    <div class="stat"><b id="stat-obs">&mdash;</b><span>observations</span></div>
  </div>
</header>

<div class="shell">
  <aside id="rail-left">
    <div>
      <div class="panel-title">Entity types</div>
      <div id="legend"></div>
    </div>
    <div>
      <div class="panel-title">Stage</div>
      <fieldset id="stage-filter">
        <div class="chip-row" id="stage-chips"></div>
      </fieldset>
    </div>
    <div>
      <div class="panel-title">Find a code</div>
      <input type="search" id="search" placeholder="e.g. H0816, Matt.5.22, M10&hellip;">
    </div>
    <div class="note">
      <b>Reading the web:</b> every line is one <span class="mono">ib_node</span> row's
      reference &mdash; observation&nbsp;&rarr;&nbsp;strong, verse, cluster, subgroup, question,
      or another observation. A strong or verse cited by several observations pulls them into
      one visible cluster; that clustering <i>is</i> the relational analysis.
    </div>
  </aside>

  <div id="canvas-wrap">
    <svg id="graph"></svg>
    <div class="tooltip" id="tooltip"></div>
    <div class="zoom-controls">
      <button id="zoom-in" title="Zoom in" aria-label="Zoom in">+</button>
      <button id="zoom-out" title="Zoom out" aria-label="Zoom out">&minus;</button>
      <button id="zoom-reset" title="Reset view" aria-label="Reset view">&#8634;</button>
    </div>
  </div>

  <aside id="rail-right">
    <div class="panel-title">Inspector</div>
    <div id="inspector">
      <div id="inspector-empty">Click any node to see what it connects to, or hover to trace
      one relation at a time. Drag nodes to untangle the web; scroll to zoom.</div>
    </div>
  </aside>
</div>

<script src="https://cdnjs.cloudflare.com/ajax/libs/d3/7.9.0/d3.min.js"></script>
<script>
// ---------------------------------------------------------------------------
// PHANTOM DATA -- not grounded in real results. Generated for escalation #1692
// (ib_node), researcher request 2026-09-14, to prototype the relational-web
// shape before ib_node/ib_observation exist for real. Schema matches
// iba/docs/1692-ib-node-finalization-v1-20260912.md sec1.
// ---------------------------------------------------------------------------
const PHANTOM_OBSERVATIONS = __OBS_JSON__;
const IB_NODE = __NODES_JSON__;

const TYPE_META = {
  observation: { label: "Observation",  plural: "Observations", color: "var(--t-observation)", symbol: d3.symbolCircle,   size: 1.0 },
  strong:      { label: "Strong's code", plural: "Strongs",      color: "var(--t-strong)",      symbol: d3.symbolDiamond,  size: 1.15 },
  verse:       { label: "Verse",         plural: "Verses",       color: "var(--t-verse)",       symbol: d3.symbolSquare,   size: 0.95 },
  cluster:     { label: "Cluster",       plural: "Clusters",     color: "var(--t-cluster)",     symbol: d3.symbolStar,     size: 1.35 },
  subgroup:    { label: "Subgroup",      plural: "Subgroups",    color: "var(--t-subgroup)",    symbol: d3.symbolTriangle, size: 1.1 },
  question:    { label: "Catalogue Q",   plural: "Questions",    color: "var(--t-question)",    symbol: d3.symbolCross,    size: 1.0 },
};
const TYPE_ORDER = ["observation", "strong", "verse", "cluster", "subgroup", "question"];

const STAGE_LABEL = { reading: "Reading", answer: "Answer", synthesis: "Synthesis", subgroup: "Subgroup (b)" };

// ---- build the node/edge model -------------------------------------------

const obsById = new Map(PHANTOM_OBSERVATIONS.map(o => [o.id, o]));
const nodeMap = new Map(); // key -> node object
const linkList = [];       // {source, target, kind}

function getNode(type, code, extra) {
  const key = type + ":" + code;
  if (!nodeMap.has(key)) {
    nodeMap.set(key, Object.assign({ id: key, type, code, degree: 0, rows: [] }, extra || {}));
  }
  return nodeMap.get(key);
}

for (const o of PHANTOM_OBSERVATIONS) {
  getNode("observation", "obs:" + o.id, { obsId: o.id, stage: o.stage, tag: o.tag, cluster_code: o.cluster_code });
}

function addLink(a, b, kind, row) {
  if (!a || !b || a === b) return;
  linkList.push({ source: a.id, target: b.id, kind, row });
  a.degree++; b.degree++;
  a.rows.push(row); b.rows.push(row);
}

for (const r of IB_NODE) {
  const obs = obsById.get(r.observation_id);
  const oNode = getNode("observation", "obs:" + r.observation_id, { obsId: r.observation_id, stage: obs.stage, tag: obs.tag, cluster_code: obs.cluster_code });

  const cNode = getNode("cluster", r.cluster_code);
  addLink(oNode, cNode, "cluster", r);

  let sgNode = null;
  if (r.cluster_subgroup_code) {
    sgNode = getNode("subgroup", r.cluster_subgroup_code, { cluster_code: r.cluster_code });
    addLink(oNode, sgNode, "subgroup", r);
  }

  let stNode = null;
  if (r.strong) {
    stNode = getNode("strong", r.strong);
    addLink(oNode, stNode, "strong", r);
  }

  let vNode = null;
  if (r.verse_reference) {
    vNode = getNode("verse", r.verse_reference);
    addLink(oNode, vNode, "verse", r);
  }

  if (r.question_code) {
    const qNode = getNode("question", r.question_code);
    addLink(oNode, qNode, "question", r);
  }

  if (r.traced_observation_id) {
    const tNode = getNode("observation", "obs:" + r.traced_observation_id, (() => {
      const to = obsById.get(r.traced_observation_id);
      return { obsId: r.traced_observation_id, stage: to.stage, tag: to.tag, cluster_code: to.cluster_code };
    })());
    addLink(oNode, tNode, "trace", r);
  }

  if (stNode && vNode) addLink(stNode, vNode, "cooccurrence", r);
}

const nodes = Array.from(nodeMap.values());
const links = linkList;

document.getElementById("stat-nodes").textContent = nodes.length;
document.getElementById("stat-edges").textContent = links.length;
document.getElementById("stat-obs").textContent = PHANTOM_OBSERVATIONS.length;

// ---- legend ---------------------------------------------------------------

const activeTypes = new Set(TYPE_ORDER);
const legendEl = document.getElementById("legend");
for (const t of TYPE_ORDER) {
  const meta = TYPE_META[t];
  const count = nodes.filter(n => n.type === t).length;
  const row = document.createElement("div");
  row.className = "legend-row";
  row.dataset.type = t;
  row.innerHTML = `<svg class="legend-swatch" viewBox="-8 -8 16 16">
      <path d="${d3.symbol(meta.symbol, 90)()}" fill="${meta.color}"></path>
    </svg>
    <span class="legend-label">${meta.plural}</span>
    <span class="legend-count mono">${count}</span>`;
  row.addEventListener("click", () => {
    if (activeTypes.has(t)) { activeTypes.delete(t); row.classList.add("off"); }
    else { activeTypes.add(t); row.classList.remove("off"); }
    applyFilters();
  });
  legendEl.appendChild(row);
}

// ---- stage chips ------------------------------------------------------------

const activeStages = new Set(Object.keys(STAGE_LABEL));
const stageChipsEl = document.getElementById("stage-chips");
for (const [s, label] of Object.entries(STAGE_LABEL)) {
  const chip = document.createElement("div");
  chip.className = "chip active";
  chip.textContent = label;
  chip.addEventListener("click", () => {
    if (activeStages.has(s)) { activeStages.delete(s); chip.classList.remove("active"); }
    else { activeStages.add(s); chip.classList.add("active"); }
    applyFilters();
  });
  stageChipsEl.appendChild(chip);
}

// ---- render -----------------------------------------------------------------

const svg = d3.select("#graph");
const wrap = document.getElementById("canvas-wrap");
const g = svg.append("g");
const linkLayer = g.append("g").attr("class", "links");
const nodeLayer = g.append("g").attr("class", "nodes");
const tooltip = document.getElementById("tooltip");

function sizeSvg() {
  const w = wrap.clientWidth, h = wrap.clientHeight;
  svg.attr("width", w).attr("height", h).attr("viewBox", [0, 0, w, h]);
  return { w, h };
}
let { w, h } = sizeSvg();

const zoom = d3.zoom().scaleExtent([0.25, 4]).on("zoom", (event) => {
  g.attr("transform", event.transform);
});
svg.call(zoom);
document.getElementById("zoom-in").onclick = () => svg.transition().duration(200).call(zoom.scaleBy, 1.4);
document.getElementById("zoom-out").onclick = () => svg.transition().duration(200).call(zoom.scaleBy, 1 / 1.4);
document.getElementById("zoom-reset").onclick = () => svg.transition().duration(300).call(zoom.transform, d3.zoomIdentity);

const linkSel = linkLayer.selectAll("line")
  .data(links)
  .join("line")
  .attr("stroke", d => d.kind === "trace" ? "var(--edge-trace)" : "var(--edge)")
  .attr("stroke-width", d => d.kind === "trace" ? 1.6 : d.kind === "cooccurrence" ? 0.7 : 1.1)
  .attr("stroke-dasharray", d => d.kind === "trace" ? "2,3" : d.kind === "cooccurrence" ? "1,3" : null)
  .attr("stroke-opacity", d => d.kind === "cooccurrence" ? 0.35 : 0.55);

function radius(d) {
  const base = 5 + Math.sqrt(d.degree) * 2.1;
  return base * TYPE_META[d.type].size;
}

const nodeSel = nodeLayer.selectAll("g.node")
  .data(nodes)
  .join("g")
  .attr("class", "node")
  .call(d3.drag()
    .on("start", (event, d) => { if (!event.active) sim.alphaTarget(0.25).restart(); d.fx = d.x; d.fy = d.y; })
    .on("drag", (event, d) => { d.fx = event.x; d.fy = event.y; })
    .on("end", (event, d) => { if (!event.active) sim.alphaTarget(0); d.fx = null; d.fy = null; }));

nodeSel.append("path")
  .attr("d", d => d3.symbol(TYPE_META[d.type].symbol, Math.PI * radius(d) * radius(d))())
  .attr("fill", d => TYPE_META[d.type].color)
  .attr("stroke", "var(--surface)")
  .attr("stroke-width", 1.4)
  .attr("fill-opacity", 0.92);

nodeSel.append("title").text(d => d.code);

nodeSel.on("mouseenter", (event, d) => {
    highlight(d);
    tooltip.style.opacity = 1;
    tooltip.innerHTML = tooltipHtml(d);
  })
  .on("mousemove", (event) => {
    const bounds = wrap.getBoundingClientRect();
    tooltip.style.left = (event.clientX - bounds.left + 16) + "px";
    tooltip.style.top = (event.clientY - bounds.top + 12) + "px";
  })
  .on("mouseleave", () => { tooltip.style.opacity = 0; clearHighlight(); })
  .on("click", (event, d) => { event.stopPropagation(); inspect(d); });

svg.on("click", () => { d3.select("#inspector-empty"); showEmptyInspector(); });

function tooltipHtml(d) {
  const meta = TYPE_META[d.type];
  let extra = "";
  if (d.type === "observation") extra = `<br>${STAGE_LABEL[d.stage]} &middot; ${d.cluster_code}${d.tag ? " &middot; " + d.tag : ""}`;
  return `<b>${d.code.includes(":") ? d.code.split(":")[1] : d.code}</b> &mdash; ${meta.label}${extra}<br>${d.degree} connection${d.degree === 1 ? "" : "s"}`;
}

const sim = d3.forceSimulation(nodes)
  .force("link", d3.forceLink(links).id(d => d.id).distance(d => d.kind === "trace" ? 90 : d.kind === "cooccurrence" ? 40 : 62).strength(d => d.kind === "cooccurrence" ? 0.15 : 0.5))
  .force("charge", d3.forceManyBody().strength(d => -70 - d.degree * 6))
  .force("center", d3.forceCenter(w / 2, h / 2))
  .force("collide", d3.forceCollide(d => radius(d) + 6))
  .on("tick", ticked);

function ticked() {
  linkSel.attr("x1", d => d.source.x).attr("y1", d => d.source.y)
         .attr("x2", d => d.target.x).attr("y2", d => d.target.y);
  nodeSel.attr("transform", d => `translate(${d.x},${d.y})`);
}

// let it settle, then ease charge down a touch for a calmer resting layout
setTimeout(() => { sim.alphaTarget(0); }, 3000);

window.addEventListener("resize", () => {
  const s = sizeSvg(); w = s.w; h = s.h;
  sim.force("center", d3.forceCenter(w / 2, h / 2));
  sim.alpha(0.3).restart();
});

// ---- highlight on hover -----------------------------------------------------

function neighborsOf(d) {
  const set = new Set([d.id]);
  for (const l of links) {
    if (l.source.id === d.id) set.add(l.target.id);
    if (l.target.id === d.id) set.add(l.source.id);
  }
  return set;
}

function highlight(d) {
  const neigh = neighborsOf(d);
  nodeSel.style("opacity", n => neigh.has(n.id) ? 1 : 0.15);
  linkSel.style("opacity", l => (l.source.id === d.id || l.target.id === d.id) ? 0.9 : 0.05);
}
function clearHighlight() {
  nodeSel.style("opacity", 1);
  linkSel.style("opacity", null);
}

// ---- filters ------------------------------------------------------------

function applyFilters() {
  const visible = new Set();
  for (const n of nodes) {
    if (!activeTypes.has(n.type)) continue;
    if (n.type === "observation" && !activeStages.has(n.stage)) continue;
    visible.add(n.id);
  }
  nodeSel.style("display", n => visible.has(n.id) ? null : "none");
  linkSel.style("display", l => (visible.has(l.source.id) && visible.has(l.target.id)) ? null : "none");
}

// ---- search --------------------------------------------------------------

document.getElementById("search").addEventListener("input", (e) => {
  const q = e.target.value.trim().toLowerCase();
  if (!q) { clearHighlight(); return; }
  const matches = nodes.filter(n => n.code.toLowerCase().includes(q));
  const matchIds = new Set(matches.map(n => n.id));
  nodeSel.style("opacity", n => matchIds.has(n.id) ? 1 : 0.1);
  linkSel.style("opacity", l => (matchIds.has(l.source.id) || matchIds.has(l.target.id)) ? 0.6 : 0.04);
  if (matches.length === 1) inspect(matches[0]);
});

// ---- inspector ------------------------------------------------------------

const inspectorEl = document.getElementById("inspector");

function showEmptyInspector() {
  inspectorEl.innerHTML = `<div id="inspector-empty">Click any node to see what it connects to,
    or hover to trace one relation at a time. Drag nodes to untangle the web; scroll to zoom.</div>`;
}

function inspect(d) {
  const meta = TYPE_META[d.type];
  const label = d.code.includes(":") ? d.code.split(":")[1] : d.code;
  const neigh = [];
  const seen = new Set();
  for (const l of links) {
    let other = null;
    if (l.source.id === d.id) other = l.target;
    else if (l.target.id === d.id) other = l.source;
    if (other && !seen.has(other.id)) { seen.add(other.id); neigh.push(other); }
  }
  neigh.sort((a, b) => TYPE_ORDER.indexOf(a.type) - TYPE_ORDER.indexOf(b.type) || b.degree - a.degree);

  let metaLine = `${meta.label} &middot; ${d.degree} connection${d.degree === 1 ? "" : "s"}`;
  if (d.type === "observation") {
    metaLine = `${STAGE_LABEL[d.stage]} stage &middot; ${d.cluster_code}${d.tag ? " &middot; tag: " + d.tag : ""}`;
  }

  let html = `<span class="insp-type">${meta.plural}</span>
    <div class="insp-title mono">${label}</div>
    <div class="insp-meta">${metaLine}</div>`;

  html += `<div class="insp-section-title">Connects to (${neigh.length})</div><div class="link-list">`;
  for (const n of neigh.slice(0, 40)) {
    const nl = n.code.includes(":") ? n.code.split(":")[1] : n.code;
    html += `<div class="link-item" data-target="${n.id}">
      <span class="dot" style="background:${TYPE_META[n.type].color}"></span>
      <span class="mono">${nl}</span>
      <span style="margin-left:auto;color:var(--ink-3);font-size:0.72rem">${TYPE_META[n.type].label}</span>
    </div>`;
  }
  html += `</div>`;

  if (d.rows && d.rows.length) {
    const uniqueRows = Array.from(new Map(d.rows.map(r => [r.id, r])).values()).sort((a, b) => a.id - b.id);
    html += `<div class="insp-section-title">Source ib_node rows (${uniqueRows.length})</div>`;
    for (const r of uniqueRows.slice(0, 12)) {
      html += `<div class="row-card"><span class="rid mono">#${r.id}</span> obs <span class="mono">${r.observation_id}</span>
        &middot; seq <span class="mono">${r.seq}</span> &middot; ${r.source_stage}<br>
        ${[r.strong, r.verse_reference, r.cluster_subgroup_code, r.question_code, r.traced_observation_id ? "&rarr; obs " + r.traced_observation_id : null]
          .filter(Boolean).map(x => `<span class="mono">${x}</span>`).join(" &middot; ") || "<span style=\\"color:var(--ink-3)\\">cluster-level only</span>"}
      </div>`;
    }
  }

  inspectorEl.innerHTML = html;
  inspectorEl.querySelectorAll(".link-item").forEach(el => {
    el.addEventListener("click", () => {
      const target = nodeMap.get(el.dataset.target);
      if (target) inspect(target);
    });
  });

  clearHighlight();
  highlight(d);
}

applyFilters();
</script>
"""

html = TEMPLATE.replace("__NODES_JSON__", nodes_json).replace("__OBS_JSON__", obs_json)

with open(OUT_PATH, "w", encoding="utf-8") as f:
    f.write(html)

print("wrote", OUT_PATH, len(html), "bytes")
