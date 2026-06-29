### Pol+itica de datos del repositorio MCC225

#### Principio general

Este repositorio versiona código, notebooks, lecturas, guias, rúbricas y fixtures pequeños. No versiona datasets completos ni artefactos generados por ejecución experimental.

#### Que si va en Git

- Notebooks y scripts docentes.
- Lecturas, actividades, rúbricas y guías.
- Fixtures mínimos necesarios para que un ejemplo pedágogico abra sin conexión, siempre que sean pequeños.
- Metadatos pequeños de referencia, por ejemplo archivos `.json`, `.jsonl`, `.csv` o `.md` usados como evidencia académica.

#### Qué no va en Git

- Imágenes masivas descargadas desde Hugging Face, Kaggle u otra fuente.
- Subconjuntos Flickr, carpetas `bootstrap_*`, carpetas `*_hf` y carpetas `flickr*` con imágenes.
- Embeddings, pesos, checkpoints, caches, logs y outputs regenerables.
- Resultados experimentales pesados que pueden obtenerse ejecutando un pipeline.

#### Regla operativa

Si una semana usa datos pesados, debe incluir un script de preparación local con nombre parecido a `01_prepare_*.py`. El estudiante clona el repositorio, instala dependencias y ejecuta ese script para descargar o regenerar los datos en su máquina.

#### Reproducibilidad mínima

Cada semana con datos debe indicar:

1. Fuente original de datos.
2. Script de preparación.
3. Semilla o criterio de muestreo si se usa subconjunto.
4. Rutas locales generadas.
5. Archivos que no deben comitearse.

#### Git LFS

Git LFS queda reservado para pocos binarios pequeños y deliberadamente versionados. No debe usarse para datasets completos de clase, porque el ancho de banda se consume cuando estudiantes hacen clone, pull o fork.
