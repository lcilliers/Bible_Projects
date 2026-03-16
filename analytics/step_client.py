"""
step_client.py
──────────────
Thin wrapper around the STEP Bible public API for use within the
Bible_verse_analytics module.

The STEP Bible API is publicly accessible without an API key.
See docs/step_setup.md for full configuration instructions.
"""

import os
from typing import Optional

import requests
from dotenv import load_dotenv

ROOT_DIR = os.path.join(os.path.dirname(__file__), "..")
load_dotenv(os.path.join(ROOT_DIR, ".env"))


class StepClient:
    """Client for the STEP Bible public HTTP API.

    Configuration is read from environment variables (`.env`):
      - STEP_API_BASE_URL      — default: https://www.stepbible.org/api
      - STEP_DEFAULT_VERSION   — default: ESV
      - STEP_REQUEST_TIMEOUT   — default: 10 (seconds)
    """

    def __init__(self) -> None:
        self.base_url = os.getenv(
            "STEP_API_BASE_URL", "https://www.stepbible.org/api"
        ).rstrip("/")
        self.default_version = os.getenv("STEP_DEFAULT_VERSION", "ESV")
        self.timeout = int(os.getenv("STEP_REQUEST_TIMEOUT", "10"))

    # ── Internal helpers ────────────────────────────────────────────────────

    def _get(self, path: str) -> dict:
        """Perform a GET request and return the parsed JSON response."""
        url = f"{self.base_url}/{path.lstrip('/')}"
        response = requests.get(url, timeout=self.timeout)
        response.raise_for_status()
        return response.json()

    # ── Public API ──────────────────────────────────────────────────────────

    def get_passage(self, reference: str, version: Optional[str] = None) -> dict:
        """Retrieve a Bible passage by reference.

        Parameters
        ----------
        reference : str
            Passage reference in dot notation, e.g. ``"John.3.16"`` or
            ``"Gen.1.1-Gen.1.3"``.
        version : str, optional
            Bible version/translation code (e.g. ``"ESV"``, ``"NIV"``).
            Defaults to ``STEP_DEFAULT_VERSION`` from the environment.

        Returns
        -------
        dict
            Raw JSON response from the STEP Bible API.
        """
        v = version or self.default_version
        return self._get(f"bible/passage/{v}/{reference}")

    def search(self, query: str, version: Optional[str] = None) -> list:
        """Search for a word or phrase across the Bible.

        Parameters
        ----------
        query : str
            Search term or phrase, e.g. ``"grace"`` or ``"love of God"``.
        version : str, optional
            Bible version/translation code. Defaults to
            ``STEP_DEFAULT_VERSION`` from the environment.

        Returns
        -------
        list
            List of verse result dicts from the STEP Bible API response.
        """
        v = version or self.default_version
        data = self._get(f"bible/search/{v}/{query}")
        # The API may wrap results under a key; return the list if present.
        if isinstance(data, list):
            return data
        return data.get("results", data.get("verses", []))

    def get_versions(self) -> list:
        """Return the list of available Bible versions from the API.

        Returns
        -------
        list
            List of version dicts (each typically contains ``"shortName"``
            and ``"longName"`` fields).
        """
        data = self._get("bible/versions")
        if isinstance(data, list):
            return data
        return data.get("versions", [])
