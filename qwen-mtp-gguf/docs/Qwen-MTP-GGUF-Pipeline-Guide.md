# Qwen MTP GGUF Pipeline Guide

## Pipeline Overview

```mermaid
flowchart TD
  A["User request: target model + MTP source"] --> B["Environment preflight"]
  B --> C{"Enough disk/RAM and compatible config?"}
  C -- "No" --> D["Stop, summarize blockers, ask user"]
  C -- "Yes" --> E["Download/copy target HF model"]
  E --> F{"Target already has valid MTP/nextn tensors?"}
  F -- "Yes" --> H["Validate index mappings"]
  F -- "No" --> G["Download minimal MTP shards and save mtp_heads.safetensors"]
  G --> H["Inject keys into model.safetensors.index.json"]
  H --> I["Convert temporary F16 GGUF"]
  I --> J["Local Qwen ChatML smoke test"]
  J --> K{"Smoke test passes?"}
  K -- "No" --> L["Stop before upload"]
  K -- "Yes" --> M["Quantize requested GGUF formats"]
  M --> N{"Upload strategy"}
  N -- "stream" --> O["Upload one, delete one"]
  N -- "batch" --> P["Upload all after local build"]
  N -- "local-only" --> Q["Keep local GGUF files"]
```

## Resource Planning

The pipeline estimates peak storage from:

- Target model HF files.
- Minimal MTP source shards.
- Temporary F16 GGUF.
- Requested quantized GGUF outputs.
- Safety margin.

For large models, `stream` is recommended because it keeps only one quantized GGUF live at a time. `batch` is useful when uploads are delayed but requires enough disk for all requested outputs.

## Feasibility Rules

Continue only when:

- llama.cpp converter and quantizer exist.
- Work directory has enough free disk.
- RAM is plausible for conversion/quantization.
- HF token is available for private downloads/uploads.
- Target and MTP source configs match on core architecture fields.
- MTP source index contains `mtp` or `nextn` keys.

The user may override warnings, but config mismatch and disk shortage should be treated as hard blockers unless they explicitly accept the risk.

## Test Strategy

Run a GGUF smoke test before upload:

```bash
python3 scripts/qwen_gguf_smoke_test.py \
  --model ./target-qwen-MTP-F16.gguf \
  --llama-cli ./llama.cpp/build/bin/llama-cli \
  --prompt "State the capital of France in one short sentence." \
  --gpu-layers 0
```

HF-side tests can use:

```python
prompt = processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
inputs = processor(text=[prompt], return_tensors="pt")
```

GGUF-side tests use Qwen/ChatML prompt text:

```text
<|im_start|>system
You are a helpful AI assistant.<|im_end|>
<|im_start|>user
State the capital of France.<|im_end|>
<|im_start|>assistant
```

## Release Checklist

- `preflight_report.md` reviewed.
- `pipeline.log` shows MTP validation and index injection.
- `smoke_*.log` exists and shows successful inference.
- Every expected GGUF file exists locally or remotely.
- Local cleanup happened only after confirmed upload.
- Public README contains no private paths, tokens, or personal repo details.
