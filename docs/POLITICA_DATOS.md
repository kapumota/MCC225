### Politica de datos del repositorio MCC225

#### Principio general

Este repositorio versiona codigo, notebooks, lecturas, guias, rubricas y fixtures pequenos. No versiona datasets completos ni artefactos generados por ejecucion experimental.

#### Que si va en Git

- Notebooks y scripts docentes.
- Lecturas, actividades, rubricas y guias.
- Fixtures minimos necesarios para que un ejemplo pedagogico abra sin conexion, siempre que sean pequenos.
- Metadatos pequenos de referencia, por ejemplo archivos `.json`, `.jsonl`, `.csv` o `.md` usados como evidencia academica.

#### Que no va en Git

- Imagenes masivas descargadas desde Hugging Face, Kaggle u otra fuente.
- Subconjuntos Flickr, carpetas `bootstrap_*`, carpetas `*_hf` y carpetas `flickr*` con imagenes.
- Embeddings, pesos, checkpoints, caches, logs y outputs regenerables.
- Resultados experimentales pesados que pueden obtenerse ejecutando un pipeline.

#### Regla operativa

Si una semana usa datos pesados, debe incluir un script de preparacion local con nombre parecido a `01_prepare_*.py`. El estudiante clona el repositorio, instala dependencias y ejecuta ese script para descargar o regenerar los datos en su maquina.

#### Reproducibilidad minima

Cada semana con datos debe indicar:

1. Fuente original de datos.
2. Script de preparacion.
3. Semilla o criterio de muestreo si se usa subconjunto.
4. Rutas locales generadas.
5. Archivos que no deben comitearse.

#### Git LFS

Git LFS queda reservado para pocos binarios pequenos y deliberadamente versionados. No debe usarse para datasets completos de clase, porque el ancho de banda se consume cuando estudiantes hacen clone, pull o fork.
