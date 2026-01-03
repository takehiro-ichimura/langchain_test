# chains/diff_chain.py
import difflib


def diff(old_html, new_html):
    return "\n".join(difflib.unified_diff(
        old_html.splitlines(),
        new_html.splitlines(),
        lineterm=""
    ))
