from langchain_core.prompts import ChatPromptTemplate
from common import llm

STRUCT_PROMPT = ChatPromptTemplate.from_template("""
あなたは優秀な編集者です。
以下は雑誌原稿の生テキスト(PDFから抽出したもの)ですが、ルビなどがバラバラに含まれています。
見出し・本文・ルビ候補を推定し、次のJSON構造で返してください。

{{
 "title": "",
 "sections": [
   {{
     "heading": "",
     "paragraphs": [
        {{
          "text": "",
          "ruby": [{{"base":"","ruby":""}}]
        }}
     ]
   }}
 ]
}}

注意点:
  - 原稿の文字列に含まれない文字は追加しないでください。
  - 原稿にPAGE番号や図などが含まれてしまっている可能性がありますが、無視してください。

原稿:
{text}
""")


def structure_text(raw_text: str):
    print("=== 文章構造化中 ===")
    res = llm.invoke(STRUCT_PROMPT.format(text=raw_text))
    print("=== 文章構造化完了 ===")
    return res.content
