"""Every source_url and publication_url in the release manifest must resolve (W2.2's check).

Deselected by default (see pyproject addopts); run `pytest -m network` after a rebuild to
prove the links live. Fetches each distinct URL once with a HEAD request, falling back to
GET for hosts that refuse HEAD, and reports every failure rather than stopping at the first.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.request

import pytest

from buildstock_corpus.paths import manifest_file

RELEASE = "comstock_amy2018_2025_release_3"
UA = {"User-Agent": "buildstock-corpus link check"}


def _status(url: str) -> int:
    for method in ("HEAD", "GET"):
        req = urllib.request.Request(url, method=method, headers=UA)
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                return resp.status
        except urllib.error.HTTPError as e:
            if method == "HEAD" and e.code in (403, 405):
                continue
            return e.code
    return 0


@pytest.mark.network
def test_every_manifest_link_resolves():
    mf = manifest_file("comstock", RELEASE)
    if not mf.is_file():
        pytest.skip("no built manifest for this release")
    manifest = json.loads(mf.read_text(encoding="utf-8"))
    urls = sorted({
        a[field]
        for s in manifest["sources"]
        for a in s["artifacts"]
        for field in ("source_url", "publication_url")
    })
    assert urls, "manifest has no links to check"

    failures = {u: code for u in urls if (code := _status(u)) != 200}
    assert not failures, "links not resolving:\n" + "\n".join(f"  {c} {u}" for u, c in failures.items())
