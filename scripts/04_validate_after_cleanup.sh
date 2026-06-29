#!/usr/bin/env bash
set -euo pipefail

if [ ! -d .git ]; then
  echo "Error: ejecutar desde la raiz del repositorio MCC225."
  exit 1
fi

echo "### Estado Git"
git status --short --untracked-files=all

echo
printf "### Verificando archivos grandes trackeados en HEAD mayores a 500 KB\n"
found=0
while IFS= read -r path; do
  [ -f "$path" ] || continue
  size=$(wc -c < "$path")
  if [ "$size" -gt 512000 ]; then
    printf "%12d  %s\n" "$size" "$path"
    found=1
  fi
done < <(git ls-files)

if [ "$found" -eq 0 ]; then
  echo "OK: no hay archivos trackeados mayores a 500 KB en HEAD."
fi

echo
printf "### Archivos ignorados relevantes\n"
git check-ignore -v \
  Semana3/Cuadernos/data/images/ejemplo.png \
  Semana4/Proyecto/data/processed/ejemplo.csv \
  Semana5/Proyecto/data/flickr1k_eval_300/images/ejemplo.jpg \
  Semana5/Proyecto/outputs/embeddings/clip_embeddings.npz \
  2>/dev/null || true
