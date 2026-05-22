# Troubleshooting

## No MTP tensors found

- Confirm the MTP source model actually contains MTP or `nextn` tensors.
- Confirm the source repo is the same architecture and size as the target model.
- If the source has no `model.safetensors.index.json`, ask before scanning all safetensors because it can download large files.

## Indexed key cannot be opened

- Check that the `weight_map` filename exists in the prepared HF directory.
- Re-open `mtp_heads.safetensors` and compare its keys with the index additions.
- Restore `model.safetensors.index.pre_mtp_backup.json` only when the prepared directory needs to be rebuilt.

## llama.cpp conversion fails

- Verify `convert_hf_to_gguf.py` and `build/bin/llama-quantize` exist.
- Set `PYTHONPATH=<llama.cpp>/gguf-py`.
- Check that `config.json`, tokenizer files, safetensors shards, and index are all present in the prepared HF directory.
- Update or rebuild llama.cpp if the model architecture is newer than the local converter.

## Disk pressure

- Run `--preflight-only` before downloading large files.
- Prefer `--upload-strategy stream` so only one quantized GGUF is live at a time.
- Use index-based MTP extraction to avoid downloading full base models.
- Upload and delete each quantized GGUF after confirmation.
- Keep the temporary F16 GGUF only until all non-BF16 quantizations are complete.

## RAM pressure

- Use CPU-only smoke tests with a small context and token count.
- Run fewer quant formats first, such as `q4_k_m,q8_0`, before a full matrix.
- If the machine swaps heavily or the process is killed, move the job to a larger RAM machine. GPU VRAM is not required for conversion or quantization, but system RAM still matters.

## Config mismatch

- Stop when target and MTP source `config.json` fields differ on hidden size, layer count, attention heads, KV heads, or vocab size.
- Do not assume that a nearby Qwen size can supply compatible MTP heads.
- Continue with `--allow-config-mismatch` only after manual review.

## Smoke test fails

- Confirm `llama-cli` exists and the GGUF path is correct.
- Try `-ngl 0` to avoid GPU backend issues.
- Verify the prompt format uses Qwen/ChatML markers or the model's embedded chat template.
- If F16 smoke test fails before quantization, do not upload downstream quants.

## Upload failures

- Use `HfApi.list_repo_files` before each resume.
- Retry uploads with increasing waits and a long socket timeout.
- Do not regenerate a quant if the local file already exists and is nonzero.
