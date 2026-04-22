#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

torchrun \
  --nproc_per_node=1 \
  scripts/02_build_embeddings.py \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --model-name ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 16 \
  --output outputs/embeddings/bootstrap_embeddings.npz