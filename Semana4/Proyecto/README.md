### **Semana 4 - Proyecto OpenCLIP**

Proyecto reproducible para **aprendizaje contrastivo imagen-texto** con OpenCLIP, organizado en una estructura ejecutable para:

- extracción de embeddings imagen/texto,
- evaluación de **cross-modal retrieval**,
- análisis de **hard negatives**,
- evaluación **zero-shot**,
- y plantillas de entrenamiento local, `torchrun` y SLURM.

La carpeta real del proyecto es:

```text
Semana4/Proyecto
```

No asumas que este contenido vive directamente en `Semana4/`.


#### **1. Estructura del proyecto**

```text
Semana4/
├── papers/
└── Proyecto/
    ├── configs/
    ├── Cuaderno9-MCC225.ipynb
    ├── data/
    │   ├── bootstrap_flickr30k/
    │   ├── interim/
    │   ├── processed/
    │   └── raw/
    ├── outputs/
    │   ├── embeddings/
    │   ├── figures/
    │   ├── logs/
    │   └── metrics/
    ├── reports/
    ├── requirements-extra.txt
    ├── pyproject.toml
    ├── scripts/
    ├── slurm/
    └── src/
```



#### **2. Qué hace este proyecto**

Este proyecto toma la idea del cuaderno `Cuaderno9-MCC225.ipynb` y la organiza como un flujo reproducible.

**Pipeline principal**

1. verificar entorno,
2. cargar un checkpoint preentrenado de OpenCLIP,
3. construir embeddings de imágenes y captions,
4. evaluar retrieval imagen→texto y texto→imagen,
5. guardar hard negatives,
6. ejecutar una evaluación zero-shot simple.


**Recursos incluidos**

- un subconjunto pequeño de **Flickr30k** ya listo en `data/bootstrap_flickr30k/`,
- scripts ejecutables en `scripts/`,
- utilidades reutilizables en `src/`,
- plantillas para ejecución distribuida en `slurm/`.


#### **3. Requisitos del entorno**

Este proyecto está pensado para ejecutarse **encima del entorno principal del repositorio `MCC225`**.

**Recomendación**

Usa una de estas dos opciones:

**Opción A: Docker del repositorio principal**
Construye la imagen completa del curso con paquetes opcionales y luego entra al contenedor.

**Opción B: entorno local ya basado en el repositorio**
Ten instalado al menos:

- `requirements-base.txt`
- `requirements-opcional.txt`
- este archivo `Semana4/Proyecto/requirements-extra.txt`

> `requirements-extra.txt` de esta carpeta está diseñado para **complementar** el entorno del repositorio, no para reemplazarlo.



#### **4. `requirements-extra.txt`**

Usa este contenido exacto:

```txt
# Extras mínimos para Semana4/Proyecto.
# Este archivo complementa el entorno principal del repositorio MCC225.
# Úsalo encima de requirements-base.txt + requirements-opcional.txt,
# o dentro de la imagen Docker construida con INSTALL_OPCIONAL=true.
#
# Motivo:
# - El proyecto importa yaml.
# - Este proyecto usa Flickr30k desde Hugging Face.
# - Fijamos datasets<4 para evitar el error:
#   "Dataset scripts are no longer supported, but found flickr30k.py"

PyYAML==6.0.2
datasets==3.6.0
```

**¿Por qué existe este archivo?**

Sirve para **agregar solo los extras realmente necesarios** del proyecto:

- `PyYAML==6.0.2`: porque el proyecto usa `yaml`.
- `datasets==3.6.0`: porque con `datasets` 4.x aparece el error:

```text
RuntimeError: Dataset scripts are no longer supported, but found flickr30k.py
```

Eso ocurre al intentar cargar `nlphuji/flickr30k` desde Hugging Face con versiones más nuevas de `datasets`.



#### **5. `pyproject.toml`**

Usa este contenido exacto:

