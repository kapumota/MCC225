### Bibliografía de Semana1

#### Criterio

Esta carpeta reemplaza los PDFs externos por referencias bibliográficas verificables.

Los PDFs de papers no se versionan directamente en Git. Cada trabajo debe consultarse desde fuentes oficiales como arXiv, DOI, página del congreso, revista, editorial o sitio institucional de los autores.

La Semana 1 funciona como entrada conceptual al curso MCC225. Por ello, los papers seleccionados no buscan profundizar todavía en un único modelo, sino construir el vocabulario mínimo del curso: modalidad, representación, alineamiento, fusión, captioning, VQA, tokens visuales y modelos visión-lenguaje.

#### Papers de referencia

| Referencia base | Título completo | Autores | Año | Fuente oficial | Uso en el curso | Estado |
|---|---|---|---:|---|---|---|
| Multimodal_ML_Survey | Multimodal Machine Learning: A Survey and Taxonomy | Tadas Baltrušaitis, Chaitanya Ahuja, Louis-Philippe Morency | 2017 | [arXiv](https://arxiv.org/abs/1705.09406) | Marco conceptual para representación, traducción, alineamiento, fusión y co-learning multimodal | Verificado |
| ViT | An Image Is Worth 16x16 Words: Transformers for Image Recognition at Scale | Alexey Dosovitskiy, Lucas Beyer, Alexander Kolesnikov, Dirk Weissenborn, Xiaohua Zhai, Thomas Unterthiner, Mostafa Dehghani, Matthias Minderer, Georg Heigold, Sylvain Gelly, Jakob Uszkoreit, Neil Houlsby | 2021 | [arXiv](https://arxiv.org/abs/2010.11929) | Introducción a imágenes como secuencias de patches y tokens visuales | Verificado |
| Visual_Semantic_Alignments | Deep Visual-Semantic Alignments for Generating Image Descriptions | Andrej Karpathy, Li Fei-Fei | 2015 | [CVF CVPR 2015](https://openaccess.thecvf.com/content_cvpr_2015/html/Karpathy_Deep_Visual-Semantic_Alignments_2015_CVPR_paper.html), [arXiv](https://arxiv.org/abs/1412.2306) | Alineamiento imagen-texto, embeddings multimodales y generación de descripciones | Verificado |
| Show_Attend_Tell | Show, Attend and Tell: Neural Image Caption Generation with Visual Attention | Kelvin Xu, Jimmy Ba, Ryan Kiros, Kyunghyun Cho, Aaron Courville, Ruslan Salakhutdinov, Richard Zemel, Yoshua Bengio | 2015 | [PMLR ICML 2015](https://proceedings.mlr.press/v37/xuc15.html), [arXiv](https://arxiv.org/abs/1502.03044) | Captioning con atención visual como puente entre visión, lenguaje y explicación | Verificado |
| VQA | VQA: Visual Question Answering | Stanislaw Antol, Aishwarya Agrawal, Jiasen Lu, Margaret Mitchell, Dhruv Batra, C. Lawrence Zitnick, Devi Parikh | 2015 | [CVF ICCV 2015](https://openaccess.thecvf.com/content_iccv_2015/html/Antol_VQA_Visual_Question_ICCV_2015_paper.html), [arXiv](https://arxiv.org/abs/1505.00468), [Sitio oficial](https://visualqa.org/) | Introducción a preguntas visuales, razonamiento sobre imágenes y evaluación de respuestas | Verificado |
| CLIP | Learning Transferable Visual Models From Natural Language Supervision | Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sastry, Amanda Askell, Pamela Mishkin, Jack Clark, Gretchen Krueger, Ilya Sutskever | 2021 | [PMLR ICML 2021](https://proceedings.mlr.press/v139/radford21a.html), [arXiv](https://arxiv.org/abs/2103.00020), [GitHub](https://github.com/openai/CLIP) | Intuición inicial de aprendizaje contrastivo imagen-texto, espacios semánticos compartidos y zero-shot | Verificado |
| BLIP | BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation | Junnan Li, Dongxu Li, Caiming Xiong, Steven Hoi | 2022 | [PMLR ICML 2022](https://proceedings.mlr.press/v162/li22n.html), [arXiv](https://arxiv.org/abs/2201.12086), [GitHub](https://github.com/salesforce/BLIP) | Preview de modelos visión-lenguaje unificados para captioning, retrieval y VQA | Verificado |

#### Nota para estudiantes

Antes de citar un trabajo, se debe verificar la referencia completa en la fuente oficial. Esta lista sirve como guía de lectura del curso y no reemplaza una ficha bibliográfica formal.

Para la Semana 1 no se espera dominar todos los detalles técnicos de cada paper. Se espera identificar qué problema introduce cada trabajo y cómo se conecta con los conceptos iniciales del curso.

#### Ruta sugerida de lectura

1. Leer Multimodal Machine Learning para entender la taxonomía general del campo.
2. Leer ViT para comprender por qué una imagen puede tratarse como una secuencia de tokens visuales.
3. Leer Deep Visual-Semantic Alignments para introducir alineamiento imagen-texto.
4. Leer Show, Attend and Tell para entender captioning con atención visual.
5. Leer VQA para reconocer la tarea de pregunta-respuesta visual.
6. Leer CLIP como primera aproximación al aprendizaje contrastivo imagen-texto.
7. Leer BLIP como preview de modelos visión-lenguaje unificados.

