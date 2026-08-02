### Herramientas de investigación para posgrado en Ciencia de la Computación

Este documento complementa el repositorio del curso **MCC225 (IA Generativa y Aprendizaje Multimodal)** con una guía de herramientas que todo estudiante de posgrado en Ciencia de la Computación debería conocer para realizar investigación: búsqueda de literatura, gestión bibliográfica, revisiones sistemáticas, resumen y lectura crítica de papers, escritura académica, reproducibilidad experimental, agentes de IA para investigación, y formación continua.

No es una lista exhaustiva ni una recomendación cerrada: es un punto de partida curado para orientar al estudiante que recién empieza un trabajo integrador, taller de investigación o tesis.


#### 1. Búsqueda y descubrimiento de papers

| Herramienta | Uso principal |
|---|---|
| [Google Scholar](https://scholar.google.com) | Búsqueda general, seguimiento de citas, alertas por autor/tema |
| [Semantic Scholar](https://www.semanticscholar.org) | Búsqueda semántica, TL;DR generado por IA, grafos de citación |
| [Connected Papers](https://www.connectedpapers.com) | Mapa visual de papers relacionados a partir de un artículo semilla |
| [arXiv](https://arxiv.org) / [arXiv Sanity](https://arxiv-sanity-lite.com) | Preprints en CS/ML/stat; arXiv Sanity añade filtrado y recomendación |
| [Papers with Code](https://paperswithcode.com) | Papers vinculados a implementaciones y benchmarks/leaderboards |
| [OpenAlex](https://openalex.org) | Base de datos abierta de metadatos académicos (sucesor de Microsoft Academic) |
| [DBLP](https://dblp.org) | Bibliografía especializada en ciencias de la computación |
| [ACM Digital Library](https://dl.acm.org) / [IEEE Xplore](https://ieeexplore.ieee.org) | Bibliotecas digitales de las principales sociedades profesionales de CS |
| [Elicit](https://elicit.com) | Búsqueda y extracción de datos de papers asistida por IA |
| [Consensus](https://consensus.app) | Búsqueda de evidencia científica con síntesis por IA |

#### 2. Gestión bibliográfica y anotación

| Herramienta | Uso principal |
|---|---|
| [Zotero](https://www.zotero.org) | Gestor bibliográfico libre, con complemento para Word/LibreOffice y sincronización |
| [BibTeX](https://www.bibtex.org) / [BetterBibTeX](https://retorque.re/zotero-better-bibtex/) | Formato estándar de referencias para LaTeX; integración con Zotero |
| [Mendeley](https://www.mendeley.com) | Gestor bibliográfico con red social académica |
| [Hypothesis](https://web.hypothes.is) | Anotación colaborativa de documentos web y PDF |

#### 3. Revisiones sistemáticas y mapeo de literatura

| Herramienta | Uso principal |
|---|---|
| [PRISMA](https://www.prisma-statement.org) | Estándar metodológico y diagrama de flujo para revisiones sistemáticas |
| [Rayyan](https://www.rayyan.ai) | Cribado colaborativo de artículos (screening) para revisiones sistemáticas |
| [Covidence](https://www.covidence.org) | Gestión de flujo completo de revisiones sistemáticas (cribado, extracción, riesgo de sesgo) |
| [ASReview](https://asreview.nl) | Cribado de literatura asistido por aprendizaje activo, de código abierto |
| [VOSviewer](https://www.vosviewer.com) / [CiteSpace](https://citespace.podia.com) | Análisis bibliométrico y visualización de mapas de coautoría/co-citación |

#### 4. Lectura crítica y resumen de papers

| Herramienta | Uso principal |
|---|---|
| [Claude](https://claude.ai) / [ChatGPT](https://chatgpt.com) / [Gemini](https://gemini.google.com) | Resumen, explicación de secciones técnicas, discusión de metodología (siempre contrastando con el texto original) |
| [NotebookLM](https://notebooklm.google) | Notas y preguntas ancladas a un conjunto de documentos propios (RAG sobre PDFs cargados) |
| [Scite.ai](https://scite.ai) | Contexto de citación: si un paper es citado de forma favorable, contradictoria o meramente mencionada |
| [Semantic Scholar TL;DR](https://www.semanticscholar.org) | Resúmenes automáticos de una línea por paper |
| Plantilla de lectura crítica propia | Preguntas guía: problema, hipótesis, método, amenazas a la validez, resultado, limitaciones declaradas y no declaradas |

> Recomendación metodológica: usar modelos de lenguaje para navegar y priorizar la literatura, nunca como sustituto de la lectura completa de las secciones de método y limitaciones, especialmente en trabajos que se van a citar o replicar.

#### 5. Escritura académica y comunicación

| Herramienta | Uso principal |
|---|---|
| [Overleaf](https://www.overleaf.com) | Edición colaborativa de LaTeX en línea |
| [LaTeX Templates - Springer/IEEE/ACM](https://www.overleaf.com/latex/templates) | Plantillas de formato para conferencias/revistas |
| [Grammarly](https://www.grammarly.com) / [LanguageTool](https://languagetool.org) | Corrección gramatical y de estilo en inglés/español |
| [Excalidraw](https://excalidraw.com) / [draw.io](https://draw.io) | Diagramas de arquitectura y flujo para papers y presentaciones |
| [Quarto](https://quarto.org) | Publicación reproducible (notebooks, papers, slides) desde código |

#### 6. Reproducibilidad experimental y gestión de datos

| Herramienta | Uso principal |
|---|---|
| [Git](https://git-scm.com) / [GitHub](https://github.com) / [GitLab](https://gitlab.com) | Control de versiones y colaboración en código |
| [DVC](https://dvc.org) | Versionado de datasets y modelos grandes junto al código |
| [Weights & Biases](https://wandb.ai) / [MLflow](https://mlflow.org) | Seguimiento de experimentos, métricas e hiperparámetros |
| [Docker](https://www.docker.com) | Entornos reproducibles (ya usado en este repositorio, ver `Docker.md`) |
| [Hugging Face Hub](https://huggingface.co) | Alojamiento y versionado de modelos, datasets y demos |
| [Papers with Code - Reproducibility Checklist](https://paperswithcode.com) | Lista de verificación para reportar resultados reproducibles |

#### 7. Agentes de IA y automatización de investigación

| Herramienta | Uso principal |
|---|---|
| [Claude Code](https://claude.com/claude-code) | Agente de codificación para exploración de repositorios, refactorización y prototipado experimental |
| [Perplexity](https://www.perplexity.ai) | Búsqueda conversacional con citación de fuentes en tiempo real |
| [OpenAI Deep Research](https://openai.com) / [Gemini Deep Research](https://gemini.google.com) | Investigación autónoma multi-paso con síntesis de fuentes |
| [LangChain](https://www.langchain.com) / [LlamaIndex](https://www.llamaindex.ai) | Frameworks para construir pipelines RAG y agentes sobre literatura propia |
| [AutoGen](https://microsoft.github.io/autogen/) / [CrewAI](https://www.crewai.com) | Orquestación de agentes múltiples para tareas de investigación compuestas |
| [Model Context Protocol (MCP)](https://modelcontextprotocol.io) | Estándar abierto para conectar agentes de IA con herramientas y fuentes de datos |

> Uso responsable: todo resultado generado por agentes de IA (resúmenes, código, cifras) debe verificarse contra la fuente primaria antes de citarse o incluirse en un entregable académico.

#### 8. Cómputo y experimentación (ya cubiertos en este repositorio)

Ver la sección **"5. Herramientas y entorno de trabajo"** del README principal del curso para el stack usado en MCC225 (Python, PyTorch, Hugging Face, PEFT, OpenCLIP, Diffusers, FAISS, Gradio/Streamlit, Docker). Complementarios para investigación más amplia:

| Herramienta | Uso principal |
|---|---|
| [Google Colab](https://colab.research.google.com) / [Kaggle Notebooks](https://www.kaggle.com/code) | Cómputo GPU gratuito/económico para prototipado |
| [Papers with Code - Datasets](https://paperswithcode.com/datasets) | Catálogo de datasets por tarea |
| [Hugging Face Spaces](https://huggingface.co/spaces) | Demos públicas de modelos y prototipos |

#### 9. Formación continua (cursos y material de referencia)

| Recurso | Enfoque |
|---|---|
| [CS231n (Stanford)](http://cs231n.stanford.edu) | Redes neuronales convolucionales para visión por computadora |
| [CS224n (Stanford)](https://web.stanford.edu/class/cs224n/) | Procesamiento de lenguaje natural con deep learning |
| [Full Stack Deep Learning](https://fullstackdeeplearning.com) | De prototipo a sistema de producción con ML |
| [Hugging Face Course](https://huggingface.co/learn) | Transformers, difusión, RL, agentes - con notebooks ejecutables |
| [Fast.ai](https://www.fast.ai) | Deep learning práctico, top-down |
| [Papers We Love](https://paperswelove.org) | Comunidad y repositorio de discusión de papers clásicos y recientes |
| [Distill.pub (archivo)](https://distill.pub) | Explicaciones visuales e interactivas de conceptos de ML (archivado, pero vigente como referencia) |

#### 10. Buenas prácticas sugeridas para el estudiante de posgrado

1. Mantener un **gestor bibliográfico único** (Zotero recomendado) desde el primer semestre, no solo durante la tesis.
2. Registrar cada revisión de literatura con una **estrategia de búsqueda documentada** (cadenas de búsqueda, bases consultadas, fecha), aun si no es una revisión sistemática formal - facilita defender la cobertura ante un jurado.
3. Usar agentes de IA para **acelerar el cribado y la síntesis**, no para reemplazar la lectura crítica de método y limitaciones.
4. Versionar código y datos desde el primer experimento (Git + DVC/W&B), no al final del proyecto.
5. Documentar el entorno computacional (requirements, Dockerfile) para que cualquier resultado reportado sea reproducible por terceros.

