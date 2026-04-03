### Instrucciones Docker para MCC225

Guía práctica para construir y ejecutar el entorno reproducible del curso con Docker usando la imagen **`mcc225`**.

> En este proyecto la carpeta del curso puede llamarse como prefieras, pero la **imagen Docker** se construirá con el nombre **`mcc225`**.

#### 1. Estructura recomendada

```text
MCC225/
├── Dockerfile
├── requirements-base.txt
├── requirements-opcional.txt
├── Docker.md
├── verificacion_entorno.ipynb
├── .dockerignore
└── Semana1/
    ├── Cuaderno1-MCC225.ipynb
    └── Actividad1-MCC225.md
```

#### 2. Qué hace este Dockerfile

El `Dockerfile` de este proyecto:

- Usa `python:3.11-slim`
- Copia `requirements-base.txt` y `requirements-opcional.txt`
- Instala primero la base y luego, si corresponde, los paquetes opcionales
- Instala **PyTorch** según el argumento `TORCH_FLAVOR`
- Permite elegir entre build **CPU** o build **CUDA** (`cpu`, `cu118`, `cu121`, `cu124`)
- Sescarga recursos de `nltk`
- Descarga el modelo `es_core_news_sm` de `spaCy`
- Expone `JupyterLab` en el puerto `8899`

#### 3. Requisitos cubiertos por el entorno

Este entorno está pensado para cubrir los paquetes principales del curso, incluyendo:

- `torch`, `torchvision`
- `timm`
- `scikit-learn`
- `pandas`
- `matplotlib`
- `transformers`
- `datasets`
- `peft`
- `sentence-transformers`
- `open_clip_torch`
- `diffusers`
- `faiss-cpu`
- `gradio`
- `streamlit`

#### 4. Cómo funciona CPU vs GPU

La elección de CPU o GPU tiene dos partes:

1. **Durante el build** eliges qué variante de PyTorch quieres instalar con `TORCH_FLAVOR`.
2. **Durante la ejecución** tu código Python decide si usa CUDA o CPU con:

```python
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
```

Eso permite trabajar así:

- **PC sin GPU**: construyes con `TORCH_FLAVOR=cpu` o incluso con una build CUDA que luego caiga a CPU.
- **PC con GPU NVIDIA**: construyes con `TORCH_FLAVOR=cu121` o `cu124` y ejecutas el contenedor con `--gpus all`.

#### 5. Construir la imagen con bash

##### 5.1 Entrar a la carpeta del proyecto

**Linux/macOS/Git Bash**

```bash
cd /ruta/a/MCC225
ls
```

Debes ver al menos:

```text
Dockerfile
requirements-base.txt
requirements-opcional.txt
```

##### 5.2 Construir primero solo la base en CPU

Conviene validar primero el entorno principal, sin paquetes opcionales:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=false \
  -t mcc225 .
```

##### 5.3 Construir la imagen completa en CPU

Si el paso anterior termina bien, construye base + opcional:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225 .
```

##### 5.4 Construir la imagen completa para GPU

Ejemplo con CUDA 12.1:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cu121 \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225 .
```

Ejemplo con CUDA 12.4:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cu124 \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225 .
```

##### 5.5 Verificar que la imagen exista

```bash
docker images | grep mcc225
```

#### 6. Ejecutar el contenedor desde bash

##### 6.1 Linux/macOS/Git Bash en CPU

```bash
docker run -it --rm \
  --name mcc225_container \
  -p 8899:8899 \
  -v "$(pwd)":/workspace \
  mcc225
```

##### 6.2 Linux/macOS/Git Bash en GPU

```bash
docker run -it --rm \
  --gpus all \
  --name mcc225_container \
  -p 8899:8899 \
  -v "$(pwd)":/workspace \
  mcc225
```

##### 6.3 Windows PowerShell en CPU

```powershell
docker run -it --rm `
  --name mcc225_container `
  -p 8899:8899 `
  -v "${PWD}:/workspace" `
  mcc225
```

##### 6.4 Windows PowerShell en GPU

```powershell
docker run -it --rm `
  --gpus all `
  --name mcc225_container `
  -p 8899:8899 `
  -v "${PWD}:/workspace" `
  mcc225
```

##### 6.5 Windows CMD en CPU

```bat
docker run -it --rm --name mcc225_container -p 8899:8899 -v %cd%:/workspace mcc225
```

##### 6.6 Windows CMD en GPU

```bat
docker run -it --rm --gpus all --name mcc225_container -p 8899:8899 -v %cd%:/workspace mcc225
```

#### 7. Abrir JupyterLab

Al iniciar el contenedor, abre en el navegador:

```text
http://localhost:8899/lab
```

Si Jupyter muestra token, cópialo desde los logs del contenedor.

#### 8. Paso a paso con Docker Desktop

##### 8.1 Construir la imagen

Abre Docker Desktop y usa la terminal integrada, o una terminal normal con Docker Desktop iniciado.

Primero valida la base en CPU:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=false \
  -t mcc225 .
```

Si termina bien, construye la imagen completa. Puedes elegir una de estas dos rutas:

