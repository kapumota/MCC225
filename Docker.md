### Docker para MCC225

Guía práctica para construir y ejecutar el entorno reproducible del curso con Docker usando la imagen **`mcc225`**.

> En este proyecto la carpeta del curso puede tener cualquier nombre, pero la **imagen Docker** se construirá con el nombre **`mcc225`**.

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
- Instala `PyTorch`, `torchvision` y `torchaudio` desde el índice oficial de PyTorch según el argumento `TORCH_FLAVOR`
- Permite construir imagen para `cpu`, `cu118`, `cu121` o `cu124`
- Descarga recursos de `nltk`
- Descarga el modelo `es_core_news_sm` de `spaCy`
- Deja configurados `HF_HUB_ETAG_TIMEOUT=60` y `HF_HUB_DOWNLOAD_TIMEOUT=120`
- Expone `JupyterLab` en el puerto `8899`

#### 3. Importante: CPU o GPU

Este entorno permite dos estrategias:

##### 3.1 Build CPU

Si quieres una imagen CPU:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225 .
```

##### 3.2 Build GPU

Si quieres una imagen con soporte CUDA, elige una variante soportada por PyTorch 2.4.1.

###### CUDA 12.1

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cu121 \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225 .
```

##### CUDA 12.4

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cu124 \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225 .
```

#### 4. Construir la imagen paso a paso

##### 4.1 Entrar a la carpeta del proyecto

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

##### 4.2 Construir primero solo la base

Conviene validar primero el entorno principal, sin paquetes opcionales:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=false \
  -t mcc225 .
```

##### 4.3 Construir la imagen completa

Si el paso anterior termina bien, construye base + opcional:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225 .
```

Si quieres la variante GPU, cambia `TORCH_FLAVOR=cpu` por `cu121` o `cu124`.

##### 4.4 Verificar que la imagen exista

```bash
docker images | grep mcc225
```

En PowerShell puedes usar:

```powershell
docker images mcc225
```

#### 5. Ejecutar el contenedor desde terminal

##### 5.1 Linux/macOS/Git Bash

##### CPU

```bash
docker run -it --rm \
  --name mcc225_container \
  -p 8899:8899 \
  -v "$(pwd)":/workspace \
  mcc225
```

##### GPU

```bash
docker run -it --rm \
  --gpus all \
  --name mcc225_container \
  -p 8899:8899 \
  -v "$(pwd)":/workspace \
  mcc225
```

##### 5.2 Windows PowerShell

###### CPU

```powershell
docker run -it --rm `
  --name mcc225_container `
  -p 8899:8899 `
  -v "${PWD}:/workspace" `
  mcc225
```

##### GPU

```powershell
docker run -it --rm `
  --gpus all `
  --name mcc225_container `
  -p 8899:8899 `
  -v "${PWD}:/workspace" `
  mcc225
```

#### 5.3 Windows CMD

##### CPU

```bat
docker run -it --rm --name mcc225_container -p 8899:8899 -v %cd%:/workspace mcc225
```

##### GPU

```bat
docker run -it --rm --gpus all --name mcc225_container -p 8899:8899 -v %cd%:/workspace mcc225
```

#### 6. Abrir JupyterLab

Al iniciar el contenedor, abre en el navegador:

```text
http://localhost:8899/lab
```

Si Jupyter muestra token, cópialo desde los logs del contenedor.

#### 7. Paso a paso con Docker Desktop

##### 7.1 Antes de construir

Abre **Docker Desktop** y asegúrate de que:

- Docker Desktop esté iniciado
- el engine esté funcionando
- estés usando **Linux containers**

Si el comando `docker build` falla con un error de conexión al engine, normalmente significa que Docker Desktop no está iniciado o no está en modo Linux containers.

##### 7.2 Construir la imagen

Puedes usar la terminal integrada de Docker Desktop o una terminal normal con Docker Desktop ya iniciado.

Primero prueba la build base:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=false \
  -t mcc225 .
```

Si termina bien, construye la imagen completa:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225 .
```

Si quieres GPU, cambia `TORCH_FLAVOR=cpu` por `cu121` o `cu124`.

##### 7.3 Ejecutar la imagen desde la interfaz

En **Images**, busca `mcc225` y pulsa **Run**.

Completa los campos así:

