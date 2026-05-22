#!/usr/bin/env bash
set -euo pipefail

PREFIX="${QWEN_MTP_PREFIX:-$PWD/qwen-mtp-gguf-env}"
LLAMA_CPP="${QWEN_MTP_LLAMA_CPP:-$PREFIX/llama.cpp}"
PYTHON_BIN="${PYTHON_BIN:-python3}"
BUILD_BACKEND="cpu"
INSTALL_SYSTEM_DEPS=0
WITH_HF_SMOKE=0
YES=0

usage() {
  cat <<'USAGE'
Usage: bootstrap_qwen_mtp_env.sh [options]

Options:
  --prefix DIR              Install workspace directory (default: ./qwen-mtp-gguf-env)
  --llama-cpp DIR           llama.cpp directory (default: <prefix>/llama.cpp)
  --backend cpu|cuda|metal|vulkan
  --install-system-deps     Try to install git/cmake/build tools with apt, dnf, pacman, or brew
  --with-hf-smoke           Also install torch/accelerate for HF-side smoke tests
  -y, --yes                 Do not prompt before system package install
  -h, --help                Show help
USAGE
}

while [[ $# -gt 0 ]]; do
  case "$1" in
    --prefix) PREFIX="$2"; shift 2 ;;
    --llama-cpp) LLAMA_CPP="$2"; shift 2 ;;
    --backend) BUILD_BACKEND="$2"; shift 2 ;;
    --install-system-deps) INSTALL_SYSTEM_DEPS=1; shift ;;
    --with-hf-smoke) WITH_HF_SMOKE=1; shift ;;
    -y|--yes) YES=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "Unknown option: $1" >&2; usage; exit 2 ;;
  esac
done

need_cmd() {
  command -v "$1" >/dev/null 2>&1
}

install_system_deps() {
  if [[ "$INSTALL_SYSTEM_DEPS" -ne 1 ]]; then
    return
  fi
  if [[ "$YES" -ne 1 ]]; then
    printf "Install system packages for build tools? [y/N] "
    read -r answer
    [[ "$answer" == "y" || "$answer" == "Y" ]] || return
  fi
  if need_cmd apt-get; then
    sudo apt-get update
    sudo apt-get install -y git cmake build-essential
  elif need_cmd dnf; then
    sudo dnf install -y git cmake gcc gcc-c++ make
  elif need_cmd pacman; then
    sudo pacman -S --needed --noconfirm git cmake base-devel
  elif need_cmd brew; then
    brew install git cmake || true
  else
    echo "No supported package manager found. Install git, cmake, and a C/C++ compiler manually." >&2
  fi
}

cmake_backend_flags() {
  case "$BUILD_BACKEND" in
    cpu) echo "" ;;
    cuda) echo "-DGGML_CUDA=ON" ;;
    metal) echo "-DGGML_METAL=ON" ;;
    vulkan) echo "-DGGML_VULKAN=ON" ;;
    *) echo "Unsupported backend: $BUILD_BACKEND" >&2; exit 2 ;;
  esac
}

install_system_deps

mkdir -p "$PREFIX"
"$PYTHON_BIN" -m venv "$PREFIX/.venv"
# shellcheck source=/dev/null
source "$PREFIX/.venv/bin/activate"
python -m pip install --upgrade pip wheel setuptools
python -m pip install --upgrade "huggingface_hub[hf_xet]" safetensors transformers sentencepiece protobuf
if [[ "$WITH_HF_SMOKE" -eq 1 ]]; then
  python -m pip install --upgrade torch accelerate
fi

if [[ ! -d "$LLAMA_CPP/.git" ]]; then
  git clone --depth 1 https://github.com/ggml-org/llama.cpp "$LLAMA_CPP"
else
  git -C "$LLAMA_CPP" pull --ff-only
fi

FLAGS="$(cmake_backend_flags)"
cmake -S "$LLAMA_CPP" -B "$LLAMA_CPP/build" -DCMAKE_BUILD_TYPE=Release $FLAGS
cmake --build "$LLAMA_CPP/build" --config Release -j "$(python - <<'PY'
import os
print(max(1, min(os.cpu_count() or 1, 16)))
PY
)"

cat <<EOF

Bootstrap complete.
Activate Python environment:
  source "$PREFIX/.venv/bin/activate"

Use llama.cpp path:
  --llama-cpp "$LLAMA_CPP"
EOF
