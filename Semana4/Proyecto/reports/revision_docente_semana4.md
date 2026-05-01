# Revisión docente - Semana 4 / OpenCLIP

## Veredicto

El proyecto es suficiente como laboratorio reproducible de Semana 4 para introducir aprendizaje contrastivo, dual encoders, embeddings imagen-texto y recuperación cruzada. Con los cambios aplicados queda más adecuado como material docente, porque evita depender del dataset legacy `nlphuji/flickr30k` y usa un subconjunto Parquet más pequeño y manejable para clase.

## Correcciones y mejoras aplicadas

1. `scripts/01_prepare_flickr30k_from_hf.py`
   - El dataset remoto por defecto ahora es `Vishva007/Flickr-Dataset-1k`.
   - Se agregó alias para aceptar `Vishva007/Flickr-Dataset-1` y redirigirlo automáticamente a `Vishva007/Flickr-Dataset-1k`.
   - `trust_remote_code` ahora queda desactivado por defecto, porque este dataset está en Parquet y no requiere script remoto.
   - El directorio de salida por defecto cambió a `data/processed/flickr1k_hf`.
   - Se añadieron normalización de splits, manejo de columnas `caption` como lista, guardado de `all.csv`, `train.csv`, `val.csv` y `test.csv`, y fallback al bootstrap local si Hugging Face falla.

2. `src/dataset_utils.py`
   - Se robusteció la carga de metadata.
   - Se agregó `parse_captions` para captions en JSON, listas o texto plano.
   - Se agregó `explode_all_captions`, que permite evaluar correctamente datasets estilo Flickr con varias captions por imagen.

3. `scripts/02_build_embeddings.py`
   - Nuevo parámetro `--caption-mode {first,all}`.
   - En modo `all`, el script codifica todas las captions disponibles por imagen.
   - El `.npz` ahora guarda `image_ids`, `text_image_ids`, `text_captions`, `caption_mode` y ruta de metadata textual.

4. `src/metrics.py` y `scripts/03_eval_retrieval.py`
   - La evaluación ya no asume una matriz cuadrada 1:1.
   - Se implementó evaluación multi-positiva por `image_id`: una imagen se considera correcta si recupera cualquiera de sus captions válidas.
   - Se reportan `n_images`, `n_texts` y `caption_mode`.

5. `src/retrieval.py` y `scripts/05_mine_hard_negatives.py`
   - Los hard negatives excluyen positivos por `image_id`, no solo por diagonal.
   - Esto evita marcar como negativo otra caption válida de la misma imagen.

6. Scripts de ejecución
   - `scripts/run_local_pipeline.sh` usa el bootstrap local con `--caption-mode all`.
   - Se añadió `scripts/run_hf_flickr1k_pipeline.sh` para ejecutar la versión remota con `Vishva007/Flickr-Dataset-1k`.

7. `requirements-extra.txt`
   - Ya no se fija `datasets<4` por el problema legacy de `nlphuji/flickr30k`.
   - Se usa `datasets>=3.6.0,<5`, suficiente para datasets Parquet del Hub.

## Evaluación docente

La mejora más importante es pedagógica y metodológica: el laboratorio ahora separa el smoke test local del experimento remoto pequeño. Para una sesión síncrona, el bootstrap permite verificar entorno y flujo completo; para trabajo fuera de clase, `Vishva007/Flickr-Dataset-1k` permite evaluar recuperación de forma más realista sin descargar el Flickr30k completo.

## Recomendaciones restantes

1. Ampliar el bootstrap local de 6 a 30-60 imágenes para que las métricas de recuperación sean interpretables aun sin internet.
2. Añadir generación automática de figuras en `outputs/figures/` para ejemplos top-k y hard negatives.
3. Convertir `reports/reporte_proyecto.md` en una plantilla con tabla de métricas, análisis de errores y decisiones metodológicas.
4. Añadir smoke tests simples con `pytest` para metadata, shapes de embeddings y evaluación multi-caption.
5. Incluir una rúbrica breve para la entrega: reproducibilidad, evaluación, análisis de error y defensa oral.
