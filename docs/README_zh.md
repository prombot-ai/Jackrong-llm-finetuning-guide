<div align="center">

<p><sub><strong>开源 LLM 学习工坊</strong></sub></p>

<h1>Jackrong LLM Fine-Tuning Guide</h1>

<p><strong>学习 → 蒸馏 → 微调 → 对齐 → 发布</strong></p>

<p>
  一个把原始数据转化为可复现训练工作流<br>
  与本地可运行模型的实践型知识库。
</p>

<p>
  <a href="../train_code/"><strong>开始训练</strong></a>
  ·
  <a href="../High-fidelity%20Dataset/"><strong>探索数据集</strong></a>
  ·
  <a href="../qwen-mtp-gguf/"><strong>使用 GGUF 发布</strong></a>
  ·
  <a href="../showcase/"><strong>查看页面设计</strong></a>
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
    <a href="../README.md">English</a> · 中文 ·
    <a href="../docs/README_ko.md">한국어</a> ·
    <a href="../docs/README_ja.md">日本語</a>
  </sub>
</p>

</div>

---

<table>
<tr>
<td align="center" width="25%"><strong>24</strong><br><sub>精选数据集</sub></td>
<td align="center" width="25%"><strong>5</strong><br><sub>可运行配方</sub></td>
<td align="center" width="25%"><strong>3</strong><br><sub>训练方法</sub></td>
<td align="center" width="25%"><strong>4</strong><br><sub>支持语言</sub></td>
</tr>
</table>

## 选择你的路径

<table>
<tr>
<td width="50%" valign="top">
  <sub><strong>01 / 学习</strong></sub>
  <h3>在浏览器中微调模型</h3>
  <p>无需先搭建本地 GPU 环境，即可运行带完整引导的 Colab 或 Kaggle 配方。</p>
  <p><a href="../train_code/"><strong>浏览训练配方 →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>02 / 构建数据</strong></sub>
  <h3>蒸馏更好的数据集</h3>
  <p>为后续训练准备推理、代码、STEM、对话和领域数据。</p>
  <p><a href="../data_processing_code/"><strong>探索数据配方 →</strong></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <sub><strong>03 / 对齐</strong></sub>
  <h3>实践 SFT、GRPO 和 GSPO</h3>
  <p>通过可审阅的代码，从监督微调逐步进阶到强化学习工作流。</p>
  <p><a href="../train_code/README.md"><strong>比较训练方法 →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>04 / 发布</strong></sub>
  <h3>部署支持 MTP 的 GGUF</h3>
  <p>验证、转换、冒烟测试、量化并发布 Qwen 家族模型，用于本地推理。</p>
  <p><a href="../qwen-mtp-gguf/"><strong>打开 MTP GGUF Skill →</strong></a></p>
</td>
</tr>
</table>

## 一条贯穿始终的学习闭环

<p align="center">
  <strong>01 · 精选</strong>
  &nbsp;→&nbsp;
  <strong>02 · 蒸馏</strong>
  &nbsp;→&nbsp;
  <strong>03 · 训练</strong>
  &nbsp;→&nbsp;
  <strong>04 · 对齐</strong>
  &nbsp;→&nbsp;
  <strong>05 · 发布</strong>
</p>

