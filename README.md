<div align="center">

<p><sub><strong>OPEN-SOURCE LLM LEARNING WORKSHOP</strong></sub></p>

<h1>Jackrong LLM Fine-Tuning Guide</h1>

<p><strong>Learn → Distill → Fine-tune → Align → Ship</strong></p>

<p>
  A hands-on knowledge base for turning raw data into reproducible training workflows<br>
  and runnable local models.
</p>

<p>
  <a href="train_code/"><strong>Start training</strong></a>
  ·
  <a href="High-fidelity%20Dataset/"><strong>Explore datasets</strong></a>
  ·
  <a href="qwen-mtp-gguf/"><strong>Ship with GGUF</strong></a>
  ·
  <a href="showcase/"><strong>View the design showcase</strong></a>
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
    English · <a href="docs/README_zh.md">中文</a> ·
    <a href="docs/README_ko.md">한국어</a> ·
    <a href="docs/README_ja.md">日本語</a>
  </sub>
</p>

</div>

---

<table>
<tr>
<td align="center" width="25%"><strong>24</strong><br><sub>CURATED DATASETS</sub></td>
<td align="center" width="25%"><strong>5</strong><br><sub>RUNNABLE RECIPES</sub></td>
<td align="center" width="25%"><strong>3</strong><br><sub>TRAINING METHODS</sub></td>
<td align="center" width="25%"><strong>4</strong><br><sub>LANGUAGES</sub></td>
</tr>
</table>

## Choose your path

<table>
<tr>
<td width="50%" valign="top">
  <sub><strong>01 / LEARN</strong></sub>
  <h3>Fine-tune in your browser</h3>
  <p>Run guided Colab or Kaggle recipes without building a local GPU environment first.</p>
  <p><a href="train_code/"><strong>Browse training recipes →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>02 / BUILD DATA</strong></sub>
  <h3>Distill a better dataset</h3>
  <p>Prepare reasoning, coding, STEM, conversation, and domain data for downstream training.</p>
  <p><a href="data_processing_code/"><strong>Explore data recipes →</strong></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <sub><strong>03 / ALIGN</strong></sub>
  <h3>Practice SFT, GRPO, and GSPO</h3>
  <p>Move from supervised fine-tuning to reinforcement-learning workflows with inspectable code.</p>
  <p><a href="train_code/README.md"><strong>Compare training methods →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>04 / SHIP</strong></sub>
  <h3>Deploy an MTP-enabled GGUF</h3>
  <p>Validate, convert, smoke-test, quantize, and release Qwen-family models for local inference.</p>
  <p><a href="qwen-mtp-gguf/"><strong>Open the MTP GGUF skill →</strong></a></p>
</td>
</tr>
</table>

## One learning loop, end to end

<p align="center">
  <strong>01 · CURATE</strong>
  &nbsp;→&nbsp;
  <strong>02 · DISTILL</strong>
  &nbsp;→&nbsp;
  <strong>03 · TRAIN</strong>
  &nbsp;→&nbsp;
  <strong>04 · ALIGN</strong>
  &nbsp;→&nbsp;
  <strong>05 · SHIP</strong>
</p>

