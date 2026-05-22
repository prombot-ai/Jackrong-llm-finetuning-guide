# Technical Flow

## MTP tensor identification

Use case-insensitive key matching for `mtp` and `nextn`. Prefer index-based discovery over full-file scanning:

1. Download or read `model.safetensors.index.json`.
2. Collect matching keys from `weight_map`.
3. Build the minimal shard list from those keys.
4. Open only the needed shards with `safetensors.safe_open`.
5. Save the collected tensors with `safetensors.torch.save_file`.

This avoids downloading every shard of large base models when the MTP heads live in only a few shards.

## Feasibility check

Before extraction, compare target and MTP source `config.json` values for architecture-level fields such as `model_type`, `hidden_size`, `num_hidden_layers`, `num_attention_heads`, `num_key_value_heads`, `intermediate_size`, `vocab_size`, `rope_theta`, and `max_position_embeddings`.

Treat mismatches as blockers unless the user explicitly confirms that the target model intentionally changed that field and that the MTP source still matches the tensor layout. Fine-tuning should normally preserve these fields.

## Target model preparation

The prepared HF directory must contain the target model's normal config/tokenizer files and safetensors shards. Existing GGUF files, optimizer states, training checkpoints, logs, and experiment folders should not be downloaded or copied into the conversion directory.

The injection step modifies only the prepared copy:

- `mtp_heads.safetensors` is added to the directory.
- `model.safetensors.index.json` is backed up if present.
- Every extracted MTP key is mapped to `mtp_heads.safetensors`.
- If no index exists, build one by scanning every local `.safetensors` shard.

## llama.cpp conversion pattern

Set `PYTHONPATH` to llama.cpp's `gguf-py` directory before running `convert_hf_to_gguf.py`.

Use F16 as the temporary source for most quantization types. Generate BF16 directly from the prepared HF model directory because it is a precision-preserving output, not a quantization from F16.

## Qwen smoke-test formatting

For HF model smoke tests, format messages through the model tokenizer or processor:

```python
messages = [
    {"role": "system", "content": "You are a helpful AI assistant."},
    {"role": "user", "content": "State the capital of France."},
]
prompt = processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
inputs = processor(text=[prompt], return_tensors="pt")
```

For GGUF smoke tests with `llama-cli`, use ChatML-style text:

```text
<|im_start|>system
You are a helpful AI assistant.<|im_end|>
<|im_start|>user
State the capital of France.<|im_end|>
<|im_start|>assistant
```

Default to CPU smoke tests with `-ngl 0`. GPU offload is optional and should be requested explicitly.

## Upload and cleanup policy

Always list remote files before work begins. This makes runs resumable and prevents repeat uploads.

Only delete local files after the corresponding upload succeeds. Do not delete the prepared HF directory or temporary F16 file if a job fails; they are useful for resume and debugging.

When publishing publicly, remove private paths, tokens, internal model names, and machine-specific logs from README text.
