#!/usr/bin/env bash
set -euo pipefail

if [ ! -d .git ]; then
  echo "Error: ejecutar desde la raiz del repositorio MCC225."
  exit 1
fi

cat <<'MSG'
### Limpieza sin reescribir historia
Este script hace git rm --cached de datasets y artefactos regenerables.
No borra archivos locales. Solo deja de versionarlos desde el siguiente commit.
MSG

paths=(
  "Semana3/Cuadernos/data/images"
  "Semana4/Proyecto/data/bootstrap_flickr30k/images"
  "Semana4/Proyecto/data/flickr1k_hf/images"
  "Semana4/Proyecto/data/processed"
  "Semana5/Proyecto/data/bootstrap_flickr30k/images"
  "Semana5/Proyecto/data/flickr1k_eval_300/images"
)

for p in "${paths[@]}"; do
  if git ls-files --error-unmatch "$p" >/dev/null 2>&1 || git ls-files "$p" | grep -q .; then
    echo "Sacando del indice: $p"
    git rm -r --cached --ignore-unmatch "$p"
  else
    echo "No trackeado o no existe: $p"
  fi
done

# Artefactos por extension en todo el repositorio.
while IFS= read -r f; do
  [ -n "$f" ] || continue
  echo "Sacando del indice: $f"
  git rm --cached --ignore-unmatch "$f"
done < <(git ls-files '*.npz' '*.npy' '*.pt' '*.pth' '*.ckpt' '*.safetensors' '*.h5' '*.onnx' '*.bin' '*.parquet')

echo
printf "### Estado despues de git rm --cached\n"
git status --short --untracked-files=no

echo
cat <<'MSG'
Siguiente paso sugerido:
  git add .gitignore .gitattributes .dockerignore .pre-commit-config.yaml docs scripts
  git commit -m "Ordena politica de datos y deja de versionar artefactos regenerables"
MSG
