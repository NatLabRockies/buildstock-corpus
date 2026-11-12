"""Collapsible <details> blocks on a site page become headings (R3.2 of PLAN-resstock.md).

ResStock's FAQ page is 48 `<details><summary>question</summary><p>answer</p></details>`
blocks of raw HTML: every answer was in the corpus, but no question was a heading, so the
page had five sections and a chunk could not be filed under the question it answers. The
markdown extractor unfolds each block: the summary becomes a heading one level below the
heading it sits under, and the simple HTML of the answer becomes markdown.
"""

from __future__ import annotations

import buildstock_corpus.extract.markdown as M

FAQ = """---
title: FAQ
---
# Frequently Asked Questions
{: .fw-500}

## ResStock Essentials

<details>
    <summary>Is ResStock credible?</summary>
    <p>Yes. See the <a href="https://example.org/eulp">EULP
    report</a> and <b>calibration</b> notes.</p>
</details>

<details>
    <summary>What timeseries data are available?</summary>
    <p>Provided for multiple geographic levels:</p>
    <ul>
        <li>State</li>
        <li>ISO/RTO region</li>
    </ul>
    <p>Files are split by <i>dwelling type</i>.</p>
</details>

## Data Viewer
"""


def test_each_question_becomes_a_heading_under_its_section():
    title, body, published = M.clean_markdown(FAQ)
    assert (title, published) == ("FAQ", True)
    assert body.splitlines() == [
        "# Frequently Asked Questions",
        "",
        "## ResStock Essentials",
        "",
        "### Is ResStock credible?",
        "",
        "Yes. See the [EULP report](https://example.org/eulp) and **calibration** notes.",
        "",
        "### What timeseries data are available?",
        "",
        "Provided for multiple geographic levels:",
        "",
        "- State",
        "- ISO/RTO region",
        "",
        "Files are split by *dwelling type*.",
        "",
        "## Data Viewer",
    ]
    assert "<details" not in body and "<summary" not in body and "<p>" not in body


def test_nested_blocks_step_down_a_level_and_attributes_are_ignored():
    src = (
        "# Publications\n\n"
        '<details markdown="block" class="level1" open>\n'
        '  <summary class="pub-header">NLR Reports</summary>\n\n'
        '  <details markdown="block" class="level2" open><summary class="pub-header">Reports and Papers</summary>\n'
        "  [A paper](https://example.org/a). Presents a framework.\n\n"
        "  </details>\n"
        "</details>\n\n"
        "After.\n"
    )
    out = M._unfold_details(src)
    lines = [ln.strip() for ln in out.splitlines() if ln.strip()]
    assert lines == [
        "# Publications",
        "## NLR Reports",
        "### Reports and Papers",
        "[A paper](https://example.org/a). Presents a framework.",
        "After.",
    ]


def test_a_multi_line_summary_is_one_heading_and_depth_stops_at_h6():
    src = "##### Deep\n\n<details>\n<summary>\n   Affected fields\n   (click to expand)\n</summary>\n<details><summary>Inner</summary>x</details>\n</details>\n"
    out = M._unfold_details(src)
    assert "###### Affected fields (click to expand)" in out
    assert "###### Inner" in out and "#######" not in out


def test_a_page_with_no_details_block_is_untouched_and_other_html_is_left():
    plain = "# Title\n\n<p>kept as written</p>\n\n<summary>stray</summary>\n"
    assert M._unfold_details(plain) == plain
    with_pre = "<details><summary>Q</summary>\n<pre><code>SELECT 1 < 2</code></pre>\n</details>\n"
    assert "<pre><code>SELECT 1 < 2</code></pre>" in M._unfold_details(with_pre)


def test_a_heading_inside_a_fence_does_not_set_the_level():
    src = "## Section\n\n```\n#### not a heading\n```\n\n<details><summary>Q</summary><p>A</p></details>\n"
    assert "\n### Q\n" in M._unfold_details(src)


def test_a_body_indented_under_its_tag_is_not_left_as_a_code_block():
    src = (
        "## Essentials\n\n<details>\n    <summary>Is it credible?</summary>\n"
        "    <p>Yes, it was calibrated.\n\n"
        '    For details see <a href="https://example.org/x">this explanation</a>.</p>\n'
        "    <pre><code>import pandas as pd\nfile = 1\n    </code></pre>\n"
        "</details>\n"
    )
    out = M._unfold_details(src)
    assert "\nFor details see [this explanation](https://example.org/x).\n" in out
    assert "\n<pre><code>import pandas as pd\nfile = 1\n    </code></pre>\n" in out
    assert not [ln for ln in out.splitlines() if ln.startswith("    ") and ln.strip() and "</code>" not in ln]


def test_only_the_shared_indentation_goes_so_a_nested_list_keeps_its_shape():
    src = "<details>\n  <summary>Reports</summary>\n  - one\n    - nested\n  ```\n  kept as is\n  ```\n</details>\n"
    out = M._unfold_details(src)
    assert "\n- one\n  - nested\n" in out
    assert "\n  kept as is\n" in out
