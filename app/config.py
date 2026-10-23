"""講座全体で共通の設定。

APIキーやモデル名はコードに書かず、環境変数またはローカルの`.env`から読み込む。
"""

import os

from dotenv import load_dotenv

# ローカルではプロジェクト直下の`.env`を読み込む。
# 既に設定されている環境変数は上書きしないため、Codespaces secretもそのまま使える。
load_dotenv()

# 既定モデル。環境変数 AIE_MODEL を設定すると切り替えられる。
#   例: export AIE_MODEL=gemini-3.5-flash
DEFAULT_MODEL = "gemini-3.5-flash-lite"
MODEL = os.getenv("AIE_MODEL", DEFAULT_MODEL)


def api_error_message(status: int, detail: str = "") -> str:
    """HTTPステータスコードを、受講生向けの日本語の説明にする（ask.py と agent.py で共用）。"""
    if status == 429:
        return "レート制限に達しました。1分ほど待ってから再実行してください。"
    if status == 503:
        return "モデルが混み合っています（503）。少し待ってから再実行してください。"
    if status in (400, 401, 403, 404):
        return f"APIキーかモデル名に問題があります（{status}）: {detail}"
    return f"APIエラー（{status}）: {detail}"


def get_api_key() -> str:
    """GEMINI_API_KEYを返す。環境変数または`.env`に未設定なら終了する。"""
    key = os.getenv("GEMINI_API_KEY")
    if not key:
        raise SystemExit(
            "GEMINI_API_KEY が見つかりません。\n"
            "ローカルではプロジェクト直下に `.env` を作成し、\n"
            "GEMINI_API_KEY=あなたのAPIキー\n"
            "を設定してください。Codespacesでは GitHub secret に登録してください。"
        )
    return key
