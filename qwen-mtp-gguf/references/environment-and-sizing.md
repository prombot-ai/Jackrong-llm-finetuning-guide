# Environment and Sizing

## What the public pipeline checks

Preflight should run before large downloads. It checks:

- OS and architecture with Python `platform`.
- CPU core count with `os.cpu_count()`.
- Total RAM with `os.sysconf` or platform fallback.
- Free disk space at the selected work directory.
- Optional GPU hints with `nvidia-smi` or macOS platform probes.
- Commands: `git`, `cmake`, `make`, `ninja`, `python3`, `pip`.
- Python packages: `huggingface_hub`, `safetensors`, `transformers`, `torch`.
- llama.cpp tools: `convert_hf_to_gguf.py`, `build/bin/llama-quantize`, and `build/bin/llama-cli`.
- HF token availability when private downloads or uploads are requested.

GPU is optional. llama.cpp supports CPU builds and many accelerated backends, but MTP extraction, index injection, HF-to-GGUF conversion, and quantization can be run without GPU acceleration.

## Disk estimates

Use HF metadata before download:

- `HfApi.model_info(..., files_metadata=True)` for file sizes.
- `model.safetensors.index.json` from the MTP source to identify only the MTP shards.
- The selected quant matrix to estimate output size.

Peak disk estimate:

```text
target HF directory
+ minimal MTP source shards
+ temporary F16 GGUF when non-BF16 quants are requested
+ live output GGUF files
+ safety margin
```

`stream` strategy uses the largest single output GGUF as the live output term. `batch` and `local-only` use the sum of all requested outputs.

The estimates are intentionally conservative because GGUF metadata, tokenizer assets, cache behavior, and quantization overhead vary by model and llama.cpp version.

## RAM estimates

Recommended RAM is estimated from the temporary F16 GGUF size. The tool should warn or block when RAM is clearly below the estimated conversion/quantization working set. Users can override with `--allow-low-ram` if they accept slow swapping or have external evidence that the target model works.

Practical rule of thumb:

- Small models under 4B parameters: 16-32 GB RAM is usually comfortable for CPU conversion/quantization.
- Mid-size models around 7B-14B: 32-64 GB RAM is safer.
- 27B-35B class models: 96 GB or more is a safer default, with large free disk.
- Very large or MoE models need a custom estimate from actual HF shard size and requested quants.

Do not present these as universal hard limits. Always prefer the preflight report from the actual target repo.

## Official references

- llama.cpp states that it supports CPU builds, Metal, CUDA, Vulkan, and other backends, and that it provides integer quantization formats for reduced memory use: https://github.com/ggml-org/llama.cpp
- llama.cpp build docs show the plain CPU CMake build and optional backend flags such as CUDA and Vulkan: https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md
- Hugging Face Hub `snapshot_download` supports `dry_run=True`, returning `DryRunFileInfo` without downloading files: https://huggingface.co/docs/huggingface_hub/en/package_reference/file_download
- Hugging Face Hub `model_info(..., files_metadata=True)` exposes per-file metadata useful for size estimates: https://huggingface.co/docs/huggingface_hub/en/package_reference/hf_api
- Transformers chat templates document `apply_chat_template`, message dictionaries with `role` and `content`, and `add_generation_prompt=True`: https://huggingface.co/docs/transformers/main/chat_templating