```toml
[build-system]
requires = ["setuptools>=68", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "semana4-proyecto"
version = "0.1.0"
description = "Proyecto Semana 4 con OpenCLIP"
requires-python = ">=3.11"

[tool.setuptools.packages.find]
where = ["."]
include = ["src*"]
```

**¿Por qué se usa `pyproject.toml`?**

Porque hace que el proyecto sea **instalable** y permite ejecutar:

```bash
cd /workspace/Semana4/Proyecto
pip install -e .
```

Eso evita depender de:

```bash
export PYTHONPATH="$(pwd):${PYTHONPATH:-}"
```

Y hace que `import src` funcione bien desde:

- scripts ejecutados con `python scripts/...`
- `bash scripts/run_local_pipeline.sh`
- Jupyter Notebook / JupyterLab
- sesiones interactivas dentro del contenedor



#### **6. Ejecución recomendada con Docker GPU**

Desde la raíz del repositorio `MCC225/`:

**6.1 Borrar contenedor e imagen anteriores**

```bash
docker rm -f mcc225_gpu_container
docker rmi -f mcc225_gpu
```

Si el contenedor no existe, el error es normal y no pasa nada.

**6.2 Construir imagen**

```bash
docker context use default

docker build --no-cache \
  --build-arg TORCH_FLAVOR=cu121 \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225_gpu .
```

**6.3 Ejecutar contenedor**

```bash
docker run -it --rm \
  --gpus all \
  --name mcc225_gpu_container \
  -p 8899:8899 \
  -v "$(pwd)":/workspace \
  mcc225_gpu
```

**6.4 Abrir JupyterLab**

```text
http://localhost:8899/lab
```


#### **7. Cómo entrar a Bash dentro del contenedor**

Si el contenedor ya está corriendo:

```bash
docker exec -it mcc225_gpu_container bash
```

Si quieres iniciar el contenedor directamente en Bash:

```bash
docker run -it --rm \
  --gpus all \
  --name mcc225_gpu_container \
  -p 8899:8899 \
  -v "$(pwd)":/workspace \
  --entrypoint bash \
  mcc225_gpu
```



#### **8. Mejorar la terminal de la imagen Docker**

El terminal por defecto puede venir sin autocompletado. La mejora recomendada es instalar:

- `bash-completion`
- `fzf`
- `tree`
- `ripgrep`
- `fd-find`
- `less`, `nano`, `vim`

Y activar `bash-completion` en `/etc/bash.bashrc`.

Si ya modificaste el `Dockerfile`, reconstruye la imagen con los comandos de la sección 6.


#### **9. Instalación dentro del contenedor**

Dentro del contenedor, desde la raíz del proyecto:

```bash
cd /workspace/Semana4/Proyecto
pip install -r requirements-extra.txt
pip install -e .
```

**Verificación**

```bash
python -c "import src; print(src.__file__)"
```

Si eso imprime algo como:

```text
/workspace/Semana4/Proyecto/src/__init__.py
```

entonces el paquete quedó bien instalado.

> Si estás usando Jupyter, reinicia el kernel después de `pip install -e .`.



#### **10. Ejecución rápida del pipeline base**

El script principal usa el subconjunto incluido en:

```text
data/bootstrap_flickr30k/metadata.csv
```

Ejecútalo desde `Semana4/Proyecto`:

```bash
bash scripts/run_local_pipeline.sh
```

Este script hace lo siguiente:

- ejecuta `scripts/00_verify_env.py`,
- construye embeddings con `scripts/02_build_embeddings.py`,
- evalúa retrieval con `scripts/03_eval_retrieval.py`,
- ejecuta zero-shot con `scripts/04_eval_zeroshot.py`.



#### **11. Uso con SLURM (opcional)**

SLURM sirve para enviar trabajos al scheduler de un cluster. En este proyecto ya hay plantillas listas en la carpeta `slurm/`.

**Archivos disponibles**

