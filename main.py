from chains.pdf_chain import load_pdf_range
from chains.structure_chain import structure_text
from chains.html_chain import json_to_html
from chains.dialog_chain import edit_json
from chains.diff_chain import diff
from ui.ask import ask_page_range

start, end = ask_page_range()
raw = load_pdf_range("input/sample.pdf", start, end)
structured = structure_text(raw)
html = json_to_html(structured)

print("=== 初期HTML ===")
print(html)

while True:
    inst = input("編集指示 > ")
    structured = edit_json(structured, inst)
    new_html = json_to_html(structured)
    print(diff(html, new_html))
    html = new_html
