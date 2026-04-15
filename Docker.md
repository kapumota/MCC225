### Docker para MCC225 (Windows CPU + Linux CPU/GPU)

Guía práctica para construir y ejecutar el entorno reproducible del curso **MCC225** con un solo `Dockerfile` y **dos imágenes distintas**:

- **`mcc225_cpu`**: para usar en **Windows con Docker Desktop** y también en Linux cuando solo se quiera CPU.
- **`mcc225_gpu`**: para usar en **Linux con GPU NVIDIA**.

> **Criterio de uso de este documento**
>
> - En **Windows** se trabajará con **Docker Desktop** y **solo CPU**.
> - En la otra PC con **Linux** se quiere disponer de **dos variantes** del entorno: **CPU** y **GPU**.
> - En Linux, para la variante GPU, conviene usar el **Docker Engine del host** con **NVIDIA Container Toolkit**.
> - Si en Linux también está instalado Docker Desktop, conviene revisar el contexto activo y usar `default` para la ejecución con GPU.

#### 1. Estructura recomendada

```text
MCC225/
├── Dockerfile
├── requirements-base.txt
├── requirements-opcional.txt
├── Docker-mcc225.md
├── verificacion_entorno.ipynb
├── .dockerignore
└── Semana1/
    ├── Cuaderno1-MCC225.ipynb
    └── Actividad1-MCC225.md
```

#### 2. Qué hace este Dockerfile

El `Dockerfile` de este proyecto:

- usa `python:3.11-slim`
- copia `requirements-base.txt` y `requirements-opcional.txt`
- instala primero la base y luego, si corresponde, los paquetes opcionales
- instala `torch`, `torchvision` y `torchaudio` según el argumento `TORCH_FLAVOR`
- permite construir imagen para `cpu`, `cu118`, `cu121` o `cu124`
- descarga recursos de `nltk`
- descarga el modelo `es_core_news_sm` de `spaCy`
- configura `HF_HUB_ETAG_TIMEOUT=60` y `HF_HUB_DOWNLOAD_TIMEOUT=120`
- expone `JupyterLab` en el puerto `8899`

#### 3. Estrategia recomendada para este curso

En vez de reutilizar siempre el mismo tag `mcc225`, conviene usar **dos tags distintos** para evitar confusiones entre equipos:

- **`mcc225_cpu`**
- **`mcc225_gpu`**

Ventajas:

- evita sobrescribir una imagen con otra
- deja claro qué imagen corresponde a cada máquina
- simplifica el soporte cuando alguien comparte capturas o comandos
- permite que en Linux convivan las dos variantes al mismo tiempo

#### 4. Qué usar en cada sistema

##### 4.1 Windows

En **Windows** se usará **Docker Desktop** con imagen **CPU**:

- imagen recomendada: `mcc225_cpu`
- build con `TORCH_FLAVOR=cpu`
- ejecución **sin** `--gpus all`

##### 4.2 Linux

En **Linux** se recomienda tener ambas imágenes:

- `mcc225_cpu` para pruebas generales o equipos sin uso de GPU
- `mcc225_gpu` para prácticas que necesiten aceleración con NVIDIA

Para la variante GPU en Linux, usa el **daemon del host** y no dependas de `desktop-linux`.

#### 5. Variantes de PyTorch recomendadas

Recomendación práctica para este documento:

- **CPU**: `TORCH_FLAVOR=cpu`
- **GPU Linux NVIDIA**: `TORCH_FLAVOR=cu121`
- **Alternativa GPU**: `TORCH_FLAVOR=cu124`

`cu121` suele ser una buena opción por compatibilidad amplia. `cu124` puede usarse si tu host y tu flujo ya están alineados con esa variante.

#### 6. Construcción de imágenes

##### 6.1 Build base CPU

Útil para validar primero el entorno principal sin paquetes opcionales:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=false \
  -t mcc225_cpu .
```

##### 6.2 Build completa CPU

Esta es la build recomendada para **Windows con Docker Desktop** y también para Linux CPU:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cpu \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225_cpu .
```

##### 6.3 Build completa GPU para Linux

Variante recomendada:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cu121 \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225_gpu .
```

Si necesitas CUDA 12.4:

```bash
docker build --no-cache \
  --build-arg TORCH_FLAVOR=cu124 \
  --build-arg INSTALL_OPCIONAL=true \
  -t mcc225_gpu .
```

##### 6.4 Verificar imágenes construidas

Linux/macOS/Git Bash:

```bash
docker images | grep mcc225
```

PowerShell:

```powershell
docker images mcc225_cpu
docker images mcc225_gpu
```

#### 7. Ejecución del contenedor

##### 7.1 Windows PowerShell con Docker Desktop (CPU)

```powershell
docker run -it --rm `
  --name mcc225_cpu_container `
  -p 8899:8899 `
  -v "${PWD}:/workspace" `
  mcc225_cpu
```

##### 7.2 Windows CMD con Docker Desktop (CPU)

```bat
docker run -it --rm --name mcc225_cpu_container -p 8899:8899 -v %cd%:/workspace mcc225_cpu
```

##### 7.3 Linux/macOS/Git Bash (CPU)

```bash
docker run -it --rm \
  --name mcc225_cpu_container \
  -p 8899:8899 \
  -v "$(pwd)":/workspace \
  mcc225_cpu
```

##### 7.4 Linux con GPU NVIDIA

```bash
docker run -it --rm \
  --gpus all \
  --name mcc225_gpu_container \
  -p 8899:8899 \
  -v "$(pwd)":/workspace \
  mcc225_gpu