- `slurm/extract_embeddings_single_node.sbatch`: extrae embeddings en 1 nodo con 1 GPU.
- `slurm/train_openclip_csv_single_node.sbatch`: entrenamiento en 1 nodo con 1 GPU.
- `slurm/train_openclip_csv_multi_node.sbatch`: entrenamiento distribuido en 2 nodos usando `torchrun`.

**Antes de enviar trabajos

En el cluster, entra a la carpeta del proyecto y deja el entorno instalado al menos una vez:

```bash
cd /ruta/al/proyecto/Semana4/Proyecto
pip install -r requirements-extra.txt
pip install -e .
```

Si tu cluster usa módulos, `conda` o un entorno virtual, activa primero el entorno correcto antes de correr `sbatch`.

**Script exacto: extracción de embeddings en 1 nodo**

Archivo: `slurm/extract_embeddings_single_node.sbatch`

```bash
#!/bin/bash -x
#SBATCH --job-name=mcc225_embed_extract
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=24G
#SBATCH --time=01:00:00
#SBATCH --output=outputs/logs/extract_%j.out

cd "${SLURM_SUBMIT_DIR}"

python scripts/02_build_embeddings.py   --metadata-csv data/bootstrap_flickr30k/metadata.csv   --model-name ViT-B-32   --pretrained laion2b_s34b_b79k   --batch-size 16   --output outputs/embeddings/bootstrap_embeddings.npz
```

Envío:

```bash
sbatch slurm/extract_embeddings_single_node.sbatch
```

**Script exacto: entrenamiento OpenCLIP en 1 nodo**

Archivo: `slurm/train_openclip_csv_single_node.sbatch`

```bash
#!/bin/bash -x
#SBATCH --job-name=mcc225_openclip_single
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=outputs/logs/slurm_single_%j.out

cd "${SLURM_SUBMIT_DIR}"

python -m open_clip_train.main   --dataset-type csv   --train-data data/bootstrap_flickr30k/metadata.csv   --val-data data/bootstrap_flickr30k/metadata.csv   --csv-img-key filepath   --csv-caption-key caption   --model ViT-B-32   --pretrained laion2b_s34b_b79k   --batch-size 8   --workers 4   --precision amp   --epochs 1   --lr 1e-5   --wd 0.1   --warmup 10   --logs outputs/logs/openclip_slurm_single   --name week4_slurm_single
```

Envío:

```bash
sbatch slurm/train_openclip_csv_single_node.sbatch
```

**Script exacto: entrenamiento OpenCLIP multi-node**

Archivo: `slurm/train_openclip_csv_multi_node.sbatch`

```bash
#!/bin/bash -x
#SBATCH --job-name=mcc225_openclip_multi
#SBATCH --nodes=2
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=outputs/logs/slurm_multi_%j.out
#SBATCH --wait-all-nodes=1

cd "${SLURM_SUBMIT_DIR}"

export MASTER_PORT=12802
master_addr=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1)
export MASTER_ADDR="${master_addr}"

torchrun   --nnodes="${SLURM_JOB_NUM_NODES}"   --nproc_per_node=1   --rdzv_backend=c10d   --rdzv_endpoint="${MASTER_ADDR}:${MASTER_PORT}"   -m open_clip_train.main   --dataset-type csv   --train-data data/bootstrap_flickr30k/metadata.csv   --val-data data/bootstrap_flickr30k/metadata.csv   --csv-img-key filepath   --csv-caption-key caption   --model ViT-B-32   --pretrained laion2b_s34b_b79k   --batch-size 8   --workers 4   --precision amp   --epochs 1   --lr 1e-5   --wd 0.1   --warmup 10   --local-loss   --gather-with-grad   --logs outputs/logs/openclip_slurm_multi   --name week4_slurm_multi
```

Envío:

```bash
sbatch slurm/train_openclip_csv_multi_node.sbatch
```

**Cómo monitorear trabajos**

Ver cola de trabajos:

