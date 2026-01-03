from langchain_core.prompts import ChatPromptTemplate
from common import llm
import json

DIALOG_PROMPT = ChatPromptTemplate.from_template("""
現在の記事構造は以下のJSONです。
ユーザーの編集指示を反映してJSONだけを更新してください。

JSON:
{json}

編集指示:
{instruction}

更新後JSONのみ返してください。
""")


def edit_json(structured_json, instruction):
    print("=== 修正中 ===")
    res = llm.invoke(DIALOG_PROMPT.format(
        json=json.dumps(structured_json, ensure_ascii=False),
        instruction=instruction
    ))
    print("=== 修正完了 ===")
    return json.loads(res.content)
