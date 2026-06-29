#!/usr/bin/env bash
set -euo pipefail

if [ ! -d .git ]; then
  echo "Error: ejecutar desde la raiz del repositorio MCC225."
  exit 1
fi

if ! command -v git-filter-repo >/dev/null 2>&1; then
  echo "Error: falta git-filter-repo. Instalar con: python -m pip install git-filter-repo"
  exit 1
fi

if [ "${CONFIRM_REWRITE:-}" != "1" ]; then
  cat <<'MSG'
Este script reescribe historia. Cambia hashes de commits.
Antes de ejecutarlo:
  1. Hacer un clone fresco del repositorio.
  2. Avisar que quienes tengan clones/forks deben volver a clonar.
  3. Verificar que los datos removidos se regeneran por script.

Para ejecutar de verdad:
  CONFIRM_REWRITE=1 scripts/03_rewrite_history_assets.sh
MSG
  exit 1
fi

backup_branch="backup-antes-limpieza-$(date +%Y%m%d-%H%M%S)"
git branch "$backup_branch"
git tag "$backup_branch" || true

echo "Backup local creado: $backup_branch"

git filter-repo --force \
  --path-glob 'Semana3/Cuadernos/data/images/**' \
  --path-glob 'Semana4/Proyecto/data/bootstrap_flickr30k/images/**' \
  --path-glob 'Semana4/Proyecto/data/flickr1k_hf/images/**' \
  --path-glob 'Semana4/Proyecto/data/processed/**' \
  --path-glob 'Semana5/Proyecto/data/bootstrap_flickr30k/images/**' \
  --path-glob 'Semana5/Proyecto/data/flickr1k_eval_300/images/**' \
  --path-glob '*.npz' \
  --path-glob '*.npy' \
  --path-glob '*.pt' \
  --path-glob '*.pth' \
  --path-glob '*.ckpt' \
  --path-glob '*.safetensors' \
  --path-glob '*.h5' \
  --path-glob '*.onnx' \
  --path-glob '*.bin' \
  --path-glob '*.parquet' \
  --invert-paths

git reflog expire --expire=now --all
git gc --prune=now --aggressive

echo
printf "### Tamano de .git despues de limpieza\n"
du -sh .git || true

echo
cat <<'MSG'
Para publicar la historia reescrita:
  git push --force-with-lease origin main

Despues, pedir a colaboradores y estudiantes:
  git clone https://github.com/kapumota/MCC225.git
MSG
