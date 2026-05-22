#!/usr/bin/env python3
"""CPU smoke test for Qwen-family GGUF files with a ChatML-style prompt."""

from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


def qwen_chatml_prompt(user_prompt: str, system_prompt: str) -> str:
    return (
        f"<|im_start|>system\n{system_prompt}<|im_end|>\n"
        f"<|im_start|>user\n{user_prompt}<|im_end|>\n"
        "<|im_start|>assistant\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="Path to GGUF model")
    parser.add_argument("--llama-cli", required=True, help="Path to llama-cli")
    parser.add_argument("--prompt", default="State the capital of France in one short sentence.")
    parser.add_argument("--system-prompt", default="You are a helpful AI assistant.")
    parser.add_argument("--max-tokens", type=int, default=96)
    parser.add_argument("--ctx-size", type=int, default=2048)
    parser.add_argument("--gpu-layers", type=int, default=0, help="Use 0 for CPU-only smoke tests")
    args = parser.parse_args()

    model = Path(args.model).expanduser()
    llama_cli = Path(args.llama_cli).expanduser()
    if not model.exists():
        raise FileNotFoundError(model)
    if not llama_cli.exists():
        raise FileNotFoundError(llama_cli)

    command = [
        str(llama_cli),
        "-m",
        str(model),
        "-p",
        qwen_chatml_prompt(args.prompt, args.system_prompt),
        "-n",
        str(args.max_tokens),
        "-c",
        str(args.ctx_size),
        "--temp",
        "0.2",
        "--top-p",
        "0.9",
        "-ngl",
        str(args.gpu_layers),
    ]
    print("Running:", " ".join(command))
    result = subprocess.run(command, text=True)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


if __name__ == "__main__":
    main()
