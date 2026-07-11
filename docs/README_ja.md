<div align="center">

<p><sub><strong>オープンソース LLM 学習ワークショップ</strong></sub></p>

<h1>Jackrong LLM Fine-Tuning Guide</h1>

<p><strong>学ぶ → 蒸留 → ファインチューニング → アラインメント → デプロイ</strong></p>

<p>
  生データを再現可能なトレーニングワークフローへ変え、<br>
  ローカルで実行できるモデルとして届けるための実践的な知識ベースです。
</p>

<p>
  <a href="../train_code/"><strong>トレーニングを始める</strong></a>
  ·
  <a href="../High-fidelity%20Dataset/"><strong>データセットを探す</strong></a>
  ·
  <a href="../qwen-mtp-gguf/"><strong>GGUF としてデプロイ</strong></a>
  ·
  <a href="../showcase/"><strong>デザインショーケースを見る</strong></a>
</p>

<p>
  <code>SFT</code>&nbsp;&nbsp;
  <code>GRPO</code>&nbsp;&nbsp;
  <code>GSPO</code>&nbsp;&nbsp;
  <code>LoRA / QLoRA</code>&nbsp;&nbsp;
  <code>MTP → GGUF</code>
</p>

<p>
  <sub>
    <a href="../README.md">English</a> ·
    <a href="../docs/README_zh.md">中文</a> ·
    <a href="../docs/README_ko.md">한국어</a> · 日本語
  </sub>
</p>

</div>

---

<table>
<tr>
<td align="center" width="25%"><strong>24</strong><br><sub>厳選データセット</sub></td>
<td align="center" width="25%"><strong>5</strong><br><sub>実行可能なレシピ</sub></td>
<td align="center" width="25%"><strong>3</strong><br><sub>トレーニング手法</sub></td>
<td align="center" width="25%"><strong>4</strong><br><sub>対応言語</sub></td>
</tr>
</table>

## 目的から選ぶ

<table>
<tr>
<td width="50%" valign="top">
  <sub><strong>01 / 学ぶ</strong></sub>
  <h3>ブラウザでファインチューニング</h3>
  <p>ローカル GPU 環境を先に構築しなくても、Colab または Kaggle のガイド付きレシピを実行できます。</p>
  <p><a href="../train_code/"><strong>トレーニングレシピを見る →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>02 / データを作る</strong></sub>
  <h3>より良いデータセットを蒸留</h3>
  <p>推論、コード、STEM、会話、専門領域のデータを、後続のトレーニングに適した形へ整えます。</p>
  <p><a href="../data_processing_code/"><strong>データ処理レシピを見る →</strong></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <sub><strong>03 / アラインする</strong></sub>
  <h3>SFT、GRPO、GSPO を実践</h3>
  <p>コードを確認しながら、教師ありファインチューニングから強化学習ワークフローへ進めます。</p>
  <p><a href="../train_code/README.md"><strong>トレーニング手法を比較する →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>04 / デプロイする</strong></sub>
  <h3>MTP 対応 GGUF をデプロイ</h3>
  <p>Qwen ファミリーのモデルを検証、変換、スモークテスト、量子化し、ローカル推論向けに公開します。</p>
  <p><a href="../qwen-mtp-gguf/"><strong>MTP GGUF Skill を開く →</strong></a></p>
</td>
</tr>
</table>

## ひとつの学習ループを、最初から最後まで

<p align="center">
  <strong>01 · 選定</strong>
  &nbsp;→&nbsp;
  <strong>02 · 蒸留</strong>
  &nbsp;→&nbsp;
  <strong>03 · 学習</strong>
  &nbsp;→&nbsp;
  <strong>04 · アライン</strong>
  &nbsp;→&nbsp;
  <strong>05 · デプロイ</strong>
</p>

