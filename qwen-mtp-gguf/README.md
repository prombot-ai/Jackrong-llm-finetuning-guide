# Qwen MTP GGUF Conversion Skill

Agent-ready scripts and references for Qwen-family MTP/nextn GGUF releases. The workflow preflights disk/RAM/tooling, extracts compatible MTP heads from a matching source model, injects them into a target HF model, converts with llama.cpp, runs smoke tests, quantizes, and optionally uploads to Hugging Face.

## Quick Start

```bash
cp env.example .env
# Edit .env and export HF_TOKEN before private downloads/uploads.

bash scripts/bootstrap_qwen_mtp_env.sh --prefix ./qwen-mtp-env --backend cpu
source ./qwen-mtp-env/.venv/bin/activate

python3 scripts/qwen_mtp_gguf_pipeline.py \
  --jobs jobs.example.json \
  --llama-cpp ./qwen-mtp-env/llama.cpp \
  --preflight-only
```

If `preflight_report.md` has no hard blockers, run the full pipeline:

```bash
python3 scripts/qwen_mtp_gguf_pipeline.py \
  --jobs jobs.example.json \
  --llama-cpp ./qwen-mtp-env/llama.cpp \
  --upload-strategy stream \
  --smoke-test-before-upload \
  --cleanup-after-upload
```

## Disk and RAM Check

Run `--preflight-only` before downloading full model weights. The report estimates:

- target HF model download size
- minimal MTP source shard download size
- temporary F16/BF16 GGUF size
- requested quantized GGUF size
- free disk required after the safety factor
- RAM risk for conversion and quantization

Use `stream` upload when disk is tight. It quantizes one file, uploads it, then removes it after upload confirmation. Use `batch` only when you have enough disk to keep every requested GGUF at once.

As a quick manual rule, reserve enough free disk for:

```text
target HF model + MTP shards + temporary F16 GGUF + largest requested quant + 25% safety margin
```

For RAM, conversion and quantization are CPU workflows, but large models still need substantial host memory. If preflight marks RAM as low, reduce concurrent work, choose fewer quant formats, use a larger machine, or pass an override only after accepting the risk.

## Included Files

- `SKILL.md`: Codex skill metadata and staged operating procedure.
- `agents/openai.yaml`: short agent UI metadata.
- `scripts/qwen_mtp_gguf_pipeline.py`: preflight, MTP extraction, injection, conversion, quantization, upload, and cleanup.
- `scripts/bootstrap_qwen_mtp_env.sh`: Python dependency and llama.cpp bootstrap helper.
- `scripts/qwen_gguf_smoke_test.py`: GGUF smoke test through `llama-cli`.
- `scripts/qwen_hf_smoke_test.py`: HF model smoke test with Qwen chat formatting.
- `references/`: implementation notes for sizing, technical flow, troubleshooting, and agent integration.
- `docs/`: publish-ready README, pipeline guide, and agent usage guide.
- `jobs.example.json`: multi-job pipeline configuration template.
- `env.example`: environment variable template.

## Documentation

- [Skill README](docs/Qwen-MTP-GGUF-Skill-README.md)
- [Pipeline Guide](docs/Qwen-MTP-GGUF-Pipeline-Guide.md)
- [Agent Usage Guide](docs/Qwen-MTP-GGUF-Agent-Usage.md)
- [Environment and Sizing](references/environment-and-sizing.md)
- [Technical Flow](references/technical-flow.md)
- [Troubleshooting](references/troubleshooting.md)
- [Agent Integration](references/agent-integration.md)

## Safety Defaults

- Run preflight first.
- Keep examples generic and public-safe.
- Prefer CPU mode unless accelerated smoke tests are explicitly needed.
- Treat target/source config mismatch and disk shortage as blockers.
- Keep tokens, private paths, repo secrets, and raw server logs out of public commits.

## License

MIT. See [LICENSE](LICENSE).
