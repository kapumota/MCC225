#!/usr/bin/env bash
set -euo pipefail

if [ ! -d .git ]; then
  echo "Error: ejecutar desde la raiz del repositorio MCC225."
  exit 1
fi

echo "### Tamano de .git"
du -sh .git || true

echo
printf "### Archivos trackeados mas grandes en HEAD\n"
git ls-files -s | awk '{print $4}' | while IFS= read -r path; do
  [ -f "$path" ] || continue
  size=$(wc -c < "$path")
  printf "%12d  %s\n" "$size" "$path"
done | sort -rn | head -50

echo
printf "### Blobs mas grandes en toda la historia\n"
git rev-list --objects --all | \
  git cat-file --batch-check='%(objecttype) %(objectname) %(objectsize) %(rest)' | \
  awk '$1 == "blob" {print $3, $4}' | sort -rn | head -50

echo
printf "### Conteo de candidatos a salir de Git\n"
for pattern in \
  '*.npz' '*.npy' '*.pt' '*.pth' '*.ckpt' '*.safetensors' \
  'Semana3/Cuadernos/data/images/*' \
  'Semana4/Proyecto/data/bootstrap_flickr30k/images/*' \
  'Semana4/Proyecto/data/flickr1k_hf/images/*' \
  'Semana4/Proyecto/data/processed/*' \
  'Semana5/Proyecto/data/bootstrap_flickr30k/images/*' \
  'Semana5/Proyecto/data/flickr1k_eval_300/images/*'
do
  count=$(git ls-files -- "$pattern" | wc -l | tr -d ' ')
  printf "%6s  %s\n" "$count" "$pattern"
done