```

#### 8. Abrir JupyterLab

Al iniciar el contenedor, abre en el navegador:

```text
http://localhost:8899/lab
```

Si Jupyter muestra token, cópialo desde los logs del contenedor.

#### 9. Windows: pauta operativa recomendada

Para este curso, en Windows deja el flujo así:

1. instala Docker Desktop
2. verifica que esté usando **Linux containers**
3. verifica que el engine esté activo
4. construye solo la imagen `mcc225_cpu`
5. ejecuta el contenedor sin `--gpus all`

Comprobaciones útiles en Windows:

```powershell
docker version
docker info
wsl --status
```

#### 10. Linux: CPU y GPU en la misma PC

En Linux puedes tener **las dos imágenes a la vez**:

- `mcc225_cpu`
- `mcc225_gpu`

Eso permite:

- probar notebooks ligeros con CPU
- reservar GPU para prácticas de entrenamiento o inferencia pesada
- comparar `torch.cuda.is_available()` entre ambos entornos

#### 11. Requisitos para usar GPU en Linux

Para la variante GPU en Linux, el host necesita:

- una **GPU NVIDIA compatible**
- drivers NVIDIA correctamente instalados
- **NVIDIA Container Toolkit**
- ejecución del contenedor con `--gpus all`

##### 11.1 Prueba rápida del host Linux

Antes de usar `mcc225_gpu`, conviene validar el host con:

```bash
nvidia-smi
```

Luego prueba Docker + GPU:

```bash
docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi
```

##### 11.2 Si Linux también tiene Docker Desktop instalado

Comprueba el contexto:

```bash
docker context ls
```

Si aparece activo `desktop-linux`, cambia al daemon del host:

```bash
docker context use default
```

#### 12. Validación dentro del contenedor

En JupyterLab o en la terminal del contenedor:

```python
import torch
print("torch.__version__ =", torch.__version__)
print("torch.version.cuda =", torch.version.cuda)
print("torch.cuda.is_available() =", torch.cuda.is_available())
if torch.cuda.is_available():
    print("GPU =", torch.cuda.get_device_name(0))
else:
    print("Sin GPU visible en el contenedor")
```

También puedes usar una verificación corta:

```bash
python -c "import torch; print(torch.__version__); print('cuda:', torch.cuda.is_available()); print('count:', torch.cuda.device_count()); print(torch.cuda.get_device_name(0) if torch.cuda.is_available() else 'sin GPU')"
```

#### 13. Cuándo reconstruir la imagen

Sí debes reconstruir si cambias:

- `Dockerfile`
- `requirements-base.txt`
- `requirements-opcional.txt`
- `TORCH_FLAVOR`

No necesitas reconstruir si solo cambias:

- notebooks
- archivos `.py`
- archivos `.md`
- material montado con `-v ...:/workspace`

#### 14. Problemas comunes

##### 14.1 Docker Desktop no responde en Windows

Prueba:

```powershell
docker version
docker info
```

Si falla, abre Docker Desktop y verifica que el engine esté operativo.

##### 14.2 El puerto 8899 está ocupado

Usa otro puerto del host, por ejemplo `8900`:

Windows PowerShell:

```powershell
docker run -it --rm `
  --name mcc225_cpu_container `
  -p 8900:8899 `
  -v "${PWD}:/workspace" `
  mcc225_cpu
```

Linux:

```bash
docker run -it --rm -p 8900:8899 -v "$(pwd)":/workspace mcc225_cpu
```

Luego abre:

```text
http://localhost:8900/lab
```

##### 14.3 En Linux, `torch.cuda.is_available()` sigue en `False`

Revisa en este orden:

1. el host detecta la GPU con `nvidia-smi`
2. `docker run --rm --runtime=nvidia --gpus all ubuntu nvidia-smi` funciona
3. construiste `mcc225_gpu` con `TORCH_FLAVOR=cu121` o `cu124`
4. ejecutaste el contenedor con `--gpus all`
5. si usas Docker Desktop en Linux, cambiaste a `docker context use default`

##### 14.4 Se sobreescribió una imagen por reutilizar el mismo tag

Evítalo usando siempre:

- `mcc225_cpu`
- `mcc225_gpu`

En lugar de usar `mcc225` para todo.

#### 15. Comandos mínimos recomendados

##### 15.1 Windows con Docker Desktop (CPU)

```powershell
docker build --no-cache --build-arg TORCH_FLAVOR=cpu --build-arg INSTALL_OPCIONAL=true -t mcc225_cpu .
docker run -it --rm --name mcc225_cpu_container -p 8899:8899 -v "${PWD}:/workspace" mcc225_cpu
```

##### 15.2 Linux CPU

```bash
docker build --no-cache --build-arg TORCH_FLAVOR=cpu --build-arg INSTALL_OPCIONAL=true -t mcc225_cpu .
docker run -it --rm --name mcc225_cpu_container -p 8899:8899 -v "$(pwd)":/workspace mcc225_cpu
```

##### 15.3 Linux GPU

```bash
docker context use default
docker build --no-cache --build-arg TORCH_FLAVOR=cu121 --build-arg INSTALL_OPCIONAL=true -t mcc225_gpu .
docker run -it --rm --gpus all --name mcc225_gpu_container -p 8899:8899 -v "$(pwd)":/workspace mcc225_gpu
```

#### 16. Resumen final de la adaptación

La adaptación recomendada para `Docker-mcc225` queda así:

- **Windows + Docker Desktop**: documentar **solo CPU**
- **Linux**: documentar **CPU y GPU**
- usar **dos tags** distintos: `mcc225_cpu` y `mcc225_gpu`
- para **GPU en Linux**, usar **Docker Engine del host** + **NVIDIA Container Toolkit**
- mantener `TORCH_FLAVOR=cpu`, `cu121` y opcionalmente `cu124` según el escenario.