```text
Container name: mcc225_container
Host port: 8899
Host path: C:\Users\TU_USUARIO\ruta\MCC225
Container path: /workspace
Environment variables: dejar vacío
```

Si quieres GPU y Docker Desktop ya tiene soporte NVIDIA habilitado, puedes ejecutar el contenedor desde terminal con `--gpus all`.

Después abre:

```text
http://localhost:8899/lab
```

#### 8. Qué instalan los requirements

##### `requirements-base.txt`

Incluye, entre otros:

- JupyterLab
- NumPy
- pandas
- SciPy
- scikit-learn
- matplotlib
- NLTK
- spaCy
- Transformers
- Datasets
- evaluate
- accelerate

##### `requirements-opcional.txt`

Incluye, entre otros:

- sentence-transformers
- FAISS CPU
- PEFT
- TRL
- OpenCLIP
- Diffusers
- timm
- Gradio
- Streamlit
- Plotly
- FastAPI
- Uvicorn

#### 9. Validar el entorno

Dentro de JupyterLab puedes probar:

```python
import torch
print("torch.__version__ =", torch.__version__)
print("torch.version.cuda =", torch.version.cuda)
print("torch.cuda.is_available() =", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU =", torch.cuda.get_device_name(0))
```

Para validar acceso a Hugging Face y `datasets`:

```python
import requests
from datasets import load_dataset

print("homepage:", requests.get("https://huggingface.co", timeout=30).status_code)
print("dataset api:", requests.get("https://huggingface.co/api/datasets/ag_news", timeout=30).status_code)

ds = load_dataset("ag_news", split="train[:5]")
print(ds)
print(ds[0])
```

#### 10. Cuándo debes reconstruir la imagen

##### Sí debes reconstruir la imagen si cambias:

- `Dockerfile`
- `requirements-base.txt`
- `requirements-opcional.txt`
- la versión de `TORCH_FLAVOR`

Ejemplo: si antes construiste con CPU y ahora quieres GPU, debes volver a construir.

##### No necesitas reconstruir la imagen si solo cambias:

- `Docker.md`
- notebooks
- archivos `.py`
- archivos de clase montados con `-v $(pwd):/workspace`

En esos casos basta con volver a ejecutar el contenedor, o incluso solo refrescar Jupyter si el contenedor sigue corriendo.

#### 11. Problemas comunes

##### El build falla porque Docker no responde

Prueba:

```bash
docker version
docker info
```

Si eso falla, abre Docker Desktop y verifica que esté activo.

##### El puerto 8899 está ocupado

Usa otro puerto del host, por ejemplo `8900`:

```bash
docker run -it --rm -p 8900:8899 -v "$(pwd)":/workspace mcc225
```

En ese caso abre:

```text
http://localhost:8900/lab
```

##### `torch.cuda.is_available()` sigue en `False`

Revisa lo siguiente:

1. Construiste la imagen con `TORCH_FLAVOR=cu121` o `cu124`
2. Ejecutaste el contenedor con `--gpus all`
3. La PC host realmente tiene GPU NVIDIA compatible
4. Docker Desktop tiene acceso a GPU

##### `datasets` o modelos de Hugging Face tardan demasiado

El `Dockerfile` ya deja configurado:

```text
HF_HUB_ETAG_TIMEOUT=60
HF_HUB_DOWNLOAD_TIMEOUT=120
```

Eso ayuda cuando la red es lenta o la respuesta del Hub tarda más que el valor por defecto.

#### 12. Comandos mínimos recomendados

##### Base CPU

```bash
docker build --no-cache --build-arg TORCH_FLAVOR=cpu --build-arg INSTALL_OPCIONAL=false -t mcc225 .
```

##### Completo CPU

```bash
docker build --no-cache --build-arg TORCH_FLAVOR=cpu --build-arg INSTALL_OPCIONAL=true -t mcc225 .
```

##### Completo GPU

```bash
docker build --no-cache --build-arg TORCH_FLAVOR=cu121 --build-arg INSTALL_OPCIONAL=true -t mcc225 .
```

##### Ejecutar CPU

```bash
docker run -it --rm --name mcc225_container -p 8899:8899 -v "$(pwd)":/workspace mcc225
```

##### Ejecutar GPU

```bash
docker run -it --rm --gpus all --name mcc225_container -p 8899:8899 -v "$(pwd)":/workspace mcc225
```
