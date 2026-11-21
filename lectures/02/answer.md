# 第2回 解答

## 演習

- 使ったモデル・設定（`result.json` の `config` から）：Qwen/Qwen3.5-0.8B
- 自分で学習を実行したか（`executed_training_myself`）：はい 
- 学習前：`format_rate` =　0.09523809523809523 / `content_rate` = 1.0
- 学習後：`format_rate` =　0.0 / `content_rate` =　0.9523809523809523
- 退行した質問：なし
- 学習後に残った失敗と、その型（根拠なしの質問に断定した / 根拠ありの質問に確認要求で逃げた / 形式の崩れ）：「オフィスアワーは事前予約が必要ですか」について、根拠なしの質問に断定した。
- 知識を問う質問（セクション 6）の結果（学習前の分類 → 学習後の分類）と気づいたこと：学習前はformat-errorだったものが学習後はformat-errorが解消された。
- 学習で変わったこと・変わらなかったこと：フォーマットエラーはほとんどの確率で解消された。

## 宿題

- 取り組んだレベル：基礎 
- 変えた設定やデータ：num_train_epochsを20→40
- 結果（比較表や数字）：result.json（変更前）
{
  "config": {
    "base_model": "Qwen/Qwen3.5-0.8B",
    "revision": "2fc06364715b967f1860aea9cf38778875588b17",
    "seed": 42,
    "num_train_epochs": 20,
    "warmup_steps": 6,
    "lr": 0.0002,
    "lora_r": 16,
    "lora_alpha": 32,
    "max_seq_len": 512,
    "max_new_tokens": 96,
    "gen": {
      "do_sample": false
    }
  },
  "versions": {
    "transformers": "5.18.0",
    "peft": "0.21.1",
    "trl": "1.14.2",
    "torch": "2.11.0+cu130"
  },
  "method": "LoRA（量子化なし）",
  "before": {
    "label": "before",
    "n": 21,
    "format_rate": 0.09523809523809523,
    "content_rate": 0.0,
    "both_rate": 0.0,
    "seconds": 23.4
  },
  "after": {
    "label": "after",
    "n": 21,
    "format_rate": 1.0,
    "content_rate": 0.9523809523809523,
    "both_rate": 0.9523809523809523,
    "seconds": 67.6
  },
  "regressed": [],
  "executed_training_myself": true
}

result.json（変更後）
{
  "config": {
    "base_model": "Qwen/Qwen3.5-0.8B",
    "revision": "2fc06364715b967f1860aea9cf38778875588b17",
    "seed": 42,
    "num_train_epochs": 40,
    "warmup_steps": 6,
    "lr": 0.0002,
    "lora_r": 16,
    "lora_alpha": 32,
    "max_seq_len": 512,
    "max_new_tokens": 96,
    "gen": {
      "do_sample": false
    }
  },
  "versions": {
    "transformers": "5.18.0",
    "peft": "0.21.1",
    "trl": "1.14.2",
    "torch": "2.11.0+cu130"
  },
  "method": "LoRA（量子化なし）",
  "before": {
    "label": "before",
    "n": 21,
    "format_rate": 0.09523809523809523,
    "content_rate": 0.0,
    "both_rate": 0.0,
    "seconds": 37.2
  },
  "after": {
    "label": "after",
    "n": 21,
    "format_rate": 1.0,
    "content_rate": 0.8571428571428571,
    "both_rate": 0.8571428571428571,
    "seconds": 44.4
  },
  "regressed": [],
  "executed_training_myself": true
}

- ファインチューニングが向く場面・向かない場面についての考察：向く場面は日本語や専門分野などの学習の
量が少ない場合。向かない場面は最新の情報を取り込みたい場合。
