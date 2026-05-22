# Agent Integration

## Universal agent workflow

Use this sequence in Codex, Claude Code, OpenCode, Qwen Code, Hermes, or any shell-capable coding agent:

1. Parse the user request into:
   - Target model repo or local path.
   - Matching base/MTP source repo.
   - Output repo or local-only destination.
   - Quant types.
   - Upload strategy.

2. Run environment bootstrap if needed:

```bash
bash scripts/bootstrap_qwen_mtp_env.sh --prefix ./qwen-mtp-env --backend cpu
source ./qwen-mtp-env/.venv/bin/activate
```

3. Run preflight:

```bash
python3 scripts/qwen_mtp_gguf_pipeline.py ... --preflight-only
```

4. Summarize blockers:
   - Disk deficit.
   - RAM warning.
   - Missing llama.cpp tools.
   - Missing token.
   - Target/base config mismatch.

5. Ask the user before:
   - Installing system packages.
   - Continuing with config mismatch.
   - Running with insufficient disk.
   - Choosing `batch` when `stream` is enough.
   - Making a repo public.

6. Run the full pipeline with `--smoke-test-before-upload`.

7. Verify outputs:
   - `preflight_report.md`
   - `pipeline.log`
   - `smoke_*.log`
   - Remote file list when uploading.

## Prompt template for other agents

```text
Use the Qwen MTP GGUF workflow in this repository.
Target model: <target repo or path>
MTP source model: <matching base repo>
Output: <HF repo or local-only>
Quant types: <list or default full matrix>
First bootstrap missing dependencies, then run preflight. Stop and summarize if disk, RAM, llama.cpp, token, or config compatibility checks fail. If preflight passes, inject missing MTP heads, convert to GGUF, run a local Qwen ChatML smoke test, then quantize and upload using the selected strategy.
```

## Agent-specific notes

- Codex: put the reusable workflow in a Codex skill and keep scripts under `scripts/`.
- Claude Code: place this directory inside the project and ask Claude to run the shell commands directly.
- OpenCode and Qwen Code: use the same scripts; do not rely on Codex-specific skill metadata.
- Hermes-style agents: call `preflight-only` as a planning tool, then run the full pipeline as an execution tool.

## Privacy defaults

Public docs should never contain:

- HF tokens or token file paths.
- Private repository names.
- Internal server paths.
- Full upload logs with usernames or machine paths.

Use placeholders in GitHub/HF READMEs and keep private deployment notes in a separate local-only document.