```bash
squeue -u $USER
```

Ver detalle de un trabajo:

```bash
scontrol show job <JOB_ID>
```

Cancelar un trabajo:

```bash
scancel <JOB_ID>
```


**Logs**


Los scripts escriben logs en `outputs/logs/`. Ejemplos:

```text
outputs/logs/extract_<jobid>.out
outputs/logs/slurm_single_<jobid>.out
outputs/logs/slurm_multi_<jobid>.out
```

Para seguir un log en vivo:

```bash
tail -f outputs/logs/extract_<jobid>.out
```

**Qué ajustar si tu cluster lo pide**

Estos scripts asumen una configuración SLURM relativamente estándar. Si tu cluster usa particiones, cuentas o QoS, agrega lo que corresponda, por ejemplo:

```bash
#SBATCH --partition=gpu
#SBATCH --account=tu_cuenta
```

También podrías necesitar ajustar:

- `#SBATCH --gres=gpu:1`
- `#SBATCH --cpus-per-task=...`
- `#SBATCH --mem=...`
- `#SBATCH --time=...`
- `#SBATCH --nodes=...`

#### **Recomendación práctica**

Primero valida el pipeline localmente:

```bash
bash scripts/run_local_pipeline.sh
```

Luego prueba en el cluster, en este orden:

```bash
sbatch slurm/extract_embeddings_single_node.sbatch
sbatch slurm/train_openclip_csv_single_node.sbatch
```

Y deja `train_openclip_csv_multi_node.sbatch` para el final, cuando ya tengas claro que el entorno, los paths y el entrenamiento funcionan bien en un solo nodo.


#### **12. Launchers**

**`scripts/run_local_pipeline.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python scripts/00_verify_env.py

python scripts/02_build_embeddings.py \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --model-name ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 16 \
  --output outputs/embeddings/bootstrap_embeddings.npz

python scripts/03_eval_retrieval.py \
  --embeddings outputs/embeddings/bootstrap_embeddings.npz \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --output-json outputs/metrics/retrieval_metrics.json \
  --hard-negatives-csv outputs/metrics/hard_negatives.csv \
  --top-n-hard-negatives 8

python scripts/04_eval_zeroshot.py \
  --embeddings outputs/embeddings/bootstrap_embeddings.npz \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --prompt-config data/bootstrap_flickr30k/prompt_config.json \
  --output-csv outputs/metrics/zeroshot_predictions.csv
```

**`scripts/run_torchrun_single_node.sh`**

```bash
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
```

**`scripts/10_train_openclip_csv_local.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

python -m open_clip_train.main \
  --dataset-type csv \
  --train-data data/bootstrap_flickr30k/metadata.csv \
  --val-data data/bootstrap_flickr30k/metadata.csv \
  --csv-img-key filepath \
  --csv-caption-key caption \
  --model ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 8 \
  --workers 2 \
  --precision amp \
  --epochs 1 \
  --lr 1e-5 \
  --wd 0.1 \
  --warmup 10 \
  --logs outputs/logs/openclip_train_local \
  --name week4_bootstrap_local
```

**`scripts/11_train_openclip_csv_torchrun.sh`**

```bash
#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")/.."

torchrun \
  --nproc_per_node=1 \
  -m open_clip_train.main \
  --dataset-type csv \
  --train-data data/bootstrap_flickr30k/metadata.csv \
  --val-data data/bootstrap_flickr30k/metadata.csv \
  --csv-img-key filepath \
  --csv-caption-key caption \
  --model ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 8 \
  --workers 2 \
  --precision amp \
  --epochs 1 \
  --lr 1e-5 \
  --wd 0.1 \
  --warmup 10 \
  --local-loss \
  --gather-with-grad \
  --logs outputs/logs/openclip_train_torchrun \
  --name week4_bootstrap_torchrun
```

**`slurm/extract_embeddings_single_node.sbatch`**

