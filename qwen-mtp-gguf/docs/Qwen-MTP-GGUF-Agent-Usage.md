# Agent Usage Guide

## Universal User Prompt

```text
Use the Qwen MTP GGUF workflow.
Target model: <target repo or local path>
MTP source model: <matching official/base Qwen repo>
Output: <HF repo or local-only>
Quant formats: <default full matrix or selected list>
Please first check my environment, estimate disk/RAM requirements, and stop if it is not feasible. If feasible, merge MTP heads, run a local smoke test, then quantize and upload using the safest strategy.
```

## Agent Decision Tree

1. If tools are missing, run `bootstrap_qwen_mtp_env.sh` after user approval.
2. If target/source model IDs are unclear, ask for exact repos.
3. If upload strategy is unclear, recommend `stream` for large models.
4. If preflight fails, do not download full weights.
5. If MTP source config mismatches target config, stop.
6. If F16 smoke test fails, do not upload quantized files.
7. If upload fails, keep local files and rerun the same command later.

## Claude Code / OpenCode / Qwen Code

These agents can use the scripts directly:

```bash
python3 scripts/qwen_mtp_gguf_pipeline.py --preflight-only ...
python3 scripts/qwen_mtp_gguf_pipeline.py --smoke-test-before-upload ...
```

They do not need Codex-specific skill metadata. Copy `scripts/` and `references/` into the repository and point the agent to this guide.

## Codex

Install this as a Codex skill under:

```text
~/.codex/skills/qwen-mtp-gguf
```

Then invoke:

```text
Use $qwen-mtp-gguf to convert <target model> with MTP heads from <base model>, preflight my machine first, then smoke-test and quantize.
```

## Hermes-Style Tool Agents

Expose three commands as tools:

- `bootstrap_qwen_mtp_env.sh`
- `qwen_mtp_gguf_pipeline.py --preflight-only`
- `qwen_mtp_gguf_pipeline.py`

The planner should call preflight as a feasibility tool and only call the full pipeline when the report passes.

## Public Release Notes

When publishing this skill on GitHub or Hugging Face:

- Keep examples generic.
- Use placeholders for model IDs.
- Include official references for llama.cpp and Hugging Face APIs.
- Do not include private server paths, HF token file paths, personal repo names, or upload logs.
