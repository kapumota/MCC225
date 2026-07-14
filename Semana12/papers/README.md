### Bibliografía de Semana12

#### Criterio

Esta carpeta reemplaza los PDFs externos por referencias bibliográficas verificables.

Los PDFs de papers no se versionan directamente en Git. Cada trabajo debe consultarse desde fuentes oficiales como arXiv, DOI, página del congreso, revista, editorial o sitio institucional de los autores.

La Semana 12 se centra en audio-texto y video-texto. El foco está en representación temporal, sincronía audiovisual, alineamiento semántico y temporal, modelos omni y problemas específicos de evaluación multimodal temporal. Por ello, los trabajos seleccionados cubren aprendizaje contrastivo audio-texto, preentrenamiento video-audio-texto, grounding temporal, comprensión de secuencias largas, interacción multimodal en streaming, arquitecturas any-to-any y benchmarks orientados a medir orden, duración, movimiento, sincronía y dependencia real de cada modalidad.

#### Papers de referencia

| Referencia base | Título completo | Autores | Año | Fuente oficial | Uso en el curso | Estado |
|---|---|---|---:|---|---|---|
| CLAP | CLAP: Learning Audio Concepts From Natural Language Supervision | Benjamin Elizalde, Soham Deshmukh, Mahmoud Al Ismail, Huaming Wang | 2022 | [arXiv](https://arxiv.org/abs/2206.04769) | Fundamento de alineamiento contrastivo audio-texto para recuperación cruzada y clasificación zero-shot | Verificado |
| VATT | VATT: Transformers for Multimodal Self-Supervised Learning from Raw Video, Audio and Text | Hassan Akbari et al. | 2021 | [arXiv](https://arxiv.org/abs/2104.11178) | Preentrenamiento autosupervisado conjunto sobre video, audio y texto con Transformers y objetivos contrastivos | Verificado |
| MERLOT_Reserve | MERLOT Reserve: Neural Script Knowledge through Vision and Language and Sound | Rowan Zellers et al. | 2022 | [arXiv](https://arxiv.org/abs/2201.02639), [GitHub](https://github.com/rowanz/merlot_reserve) | Representación conjunta de video, audio y texto mediante segmentos temporales y predicción multimodal enmascarada | Verificado |
| Moment_DETR | QVHighlights: Detecting Moments and Highlights in Videos via Natural Language Queries | Jie Lei et al. | 2021 | [arXiv](https://arxiv.org/abs/2107.09609), [GitHub](https://github.com/jayleicn/moment_detr) | Grounding temporal de consultas textuales mediante localización de intervalos y estimación de saliencia | Verificado |
| ImageBind | ImageBind: One Embedding Space To Bind Them All | Rohit Girdhar, Alaaeldin El-Nouby, Zhuang Liu, Mannat Singh, Kalyan Vasudev Alwala, Armand Joulin, Ishan Misra | 2023 | [arXiv](https://arxiv.org/abs/2305.05665), [GitHub](https://github.com/facebookresearch/ImageBind) | Alineamiento de imagen, texto, audio, profundidad, información térmica e IMU en un espacio común | Verificado |
| InternVideo2 | InternVideo2: Scaling Foundation Models for Multimodal Video Understanding | Yi Wang et al. | 2024 | [arXiv](https://arxiv.org/abs/2403.15377), [GitHub](https://github.com/OpenGVLab/InternVideo) | Modelo fundacional de video que integra modelado enmascarado, contraste video-texto y generación autoregresiva | Verificado |
| Qwen2_5_Omni | Qwen2.5-Omni Technical Report | Jin Xu et al. | 2025 | [arXiv](https://arxiv.org/abs/2503.20215), [GitHub](https://github.com/QwenLM/Qwen2.5-Omni) | Modelo omni con entrada de texto, imagen, audio y video, salida de texto y voz, arquitectura Thinker-Talker, streaming y TMRoPE | Verificado |
| TemporalBench | TemporalBench: Benchmarking Fine-grained Temporal Understanding for Multimodal Video Models | Mu Cai et al. | 2024 | [arXiv](https://arxiv.org/abs/2410.10818), [GitHub](https://github.com/mu-cai/TemporalBench) | Evaluación de frecuencia, magnitud del movimiento, orden de eventos y sesgos de preguntas de opción múltiple | Verificado |
| Video_MME | Video-MME: The First-Ever Comprehensive Evaluation Benchmark of Multi-modal LLMs in Video Analysis | Chaoyou Fu et al. | 2024 | [arXiv](https://arxiv.org/abs/2405.21075), [GitHub](https://github.com/BradyFU/Video-MME) | Evaluación de videos cortos, medianos y largos, incluyendo comparaciones con audio y subtítulos | Verificado |
| AV_SyncBench | AV-SyncBench: Decoupled Benchmarking of Temporal and Semantic Audio-Visual Synchronization | Tianhong Zhou et al. | 2026 | [arXiv](https://arxiv.org/abs/2607.00726), [Proyecto](https://fgt7t6g.github.io/AV-SyncBench/) | Separación explícita entre correspondencia semántica y sincronización temporal de audio y video | Verificado |

#### Papers complementarios orientados al futuro

| Referencia base | Título completo | Autores | Año | Fuente oficial | Uso en el curso | Estado |
|---|---|---|---:|---|---|---|
| AudioCLIP | AudioCLIP: Extending CLIP to Image, Text and Audio | Andrey Guzhov, Federico Raue, Jörn Hees, Andreas Dengel | 2021 | [arXiv](https://arxiv.org/abs/2106.13043), [GitHub](https://github.com/AndreyGuzhov/AudioCLIP) | Extensión del aprendizaje contrastivo para alinear simultáneamente audio, imagen y texto | Complementario |
| mSLAM | mSLAM: Massively Multilingual Joint Pre-training for Speech and Text | Ankur Bapna et al. | 2022 | [arXiv](https://arxiv.org/abs/2202.01374) | Preentrenamiento conjunto multilingüe de voz y texto con señales autosupervisadas y supervisadas | Complementario |
| Audio_Flamingo_2 | Audio Flamingo 2: An Audio-Language Model with Long-Audio Understanding and Expert Reasoning Abilities | Sreyan Ghosh et al. | 2025 | [arXiv](https://arxiv.org/abs/2503.03983), [Proyecto](https://research.nvidia.com/labs/adlr/AF2/) | Comprensión y razonamiento sobre audio largo, incluyendo habla, música y sonidos ambientales | Complementario |
| Audio_Reasoner | Audio-Reasoner: Improving Reasoning Capability in Large Audio Language Models | Zhifei Xie, Mingbao Lin, Zihang Liu, Pengcheng Wu, Shuicheng Yan, Chunyan Miao | 2025 | [arXiv](https://arxiv.org/abs/2503.02318) | Entrenamiento explícito para razonamiento auditivo mediante datos con procesos estructurados de razonamiento | Complementario |
| TimeSformer | Is Space-Time Attention All You Need for Video Understanding? | Gedas Bertasius, Heng Wang, Lorenzo Torresani | 2021 | [arXiv](https://arxiv.org/abs/2102.05095), [GitHub](https://github.com/facebookresearch/TimeSformer) | Separación de atención espacial y temporal para representar secuencias de video | Complementario |
| VideoCLIP | VideoCLIP: Contrastive Pre-training for Zero-shot Video-Text Understanding | Hu Xu et al. | 2021 | [arXiv](https://arxiv.org/abs/2109.14084) | Alineamiento video-texto utilizando segmentos temporalmente solapados y negativos difíciles | Complementario |
| UniVTG | UniVTG: Towards Unified Video-Language Temporal Grounding | Kevin Qinghong Lin et al. | 2023 | [arXiv](https://arxiv.org/abs/2307.16715), [GitHub](https://github.com/showlab/UniVTG) | Unificación de recuperación de momentos, detección de segmentos destacados y resumen temporal | Complementario |
| LanguageBind | LanguageBind: Extending Video-Language Pretraining to N-modality by Language-based Semantic Alignment | Bin Zhu et al. | 2023 | [arXiv](https://arxiv.org/abs/2310.01852), [GitHub](https://github.com/PKU-YuanGroup/LanguageBind) | Uso del lenguaje como modalidad central para alinear video, audio, profundidad e infrarrojo | Complementario |
| NExT_GPT | NExT-GPT: Any-to-Any Multimodal LLM | Shengqiong Wu, Hao Fei, Leigang Qu, Wei Ji, Tat-Seng Chua | 2023 | [arXiv](https://arxiv.org/abs/2309.05519), [GitHub](https://github.com/NExT-GPT/NExT-GPT) | Arquitectura any-to-any que conecta un LLM con encoders, adaptadores y decodificadores multimodales | Complementario |
| AnyGPT | AnyGPT: Unified Multimodal LLM with Discrete Sequence Modeling | Jun Zhan et al. | 2024 | [arXiv](https://arxiv.org/abs/2402.12226), [GitHub](https://github.com/OpenMOSS/AnyGPT) | Representación unificada de texto, voz, imagen y música mediante secuencias discretas | Complementario |
| Moshi | Moshi: A Speech-Text Foundation Model for Real-Time Dialogue | Alexandre Défossez et al. | 2024 | [arXiv](https://arxiv.org/abs/2410.00037), [GitHub](https://github.com/kyutai-labs/moshi) | Diálogo voz-a-voz full-duplex con baja latencia, interrupciones y flujos paralelos de audio | Complementario |
| TempCompass | TempCompass: Do Video LLMs Really Understand Videos? | Shilong Liu et al. | 2024 | [arXiv](https://arxiv.org/abs/2403.00476), [GitHub](https://github.com/llyx97/TempCompass) | Evaluación contrafactual de dirección, velocidad, atributos y orden con apariencia visual semejante | Complementario |
| Know_Show | Know-Show: Benchmarking Video-Language Models on Spatio-Temporal Grounded Reasoning | Chinthani Sugandhika, Chen Li, Deepu Rajan, Basura Fernando | 2025 | [arXiv](https://arxiv.org/abs/2512.05513), [GitHub](https://github.com/LUNAProject22/Know-Show) | Evaluación conjunta de razonamiento y localización de la evidencia espacial y temporal | Complementario |
| AudioMarathon | AudioMarathon: A Comprehensive Benchmark for Long-Context Audio Understanding and Efficiency in Audio LLMs | Peize He et al. | 2025 | [arXiv](https://arxiv.org/abs/2510.07293) | Evaluación de audio largo, dependencias temporales, razonamiento multi-hop y eficiencia de inferencia | Complementario |
| Qwen3_5_Omni | Qwen3.5-Omni Technical Report | Qwen Team | 2026 | [arXiv](https://arxiv.org/abs/2604.15804) | Línea futura de modelos omni con contexto extenso, arquitectura MoE, interacción audiovisual y grounding temporal | Exploratorio |

#### Nota para estudiantes

Antes de citar un trabajo, se debe verificar la referencia completa en la fuente oficial. Esta lista sirve como guía de lectura del curso y no reemplaza una ficha bibliográfica formal.

La Semana 12 no se debe interpretar como una revisión separada de modelos de audio y modelos de video. El objetivo es comprender cómo se representan secuencias multimodales, cómo se alinean eventos con lenguaje, cómo se distingue correspondencia semántica de sincronía temporal y qué requisitos adicionales aparecen en los modelos omni y en los sistemas de streaming.

#### Ruta sugerida de lectura

1. Leer CLAP para comprender el alineamiento contrastivo entre audio y lenguaje.
2. Leer VATT y VideoCLIP para estudiar preentrenamiento conjunto y alineamiento video-texto.
3. Leer MERLOT Reserve para analizar la integración temporal de video, audio y texto.
4. Leer Moment-DETR y UniVTG para comprender grounding y localización de intervalos temporales.
5. Leer ImageBind y LanguageBind para comparar espacios compartidos y modalidades de enlace.
6. Leer InternVideo2 para estudiar modelos fundacionales orientados a comprensión de video.
7. Leer NExT-GPT y AnyGPT para comparar integración modular y tokenización multimodal unificada.
8. Leer Moshi y Qwen2.5-Omni para analizar interacción en streaming, voz-a-voz y sincronización audiovisual.
9. Leer TempCompass, TemporalBench y Video-MME para estudiar evaluación temporal y dependencia de modalidades.
10. Leer Audio Flamingo 2, Audio-Reasoner, Know-Show, AudioMarathon, AV-SyncBench y Qwen3.5-Omni como líneas orientadas al futuro.

#### Advertencia metodológica

Un modelo no demuestra comprensión temporal solo porque acepta audio o video. Debe verificarse si sus resultados dependen del orden, duración, movimiento, sincronía y evidencia contenida en diferentes momentos. Los experimentos deben reportar estrategia de muestreo, cantidad de frames, duración, frecuencia de audio, modalidades disponibles, presupuesto de tokens, latencia, métricas y errores representativos.

Un **modelo omni** tampoco debe evaluarse únicamente por la cantidad de modalidades que admite. Debe comprobarse qué modalidades procesa realmente, cuáles genera, cómo representa el tiempo compartido, cómo responde ante modalidades faltantes o contradictorias y si puede señalar la evidencia temporal que sustenta su respuesta.