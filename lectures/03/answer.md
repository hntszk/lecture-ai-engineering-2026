# 第3回 解答

## 演習

- 第1回（素のLLM）とエージェントの回答の違い：
参照先もあるため、より講座の内容に沿った回答を得ることができた。
- `--trace` で見えたツール呼び出し（ツール名と引数）：
[tool call]   search_glossary({'query': 'LoRA'})
[tool call]   search_glossary({'query': 'QLoRA'})
[tool return] search_glossary -> [{"term": "LoRA", "lecture": 2, "definition": "事前学習済みの重みは固定したまま、重みの更新分を2つの小さな行列の積（低ランク行列）で表し、その小さな行列だけを学習するPEFT手法。学習するパラ…
[tool return] search_glossary -> [{"term": "QLoRA", "lecture": 2, "definition": "ベースモデルの重みを4ビットなどに量子化してメモリを節約したうえで、LoRAで学習する手法。より大きなモデルを小さなGPUで扱える。本講座の第2…
[usage] RunUsage(cost=Decimal('0.00370275'), details={'thoughts_tokens': 357, 'text_prompt_tokens': 1527}, input_text_tokens=1527, input_tokens=1527, output_reasoning_tokens=357, output_tokens=682, requests=2, tool_calls=2)
- 1つの質問での LLM 呼び出し回数（`requests`）：
2回
- 追加したツールと、docstring に書いた説明：
"""講座の用語集から用語を検索し、定義と、どの回で扱うかを返す。

    AIエンジニアリングの用語や、この講座（AIE2026）に固有の言葉について
    答える前に使うこと。query には調べたい用語を1つだけ入れる（例: "LoRA"）。
"""

## 宿題

- 取り組んだレベル：発展（b）
- やったこと：Pi で `gemini-flash-lite` を選び、`app/agent.py` の `INSTRUCTIONS` を読んで学習支援の方針を説明するよう依頼した。また、Pi の[システムプロンプト生成コード](https://github.com/earendil-works/pi/blob/main/packages/coding-agent/src/core/system-prompt.ts)と比較した。
- 結果：Pi は「用語集の確認」「講義概要の参照」「関連する回の明記」「宿題はヒントで導く」という方針を整理して回答した。
- 気づき・疑問：Pi は開発全般を支援する一方、講座のエージェントは情報の参照方法や教育的配慮まで指定されている。この違いから、用途に合った指示とツールの設計が重要だと考えた。今回確認できたのは指示の説明であり、講座のエージェントが実際にその方針を守るかは別途検証が必要である。
