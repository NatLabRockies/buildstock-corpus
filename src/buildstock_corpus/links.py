"""Absolute URLs for where a document's source lives and where its publication lives.

A consumer who fetched one Markdown file over HTTPS has no clone, no manifest and no map,
so anything it needs in order to cite the file has to be written into the file (W2.1) or
be one fetch away in the manifest (W2.2). Two links do that:

  source_url       the upstream file at the commit the corpus was built from -- a GitHub
                   file URL carrying the commit hash, so it resolves to the same bytes
                   next year. For a document fetched from OSTI it is the OSTI URL.
  publication_url  the human-readable publication a reader should be sent to: the live
                   ComStock-site page for a site page, the file the site serves for a
                   site-served PDF, the release's reference-documentation PDF for a
                   technical-reference chapter, and the OSTI URL for an OSTI report.

Everything here is pure string building from facts the build already holds (the clone
record's repo and sha, the source registry's site_url / publication_url, the fetch
state's PDF URLs). Nothing is fetched; test_links_network.py is where the URLs are proven
to resolve.
"""

from __future__ import annotations

from urllib.parse import quote

_GITHUB = "https://github.com/"


def _quote_path(path: str) -> str:
    """Percent-encode a repo-relative path for use in a URL, keeping the slashes."""
    return quote(path.strip("/"), safe="/")


def repo_web_url(repo: str) -> str:
    """The browsable URL of a clone URL: strip `.git`, normalise a scheme-less owner/name."""
    repo = repo.strip().rstrip("/")
    if repo.endswith(".git"):
        repo = repo[: -len(".git")]
    if repo.startswith("git@github.com:"):
        repo = _GITHUB + repo[len("git@github.com:"):]
    elif "://" not in repo:
        repo = _GITHUB + repo.lstrip("/")
    return repo


def repo_file_url(repo: str, sha: str, path: str) -> str:
    """GitHub file URL at an exact commit: .../blob/<sha>/<path>.

    The sha, not the branch or tag name, so the link cannot move when upstream rewrites
    a tag or advances a branch.
    """
    if not sha:
        raise ValueError(f"repo_file_url: no commit sha for {repo} / {path}")
    return f"{repo_web_url(repo)}/blob/{sha}/{_quote_path(path)}"


def site_file_url(site_url: str, path: str) -> str:
    """URL of a file the site serves as-is (a PDF under assets/, an image)."""
    return f"{site_url.rstrip('/')}/{_quote_path(path)}"


def site_page_url(site_url: str, source_path: str) -> str:
    """URL of the rendered page for a Jekyll source file: docs/a/b.md -> docs/a/b.html.

    Holds for every page in the ComStock site repo because none sets its own permalink;
    a page that did would need a registry override rather than this rule.
    """
    path = source_path.strip("/")
    if path.endswith(".md"):
        path = path[: -len(".md")] + ".html"
    return site_file_url(site_url, path)


def is_absolute_https(url: str | None) -> bool:
    return isinstance(url, str) and url.startswith("https://") and len(url) > len("https://")