| Stage | What you can do here | Entry point |
|---|---|---|
| Curate | Select high-fidelity reasoning, coding, conversation, and domain data | [Dataset catalog](High-fidelity%20Dataset/) |
| Distill | Generate or transform training data with a teacher-model workflow | [Data processing](data_processing_code/) |
| Train | Run LoRA / QLoRA supervised fine-tuning in Colab, Kaggle, or Python | [Training lab](train_code/) |
| Align | Explore released GRPO and GSPO reinforcement-learning recipes | [RL recipes](train_code/README.md#-reinforcement-learning-grpo--gspo) |
| Ship | Export adapters, merge 16-bit checkpoints, and build MTP-enabled GGUF releases | [Deployment skill](qwen-mtp-gguf/) |

## Training lab

Five released recipes cover browser-first learning, supervised fine-tuning, and reinforcement learning.

| Model | Method · environment | Run |
|---|---|---|
| **Qwopus3.5 27B** | `SFT` · Google Colab | [Launch notebook](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus3-5-27b-Colab.ipynb) |
| **Qwopus3.6 27B** | `GSPO` · Python | [Read the tutorial](train_code/Qwopus3.6-27B-GSPO/) |
| **Qwen3.5 Neo 9B** | `SFT` · Kaggle | [Open notebook](train_code/Qwen3.5-9B-Neo-Kaggle.ipynb) |
| **Qwopus3.5 35B-A3B** | `SFT` · Kaggle | [Open notebook](train_code/Qwopus-3.5-35B-A3B-Kaggle.ipynb) |
| **Llama3.2-R1 3B** | `GRPO` · Kaggle | [Open notebook](train_code/Llama-3.2-3B-R1-Zero-GRPO.ipynb) |

**[Browse the complete training catalog →](train_code/README.md)**

## MTP GGUF, from checkpoint to local runtime

> [!TIP]
> The [`qwen-mtp-gguf`](qwen-mtp-gguf/) subproject is an agent-ready release workflow—not just a conversion command. It checks model compatibility and machine resources, validates or injects MTP / nextn tensors, converts with llama.cpp, runs HF and GGUF smoke tests, builds a quantization matrix, and supports safer upload and resume operations.

<p>
  <a href="qwen-mtp-gguf/"><strong>Open the skill</strong></a>
  ·
  <a href="qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Pipeline-Guide.md">Read the pipeline guide</a>
  ·
  <a href="qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Agent-Usage.md">Use it with an agent</a>
</p>

## Resource library

<table>
<tr>
<td width="50%" valign="top">
  <sub><strong>DATA</strong></sub>
  <h3>High-fidelity dataset catalog</h3>
  <p>Twenty-four curated collections for reasoning, mathematics, code, instruction following, conversation, and domain work.</p>
  <p><a href="High-fidelity%20Dataset/"><strong>Explore the catalog →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>GUIDES</strong></sub>
  <h3>Long-form learning library</h3>
  <p>Beginner walkthroughs and technical reports that connect concepts to complete training workflows.</p>
  <p><a href="guidePDF/"><strong>Read the guides →</strong></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <sub><strong>AUTOMATION</strong></sub>
  <h3>Codex goal templates</h3>
  <p>Editable plans for RL training, MTP GGUF releases, and repeatable repository maintenance.</p>
  <p><a href="codex-goals/"><strong>Use a goal template →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>DOCUMENTATION</strong></sub>
  <h3>Multilingual knowledge base</h3>
  <p>English, Chinese, Korean, and Japanese entry points, plus project philosophy and maintenance notes.</p>
  <p><a href="docs/"><strong>Open the documentation →</strong></a></p>
</td>
</tr>
</table>

## What the workshop covers

| Area | Released workflows |
|---|---|
| Fine-tuning | LoRA / QLoRA SFT, browser notebooks, Python tutorials |
| Reinforcement learning | GRPO and GSPO recipes with inspectable reward and training code |
| Data | Distillation, preprocessing, dataset selection, and batch download helpers |
| Export | LoRA adapters, merged 16-bit checkpoints, GGUF conversion and quantization |
| Agent tooling | Reusable MTP release skill and editable Codex goal templates |

<details>
<summary><strong>Model support roadmap</strong></summary>

<br>

Released RL recipes may use GRPO or GSPO depending on the model and training objective.

| Model family | SFT support | RL support |
|---|---:|---:|
| Qwen 3.5 | Released | Scheduled |
| Qwen 3.6 | Released | Released |
| Qwen 3 | Scheduled | Scheduled |
| Llama3.2-R1 3B | Included | Released |
| Llama 3.1 / 3.3 | Scheduled | Scheduled |

</details>

## Open source, by design

> Training knowledge is most useful when learners can reproduce it, inspect the decisions, and adapt the workflow to their own models and data.

The source code and documentation for released fine-tuned models stay available whenever possible. Read the longer [project philosophy](docs/PROJECT_PHILOSOPHY.md) and the repository [maintenance guide](docs/MAINTAINING_THE_KNOWLEDGE_BASE.md).

<details>
<summary><strong>Cite this project</strong></summary>

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

<p><sub>Open knowledge for people building open models.</sub></p>

</div>