**Ruta A. Imagen CPU**

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225 .
```

**Ruta B. Imagen GPU (CUDA 12.1)**

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cu121 \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225 .
```

##### 8.2 Ejecutar la imagen desde la interfaz

En **Images**, busca `mcc225` y pulsa **Run**.

Completa los campos así:

```text
Container name: mcc225-entorno
Host port: 8899
Container port: 8899
Host path: C:\Users\TU_USUARIO\Documents\MCC225
Container path: /workspace
Environment variables: dejar vacío
```

Si tu PC tiene GPU NVIDIA y Docker Desktop ya está configurado para usar GPU, activa la opción de GPU si aparece en la interfaz o ejecuta el contenedor desde terminal con `--gpus all`.

Notas:

- `mcc225` es el nombre de la imagen.
- `mcc225-entorno` es solo un ejemplo de nombre del contenedor.
- También puedes usar `mcc225_container` como nombre del contenedor.
- `8899` es el puerto sugerido para evitar conflictos con `8080`, `8888` y `8891`.

Después abre:

```text
http://localhost:8899/lab
```

#### 9. Cómo usar los dos archivos de requirements fuera de Docker

##### Opción A. Solo base

```bash
pip install -r requirements-base.txt
```

##### Opción B. Base + opcional

```bash
pip install -r requirements-base.txt
pip install -r requirements-opcional.txt
```

##### Opción C. En una sola línea

```bash
pip install -r requirements-base.txt -r requirements-opcional.txt
```

> Nota: PyTorch en este proyecto se instala desde el `Dockerfile` para poder elegir CPU o CUDA con `TORCH_FLAVOR`.

#### 10. Qué instala cada archivo

- `requirements-base.txt`: núcleo del entorno, ciencia de datos, PyTorch elegido desde el `Dockerfile`, NLP clásico y moderno, `transformers`, `datasets`, `evaluate`, `spaCy`, `NLTK` y utilidades generales.
- `requirements-opcional.txt`: retrieval, embeddings, PEFT, alignment ligero, multimodalidad, demos, `timm`, `streamlit` y servicios simples.

#### 11. Recomendación práctica

No construyas de una sola vez con los opcionales hasta confirmar que la base ya funciona.

El `Dockerfile` ya separa ambas fases con `INSTALL_OPCIONAL`, así que conviene aprovecharlo:

1. construye primero con `INSTALL_OPCIONAL=false`
2. si funciona, construye con `INSTALL_OPCIONAL=true`

Si la build base pasa y la build opcional falla, entonces el siguiente conflicto estará en `requirements-opcional.txt`, no en el entorno principal.

#### 12. Validar el entorno

Abre `verificacion_entorno.ipynb` en JupyterLab y ejecuta todas las celdas.

La validación debería comprobar, como mínimo:

- Versión de Python
- Imports principales
- Disponibilidad de `torch`
- Detección de `cuda` cuando corresponda
- Carga de tokenizer de Hugging Face
- Carga de un dataset pequeño
- Funcionamiento básico de spaCy y NLTK
- Imports de `sentence_transformers`, `peft`, `diffusers`, `open_clip_torch`, `faiss`, `gradio` y `streamlit`.

#### 13. Verificación rápida dentro del contenedor

```bash
python - <<'PY'
import torch
print("torch.__version__ =", torch.__version__)
print("torch.version.cuda =", torch.version.cuda)
print("torch.cuda.is_available() =", torch.cuda.is_available())
print("torch.backends.cuda.is_built() =", torch.backends.cuda.is_built())
if torch.cuda.is_available():
    print("GPU =", torch.cuda.get_device_name(0))
PY
```

#### 14. Problemas comunes

##### El build sigue fallando

Reconstruye sin caché para evitar reutilizar capas antiguas:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=false \
  -t mcc225 .
```

Si la build base funciona y la build completa falla, revisa entonces `requirements-opcional.txt`.

##### El puerto 8899 está ocupado

Usa otro puerto del host, por ejemplo `8900`:

```bash
docker run -it --rm -p 8900:8899 -v "$(pwd)":/workspace mcc225
```

En ese caso abre:

```text
http://localhost:8900/lab
```

##### spaCy no descarga el modelo

Dentro del contenedor:

```bash
python -m spacy download es_core_news_sm
```

##### Construiste una imagen GPU, pero sigue saliendo CPU

Revisa estas tres cosas:

1. que hayas construido con `TORCH_FLAVOR=cu121` o `cu124`
2. que al ejecutar uses `--gpus all`
3. que Docker Desktop, drivers NVIDIA y el runtime de GPU estén correctamente configurados en la PC host

##### Quieres eliminar el warning `JSONArgsRecommended`

No es obligatorio, pero se puede mejorar cambiando el `CMD` del `Dockerfile` a formato JSON.

#### 15. Comandos mínimos recomendados

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=false \
  -t mcc225 .

docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225 .

docker run -it --rm \
  --name mcc225_container \
  -p 8899:8899 \
  -v "$(pwd)":/workspace \
  mcc225
```