```bash
#!/bin/bash -x
#SBATCH --job-name=mcc225_embed_extract
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=24G
#SBATCH --time=01:00:00
#SBATCH --output=outputs/logs/extract_%j.out

cd "${SLURM_SUBMIT_DIR}"

python scripts/02_build_embeddings.py \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --model-name ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 16 \
  --output outputs/embeddings/bootstrap_embeddings.npz
```

**`slurm/train_openclip_csv_single_node.sbatch`**

```bash
#!/bin/bash -x
#SBATCH --job-name=mcc225_openclip_single
#SBATCH --nodes=1
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=outputs/logs/slurm_single_%j.out

cd "${SLURM_SUBMIT_DIR}"

python -m open_clip_train.main \
  --dataset-type csv \
  --train-data data/bootstrap_flickr30k/metadata.csv \
  --val-data data/bootstrap_flickr30k/metadata.csv \
  --csv-img-key filepath \
  --csv-caption-key caption \
  --model ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 8 \
  --workers 4 \
  --precision amp \
  --epochs 1 \
  --lr 1e-5 \
  --wd 0.1 \
  --warmup 10 \
  --logs outputs/logs/openclip_slurm_single \
  --name week4_slurm_single
```

**`slurm/train_openclip_csv_multi_node.sbatch`**

```bash
#!/bin/bash -x
#SBATCH --job-name=mcc225_openclip_multi
#SBATCH --nodes=2
#SBATCH --gres=gpu:1
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=6
#SBATCH --mem=32G
#SBATCH --time=02:00:00
#SBATCH --output=outputs/logs/slurm_multi_%j.out
#SBATCH --wait-all-nodes=1

cd "${SLURM_SUBMIT_DIR}"

export MASTER_PORT=12802
master_addr=$(scontrol show hostnames "$SLURM_JOB_NODELIST" | head -n 1)
export MASTER_ADDR="${master_addr}"

torchrun \
  --nnodes="${SLURM_JOB_NUM_NODES}" \
  --nproc_per_node=1 \
  --rdzv_backend=c10d \
  --rdzv_endpoint="${MASTER_ADDR}:${MASTER_PORT}" \
  -m open_clip_train.main \
  --dataset-type csv \
  --train-data data/bootstrap_flickr30k/metadata.csv \
  --val-data data/bootstrap_flickr30k/metadata.csv \
  --csv-img-key filepath \
  --csv-caption-key caption \
  --model ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 8 \
  --workers 4 \
  --precision amp \
  --epochs 1 \
  --lr 1e-5 \
  --wd 0.1 \
  --warmup 10 \
  --local-loss \
  --gather-with-grad \
  --logs outputs/logs/openclip_slurm_multi \
  --name week4_slurm_multi
```

#### **13. Salidas esperadas**

Después de correr el pipeline, deberías obtener archivos como estos:

```text
outputs/embeddings/bootstrap_embeddings.npz
outputs/metrics/retrieval_metrics.json
outputs/metrics/hard_negatives.csv
outputs/metrics/zeroshot_predictions.csv
```

**Interpretación rápida**

- `bootstrap_embeddings.npz`: embeddings de imágenes y textos.
- `retrieval_metrics.json`: métricas de recuperación cruzada.
- `hard_negatives.csv`: emparejamientos difíciles o confusos.
- `zeroshot_predictions.csv`: predicciones zero-shot con prompts.



#### **14. Ejecución paso a paso**

**14.1 Verificar entorno**

```bash
python scripts/00_verify_env.py
```

**14.2 Construir embeddings**

```bash
python scripts/02_build_embeddings.py \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --model-name ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --batch-size 16 \
  --output outputs/embeddings/bootstrap_embeddings.npz
```

**14.3 Evaluar retrieval**

```bash
python scripts/03_eval_retrieval.py \
  --embeddings outputs/embeddings/bootstrap_embeddings.npz \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --output-json outputs/metrics/retrieval_metrics.json \
  --hard-negatives-csv outputs/metrics/hard_negatives.csv \
  --top-n-hard-negatives 8
```