| ステージ | ここでできること | 入口 |
|---|---|---|
| 選定 | 高品質な推論、コード、会話、専門領域データを選ぶ | [データセットカタログ](../High-fidelity%20Dataset/) |
| 蒸留 | 教師モデルのワークフローでトレーニングデータを生成・変換する | [データ処理](../data_processing_code/) |
| 学習 | Colab、Kaggle、Python で LoRA / QLoRA による教師ありファインチューニングを実行する | [トレーニングラボ](../train_code/) |
| アライン | 公開済みの GRPO / GSPO 強化学習レシピを試す | [RL レシピ](../train_code/README.md#-reinforcement-learning-grpo--gspo) |
| デプロイ | Adapter の保存、16-bit チェックポイントのマージ、MTP 対応 GGUF の構築を行う | [デプロイ Skill](../qwen-mtp-gguf/) |

## トレーニングラボ

公開済みの 5 つのレシピで、ブラウザから始める学習、教師ありファインチューニング、強化学習を実践できます。

| モデル | 手法 · 環境 | 実行 |
|---|---|---|
| **Qwopus3.5 27B** | `SFT` · Google Colab | [Notebook を起動](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus3-5-27b-Colab.ipynb) |
| **Qwopus3.6 27B** | `GSPO` · Python | [チュートリアルを読む](../train_code/Qwopus3.6-27B-GSPO/) |
| **Qwen3.5 Neo 9B** | `SFT` · Kaggle | [Notebook を開く](../train_code/Qwen3.5-9B-Neo-Kaggle.ipynb) |
| **Qwopus3.5 35B-A3B** | `SFT` · Kaggle | [Notebook を開く](../train_code/Qwopus-3.5-35B-A3B-Kaggle.ipynb) |
| **Llama3.2-R1 3B** | `GRPO` · Kaggle | [Notebook を開く](../train_code/Llama-3.2-3B-R1-Zero-GRPO.ipynb) |

**[トレーニングカタログをすべて見る →](../train_code/README.md)**

## MTP GGUF：チェックポイントからローカルランタイムまで

> [!TIP]
> [`qwen-mtp-gguf`](../qwen-mtp-gguf/) サブプロジェクトは、単なる変換コマンドではなく、エージェント対応のリリースワークフローです。モデルの互換性とマシンリソースを確認し、MTP / nextn テンソルを検証または注入し、llama.cpp で変換します。さらに HF / GGUF スモークテスト、量子化マトリクスの構築、安全なアップロードと再開操作までを支援します。

<p>
  <a href="../qwen-mtp-gguf/"><strong>Skill を開く</strong></a>
  ·
  <a href="../qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Pipeline-Guide.md">Pipeline Guide を読む</a>
  ·
  <a href="../qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Agent-Usage.md">エージェントと使う</a>
</p>

## リソースライブラリ

<table>
<tr>
<td width="50%" valign="top">
  <sub><strong>データ</strong></sub>
  <h3>高品質データセットカタログ</h3>
  <p>推論、数学、コード、指示追従、会話、専門領域に対応する 24 個の厳選コレクションです。</p>
  <p><a href="../High-fidelity%20Dataset/"><strong>カタログを見る →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>ガイド</strong></sub>
  <h3>長編学習ライブラリ</h3>
  <p>概念と完全なトレーニングワークフローを結び付ける、初心者向けガイドと技術レポートです。</p>
  <p><a href="../guidePDF/"><strong>ガイドを読む →</strong></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <sub><strong>自動化</strong></sub>
  <h3>Codex Goal テンプレート</h3>
  <p>RL トレーニング、MTP GGUF リリース、反復可能なリポジトリ保守のための編集可能な計画です。</p>
  <p><a href="../codex-goals/"><strong>Goal テンプレートを使う →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>ドキュメント</strong></sub>
  <h3>多言語ナレッジベース</h3>
  <p>英語、中国語、韓国語、日本語の入口に加え、プロジェクト理念と保守ノートを収録しています。</p>
  <p><a href="../docs/"><strong>ドキュメントを開く →</strong></a></p>
</td>
</tr>
</table>

## このワークショップで扱う内容

| 領域 | 公開済みワークフロー |
|---|---|
| ファインチューニング | LoRA / QLoRA SFT、ブラウザ Notebook、Python チュートリアル |
| 強化学習 | 報酬とトレーニングコードを確認できる GRPO / GSPO レシピ |
| データ | 蒸留、前処理、データセット選定、一括ダウンロード用ヘルパー |
| エクスポート | LoRA Adapter、マージ済み 16-bit チェックポイント、GGUF 変換・量子化 |
| エージェントツール | 再利用可能な MTP リリース Skill と編集可能な Codex Goal テンプレート |

<details>
<summary><strong>モデル対応ロードマップ</strong></summary>

<br>

公開済みの RL レシピでは、モデルとトレーニング目的に応じて GRPO または GSPO を使用します。

| モデルファミリー | SFT 対応 | RL 対応 |
|---|---:|---:|
| Qwen 3.5 | 公開済み | 予定 |
| Qwen 3.6 | 公開済み | 公開済み |
| Qwen 3 | 予定 | 予定 |
| Llama3.2-R1 3B | 収録済み | 公開済み |
| Llama 3.1 / 3.3 | 予定 | 予定 |

</details>

## オープンソースを前提とした設計

> トレーニングの知識は、学習者が再現し、判断の背景を確認し、自分のモデルやデータに合わせてワークフローを変更できるときに、最も役立ちます。

公開済みのファインチューニングモデルのソースコードとドキュメントは、可能な限り利用できる状態を保ちます。詳しくは [プロジェクト理念](../docs/PROJECT_PHILOSOPHY.md) と [リポジトリ保守ガイド](../docs/MAINTAINING_THE_KNOWLEDGE_BASE.md) をご覧ください。

<details>
<summary><strong>このプロジェクトを引用する</strong></summary>

```bibtex
@misc{jackrong-llm-finetuning,
  author = {Jackrong},
  title = {Jackrong LLM Fine-Tuning Guide: An Educational LLM Fine-Tuning Knowledge Base},
  year = {2026},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://github.com/R6410418/Jackrong-llm-finetuning-guide}}
}
```

</details>

---

<div align="center">

<p>
  Built with
  <a href="https://github.com/unslothai/unsloth">Unsloth</a> ·
  <a href="https://pytorch.org/">PyTorch</a> ·
  <a href="https://huggingface.co/Jackrong">Hugging Face</a> ·
  <a href="https://colab.research.google.com/">Google Colab</a> ·
  <a href="https://kaggle.com/">Kaggle</a>
</p>

<p><sub>オープンモデルを作る人々のための、オープンな知識。</sub></p>

</div>
