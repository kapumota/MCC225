### Reporte interpretativo-Semana 5 MCC225

#### 1. Configuración experimental
- Dataset activo: `flickr1k_eval_300`.
- Modo de dataset: `expanded_retrieval_parquet_flickr1k`.
- Imágenes evaluadas: `300`.
- Captions evaluadas: `1500`.
- Modelo base: `ViT-B-32`.
- Checkpoint base: `laion2b_s34b_b79k`.
- Batch size: `32`.
- GPU: `NVIDIA GeForce RTX 4080 SUPER`.
- CUDA disponible: `True`.
- Registro de entorno: `outputs/metadata/environment_record.json`.

#### 2. Validez del subconjunto
El subconjunto contiene 300 imágenes y 1500 captions; supera el umbral mínimo de 100 imágenes, aunque sigue siendo una muestra acotada.

#### 3. Métricas de recuperación
| direction     |      R@1 |      R@5 |     R@10 |      MRR |   MeanRank |   MedianRank |
|:--------------|---------:|---------:|---------:|---------:|-----------:|-------------:|
| image_to_text | 0.903333 | 0.98     | 0.99     | 0.939221 |    1.54    |            1 |
| text_to_image | 0.79     | 0.952667 | 0.971333 | 0.860603 |    2.23533 |            1 |

##### Interpretación
- En image_to_text, R@1=0.903 y MRR=0.939, desempeño muy alto para 300 consultas evaluadas.
- En text_to_image, R@1=0.790 y MRR=0.861, desempeño moderado-alto para 1500 consultas evaluadas.

La lectura de `R@1` debe complementarse con `MRR` y con inspección cualitativa de resultados top-k. Un resultado alto en un subconjunto pequeño puede deberse a baja ambigüedad semántica, por ello se exige análisis de errores.

#### 4. Evaluación zero-shot
Modo: `demostracion_bootstrap`.

La evaluación zero-shot se considera demostrativa porque el subconjunto ampliado no contiene etiquetas cerradas compatibles.

| mode            | template                                          |   accuracy |   accuracy_pct |
|:----------------|:--------------------------------------------------|-----------:|---------------:|
| prompt_ensemble | a photo of {}; an image of {}; a caption about {} |   0.833333 |          83.33 |
| single_template | a photo of {}                                     |   0.833333 |          83.33 |
| single_template | an image of {}                                    |   0.833333 |          83.33 |
| single_template | a caption about {}                                |   0.833333 |          83.33 |

La matriz de confusión se guardó en `outputs/figures/zeroshot_confusion_demostracion_bootstrap.png`.

#### 5. Comparación de checkpoints
| tag              | model_name   | pretrained            |   i2t_R@1 |   i2t_MRR |   t2i_R@1 |   t2i_MRR |   zeroshot_ensemble_acc | status   |
|:-----------------|:-------------|:----------------------|----------:|----------:|----------:|----------:|------------------------:|:---------|
| vit_b32_laion2b  | ViT-B-32     | laion2b_s34b_b79k     |  0.903333 |  0.93922  |  0.79     |  0.860627 |                       0 | ok       |
| vit_b16_datacomp | ViT-B-16     | datacomp_xl_s13b_b90k |  0.92     |  0.952143 |  0.802667 |  0.870822 |                       0 | ok       |
| vit_l14_openai   | ViT-L-14     | openai                |  0.906667 |  0.946423 |  0.764    |  0.843814 |                       0 | ok       |

#### 6. Costo computacional por checkpoint
| nota                                                                                                         |   n_images |   n_captions | gpu_name                      | cuda_available   |
|:-------------------------------------------------------------------------------------------------------------|-----------:|-------------:|:------------------------------|:-----------------|
| Costo no medido en esta ejecución. Cambie MEASURE_CHECKPOINT_COST=True para registrar tiempo por checkpoint. |        300 |         1500 | NVIDIA GeForce RTX 4080 SUPER | True             |

Cuando el costo no se haya medido, el estudiante debe declararlo y no recomendar despliegue solo por accuracy o recall.

#### 7. Limitaciones
1. Flickr30k está orientado a recuperación imagen-texto, no toda evaluación zero-shot sobre este corpus es naturalmente cerrada.
2. Las métricas dependen del tamaño y diversidad del subconjunto.
3. Las captions múltiples mejoran la evaluación imagen->texto, pero también pueden introducir ambigüedad semántica.
4. Los resultados con OpenCLIP pueden variar por checkpoint, hardware y versión de librerías.
5. El fine-tuning debe tratarse como demostración operativa salvo que incluya diseño experimental completo.