**14.4 Evaluar zero-shot**

```bash
python scripts/04_eval_zeroshot.py \
  --embeddings outputs/embeddings/bootstrap_embeddings.npz \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --prompt-config data/bootstrap_flickr30k/prompt_config.json \
  --output-csv outputs/metrics/zeroshot_predictions.csv
```

**14.5 Inspeccionar negativos duros en consola**


```bash
python scripts/05_mine_hard_negatives.py \
  --embeddings outputs/embeddings/bootstrap_embeddings.npz \
  --metadata-csv data/bootstrap_flickr30k/metadata.csv \
  --top-n 10
```


#### **15. Dataset bootstrap incluido**

El proyecto ya trae un subconjunto mínimo en:

```text
data/bootstrap_flickr30k/
```

Este bootstrap permite validar el flujo sin descargar primero un dataset grande.

Contiene:

- imágenes,
- `metadata.csv`,
- `queries.csv`,
- `prompt_config.json`.



#### **16. Preparar un subconjunto mayor desde Hugging Face**

Si quieres trabajar con una versión más grande de Flickr30k:

```bash
python scripts/01_prepare_flickr30k_from_hf.py \
  --output-root data/processed/flickr30k_hf \
  --train-limit 512 \
  --val-limit 128 \
  --test-limit 128
```

**¿Qué significa "materializar un subconjunto mayor"?**

Significa:

- descargar datos,
- convertirlos al formato que espera el pipeline,
- guardar imágenes y CSVs en `data/processed/flickr30k_hf/`.

**¿Cuándo usarlo?**


Cuando ya validaste que el pipeline funciona con el bootstrap pequeño y quieres:

- hacer pruebas más realistas,
- medir retrieval con más datos,
- tener train/val/test más representativos,
- probar fine-tuning o evaluación más seria.

**¿Cuándo no hace falta?**

No hace falta si solo quieres:

- comprobar que el pipeline corre,
- depurar imports, rutas o dependencias,
- hacer una demo rápida.

Después puedes reutilizar los scripts de embeddings y retrieval cambiando el CSV:

```bash
python scripts/02_build_embeddings.py \
  --metadata-csv data/processed/flickr30k_hf/val.csv \
  --model-name ViT-B-32 \
  --pretrained laion2b_s34b_b79k \
  --output outputs/embeddings/flickr30k_val_embeddings.npz

python scripts/03_eval_retrieval.py \
  --embeddings outputs/embeddings/flickr30k_val_embeddings.npz \
  --metadata-csv data/processed/flickr30k_hf/val.csv
```

#### **17. Abrir el cuaderno**

Con JupyterLab expuesto en el contenedor:

```text
http://localhost:8899/lab
```

Abre:

```text
/workspace/Semana4/Proyecto/Cuaderno9-MCC225.ipynb
```

> Si acabas de ejecutar `pip install -e .`, reinicia el kernel antes de correr el cuaderno.


#### **18. Flujo recomendado final**


Dentro del contenedor:

```bash
cd /workspace/Semana4/Proyecto
pip install -r requirements-extra.txt
pip install -e .
bash scripts/run_local_pipeline.sh
```

Ese es el camino más corto y estable para validar que el proyecto funciona.

## Nota de ejecución corregida

Los scripts en `scripts/` agregan automáticamente la raíz del proyecto a `sys.path`, por lo que los imports como `from src.dataset_utils import load_metadata` funcionan al ejecutarlos desde un notebook o desde terminal con comandos como:

```bash
python scripts/02_build_embeddings.py --metadata-csv data/bootstrap_flickr30k/metadata.csv --output outputs/embeddings/bootstrap_embeddings.npz
```

También se actualizó `scripts/run_local_pipeline.sh` para exportar `PYTHONPATH` antes de ejecutar el pipeline completo.
