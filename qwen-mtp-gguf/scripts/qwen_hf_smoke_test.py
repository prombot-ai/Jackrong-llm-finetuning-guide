#!/usr/bin/env python3
"""HF-side smoke test for a Qwen-family model directory before GGUF conversion."""

from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", required=True, help="HF model repo or local directory")
    parser.add_argument("--prompt", default="Write one concise sentence about MTP inference.")
    parser.add_argument("--system-prompt", default="You are a helpful AI assistant.")
    parser.add_argument("--max-new-tokens", type=int, default=128)
    parser.add_argument("--dtype", default="bfloat16", choices=["auto", "float16", "bfloat16", "float32"])
    parser.add_argument("--device-map", default="auto")
    args = parser.parse_args()

    try:
        import torch
        from transformers import AutoModelForCausalLM, AutoProcessor, AutoTokenizer
    except ImportError as exc:
        raise SystemExit(
            "HF smoke tests require torch and transformers. "
            "Run bootstrap_qwen_mtp_env.sh --with-hf-smoke or install them manually."
        ) from exc

    dtype = {
        "auto": "auto",
        "float16": torch.float16,
        "bfloat16": torch.bfloat16,
        "float32": torch.float32,
    }[args.dtype]

    try:
        processor = AutoProcessor.from_pretrained(args.model, trust_remote_code=True)
    except Exception:
        processor = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)

    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        torch_dtype=dtype,
        device_map=args.device_map,
        trust_remote_code=True,
    )

    messages = [
        {"role": "system", "content": args.system_prompt},
        {"role": "user", "content": args.prompt},
    ]
    prompt = processor.apply_chat_template(messages, add_generation_prompt=True, tokenize=False)
    device = getattr(model, "device", None) or next(model.parameters()).device
    inputs = processor(text=[prompt], return_tensors="pt").to(device)
    generate_kwargs = dict(
        **inputs,
        max_new_tokens=args.max_new_tokens,
        temperature=0.2,
        do_sample=False,
        use_cache=True,
    )
    pad_token_id = getattr(processor, "pad_token_id", None) or getattr(getattr(processor, "tokenizer", None), "pad_token_id", None)
    if pad_token_id is not None:
        generate_kwargs["pad_token_id"] = pad_token_id
    outputs = model.generate(**generate_kwargs)
    prompt_length = inputs.input_ids.shape[1]
    response_tokens = outputs[0][prompt_length:]
    print(processor.decode(response_tokens, skip_special_tokens=False))


if __name__ == "__main__":
    main()
