<div style="border:1px solid #cbd5e1;border-radius:16px;box-shadow:0 10px 15px -3px rgba(0,0,0,0.05);overflow:hidden;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,sans-serif;">
  <div style="background:linear-gradient(135deg,#1e3a8a 0%,#0284c7 100%);padding:28px 32px;color:white;">
    <div style="font-size:13px;font-weight:700;letter-spacing:0;text-transform:uppercase;opacity:.9;">Open Agent Workflow</div>
    <h1 style="margin:8px 0 10px;font-size:34px;line-height:1.15;">Qwen MTP GGUF Skill</h1>
    <p style="margin:0;font-size:16px;line-height:1.55;max-width:900px;">A complete workflow for extracting Qwen-family MTP/nextn heads, merging them into compatible fine-tuned models, converting to GGUF, smoke-testing locally, and releasing quantized artifacts safely.</p>
    <div style="margin-top:16px;display:flex;gap:8px;flex-wrap:wrap;">
      <span style="background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.28);border-radius:999px;padding:6px 10px;font-size:13px;">Preflight sizing</span>
      <span style="background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.28);border-radius:999px;padding:6px 10px;font-size:13px;">MTP extraction</span>
      <span style="background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.28);border-radius:999px;padding:6px 10px;font-size:13px;">llama.cpp GGUF</span>
      <span style="background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.28);border-radius:999px;padding:6px 10px;font-size:13px;">Agent-ready</span>
    </div>
  </div>

  <div style="padding:28px 32px;background:#ffffff;color:#334155;">
    <h2 style="font-size:20px;margin:0 0 12px;color:#1e3a8a;">What This Skill Does</h2>
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:12px;">
      <div style="border:1px solid #e2e8f0;border-radius:8px;padding:14px;background:#f8fafc;"><strong>Plans before download</strong><br/>Reads model metadata, estimates disk/RAM, checks tools, and blocks unsafe runs before large files are pulled.</div>
      <div style="border:1px solid #e2e8f0;border-radius:8px;padding:14px;background:#f8fafc;"><strong>Extracts minimal MTP shards</strong><br/>Uses the source model index to download only shards containing `mtp` or `nextn` tensors.</div>
      <div style="border:1px solid #e2e8f0;border-radius:8px;padding:14px;background:#f8fafc;"><strong>Builds release GGUFs</strong><br/>Converts F16/BF16 with llama.cpp and quantizes into common K/IQ release formats.</div>
      <div style="border:1px solid #e2e8f0;border-radius:8px;padding:14px;background:#f8fafc;"><strong>Validates before upload</strong><br/>Runs GGUF smoke tests with model chat templates when available, resumes uploads, and deletes local files only after confirmed upload.</div>
    </div>
  </div>
</div>

## Quick Start

```bash
bash scripts/bootstrap_qwen_mtp_env.sh --prefix ./qwen-mtp-env --backend cpu
source ./qwen-mtp-env/.venv/bin/activate

python3 scripts/qwen_mtp_gguf_pipeline.py \
  --source-repo owner/target-qwen-finetune \
  --mtp-source-repo owner/matching-base-qwen-with-mtp \
  --output-repo owner/target-qwen-mtp-gguf \
  --work-root ./mtp-gguf-work \
  --llama-cpp ./qwen-mtp-env/llama.cpp \
  --token-env HF_TOKEN \
  --upload-strategy stream \
  --preflight-only
```

If preflight passes:

```bash
python3 scripts/qwen_mtp_gguf_pipeline.py \
  --source-repo owner/target-qwen-finetune \
  --mtp-source-repo owner/matching-base-qwen-with-mtp \
  --output-repo owner/target-qwen-mtp-gguf \
  --work-root ./mtp-gguf-work \
  --llama-cpp ./qwen-mtp-env/llama.cpp \
  --filename-prefix target-qwen-MTP \
  --token-env HF_TOKEN \
  --upload-strategy stream \
  --smoke-test-before-upload \
  --cleanup-after-upload
```

## Supported Agent Pattern

This workflow can be used by Codex, Claude Code, OpenCode, Qwen Code, Hermes-style agents, and other shell-capable coding agents. The agent should:

1. Parse the target model, MTP source model, quant formats, and output preference.
2. Bootstrap missing tools if the user approves.
3. Run `--preflight-only` and summarize blockers.
4. Ask for upload strategy when not specified.
5. Run the full pipeline only after the feasibility check passes.
6. Verify smoke-test logs and output files.

## Default Quant Matrix

```text
q2_k, q3_k_s, q3_k_m, q3_k_l, iq4_xs,
q4_k_s, q4_k_m, q5_k_s, q5_k_m,
q6_k, q8_0, bf16
```

## Safety Defaults

- CPU mode is sufficient for conversion and quantization.
- GPU offload is optional for faster inference tests.
- Stream upload is the safest default for disk-limited machines.
- Config mismatches between target and MTP source are blockers by default.
- Public docs must not include tokens, private paths, private repo names, or raw server logs.

## Core Files

- `SKILL.md`: agent workflow and trigger description.
- `scripts/qwen_mtp_gguf_pipeline.py`: preflight, extraction, merge, conversion, quantization, smoke test, upload.
- `scripts/bootstrap_qwen_mtp_env.sh`: Python and llama.cpp environment bootstrap.
- `scripts/qwen_gguf_smoke_test.py`: CPU GGUF inference smoke test.
- `scripts/qwen_hf_smoke_test.py`: HF model smoke test using `apply_chat_template`.
- `references/environment-and-sizing.md`: sizing rules and source references.
- `references/agent-integration.md`: cross-agent usage guide.

## References

- llama.cpp: https://github.com/ggml-org/llama.cpp
- llama.cpp build guide: https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md
- Hugging Face Hub download metadata: https://huggingface.co/docs/huggingface_hub/en/package_reference/file_download
- Hugging Face Hub API: https://huggingface.co/docs/huggingface_hub/en/package_reference/hf_api
- Transformers chat templates: https://huggingface.co/docs/transformers/main/chat_templating