| 阶段 | 你可以在这里完成 | 入口 |
|---|---|---|
| 精选 | 选择高保真推理、代码、对话和领域数据 | [数据集目录](../High-fidelity%20Dataset/) |
| 蒸馏 | 借助教师模型工作流生成或转换训练数据 | [数据处理](../data_processing_code/) |
| 训练 | 在 Colab、Kaggle 或 Python 中运行 LoRA / QLoRA 监督微调 | [训练实验室](../train_code/) |
| 对齐 | 探索已发布的 GRPO 和 GSPO 强化学习配方 | [RL 配方](../train_code/README.md#-reinforcement-learning-grpo--gspo) |
| 发布 | 导出 adapter、合并 16-bit 检查点，并构建支持 MTP 的 GGUF 版本 | [部署 Skill](../qwen-mtp-gguf/) |

## 训练实验室

五个已发布配方覆盖浏览器入门、监督微调和强化学习。

| 模型 | 方法 · 环境 | 运行 |
|---|---|---|
| **Qwopus3.5 27B** | `SFT` · Google Colab | [启动 Notebook](https://colab.research.google.com/github/R6410418/Jackrong-llm-finetuning-guide/blob/main/train_code/Qwopus3-5-27b-Colab.ipynb) |
| **Qwopus3.6 27B** | `GSPO` · Python | [阅读教程](../train_code/Qwopus3.6-27B-GSPO/) |
| **Qwen3.5 Neo 9B** | `SFT` · Kaggle | [打开 Notebook](../train_code/Qwen3.5-9B-Neo-Kaggle.ipynb) |
| **Qwopus3.5 35B-A3B** | `SFT` · Kaggle | [打开 Notebook](../train_code/Qwopus-3.5-35B-A3B-Kaggle.ipynb) |
| **Llama3.2-R1 3B** | `GRPO` · Kaggle | [打开 Notebook](../train_code/Llama-3.2-3B-R1-Zero-GRPO.ipynb) |

**[浏览完整训练目录 →](../train_code/README.md)**

## 从检查点到本地运行时的 MTP GGUF

> [!TIP]
> [`qwen-mtp-gguf`](../qwen-mtp-gguf/) 子项目不仅是一条转换命令，而是一套可由 agent 执行的发布工作流。它会检查模型兼容性与机器资源，验证或注入 MTP / nextn 张量，使用 llama.cpp 转换，运行 HF 与 GGUF 冒烟测试，构建量化矩阵，并支持更安全的上传与断点续传。

<p>
  <a href="../qwen-mtp-gguf/"><strong>打开 Skill</strong></a>
  ·
  <a href="../qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Pipeline-Guide.md">阅读流程指南</a>
  ·
  <a href="../qwen-mtp-gguf/docs/Qwen-MTP-GGUF-Agent-Usage.md">与 agent 配合使用</a>
</p>

## 资源库

<table>
<tr>
<td width="50%" valign="top">
  <sub><strong>数据</strong></sub>
  <h3>高保真数据集目录</h3>
  <p>24 个精选集合，覆盖推理、数学、代码、指令跟随、对话与领域任务。</p>
  <p><a href="../High-fidelity%20Dataset/"><strong>探索数据集目录 →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>指南</strong></sub>
  <h3>长篇学习资料库</h3>
  <p>用面向初学者的完整指南和技术报告，把核心概念连接到端到端训练工作流。</p>
  <p><a href="../guidePDF/"><strong>阅读指南 →</strong></a></p>
</td>
</tr>
<tr>
<td width="50%" valign="top">
  <sub><strong>自动化</strong></sub>
  <h3>Codex Goal 模板</h3>
  <p>用于 RL 训练、MTP GGUF 发布和可复用仓库维护的可编辑计划。</p>
  <p><a href="../codex-goals/"><strong>使用 Goal 模板 →</strong></a></p>
</td>
<td width="50%" valign="top">
  <sub><strong>文档</strong></sub>
  <h3>多语言知识库</h3>
  <p>提供英文、中文、韩文和日文入口，以及项目理念与维护说明。</p>
  <p><a href="../docs/"><strong>打开文档 →</strong></a></p>
</td>
</tr>
</table>

## 工坊覆盖的能力

| 领域 | 已发布工作流 |
|---|---|
| 微调 | LoRA / QLoRA SFT、浏览器 Notebook、Python 教程 |
| 强化学习 | 带有可审阅奖励函数和训练代码的 GRPO 与 GSPO 配方 |
| 数据 | 蒸馏、预处理、数据集选择与批量下载工具 |
| 导出 | LoRA adapter、合并后的 16-bit 检查点、GGUF 转换与量化 |
| Agent 工具 | 可复用的 MTP 发布 Skill 与可编辑 Codex Goal 模板 |

<details>
<summary><strong>模型支持路线图</strong></summary>

<br>

已发布的 RL 配方会根据模型和训练目标使用 GRPO 或 GSPO。

| 模型家族 | SFT 支持 | RL 支持 |
|---|---:|---:|
| Qwen 3.5 | 已发布 | 计划中 |
| Qwen 3.6 | 已发布 | 已发布 |
| Qwen 3 | 计划中 | 计划中 |
| Llama3.2-R1 3B | 已包含 | 已发布 |
| Llama 3.1 / 3.3 | 计划中 | 计划中 |

</details>

## 从设计开始就是开源

> 当学习者能够复现训练过程、审阅关键决策，并根据自己的模型和数据调整工作流时，训练知识才最有价值。

已发布微调模型的源代码与文档会尽可能保持开放。你还可以阅读更完整的[项目理念](../docs/PROJECT_PHILOSOPHY.md)和仓库[维护指南](../docs/MAINTAINING_THE_KNOWLEDGE_BASE.md)。

<details>
<summary><strong>引用本项目</strong></summary>

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
  基于
  <a href="https://github.com/unslothai/unsloth">Unsloth</a> ·
  <a href="https://pytorch.org/">PyTorch</a> ·
  <a href="https://huggingface.co/Jackrong">Hugging Face</a> ·
  <a href="https://colab.research.google.com/">Google Colab</a> ·
  <a href="https://kaggle.com/">Kaggle</a>
</p>

<p><sub>为开放模型建设者提供开放知识。</sub></p>

</div>
