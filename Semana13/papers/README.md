### Bibliografía de Semana13

#### Criterio

Esta carpeta reemplaza los PDFs externos por referencias bibliográficas verificables.

Los PDFs de papers no se versionan directamente en Git. Cada trabajo debe consultarse desde fuentes oficiales como arXiv, DOI, página del congreso, revista, editorial o sitio institucional de los autores.

La Semana 13 se centra en agentes multimodales y seguridad multimodal. El foco está en arquitecturas agénticas, planificación y ejecución, uso de herramientas, memoria, recuperación, interacción con interfaces visuales, riesgos de inyección directa e indirecta, ataques mediante imágenes o datos recuperados, seguridad de LLMs y MLLMs, controles de autorización, evaluación adversarial y uso responsable. Por ello, los trabajos seleccionados cubren razonamiento y acción, tool use, memoria jerárquica, recuperación aumentada, agentes multimodales, uso de cálculo, inyección de prompts, seguridad de herramientas, benchmarks de agentes, **guard models**, fine-tuning seguro y líneas recientes de seguridad para MCP y sistemas agénticos persistentes.

#### Papers de referencia

| Referencia base | Título completo | Autores | Año | Fuente oficial | Uso en el curso | Estado |
|---|---|---|---:|---|---|---|
| ReAct | ReAct: Synergizing Reasoning and Acting in Language Models | Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao | 2022 | [arXiv](https://arxiv.org/abs/2210.03629), [Proyecto](https://react-lm.github.io/) | Arquitectura base para intercalar razonamiento, observación y acciones sobre herramientas o entornos externos | Verificado |
| Toolformer | Toolformer: Language Models Can Teach Themselves to Use Tools | Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, Thomas Scialom | 2023 | [arXiv](https://arxiv.org/abs/2302.04761) | Aprendizaje autosupervisado para decidir qué herramienta invocar, cuándo utilizarla, qué argumentos proporcionar y cómo integrar el resultado | Verificado |
| RAG | Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks | Patrick Lewis et al. | 2020 | [arXiv](https://arxiv.org/abs/2005.11401) | Fundamento de recuperación externa como memoria no paramétrica y fuente de evidencia para agentes | Verificado |
| MemGPT | MemGPT: Towards LLMs as Operating Systems | Charles Packer, Sarah Wooders, Kevin Lin, Vivian Fang, Shishir G. Patil, Ion Stoica, Joseph E. Gonzalez | 2023 | [arXiv](https://arxiv.org/abs/2310.08560), [GitHub](https://github.com/letta-ai/letta) | Gestión jerárquica de memoria y contexto virtual para conversaciones prolongadas y documentos extensos | Verificado |
| MM_REACT | MM-REACT: Prompting ChatGPT for Multimodal Reasoning and Action | Zhengyuan Yang et al. | 2023 | [arXiv](https://arxiv.org/abs/2303.11381), [Proyecto](https://multimodal-react.github.io/) | Paradigma de agente multimodal que coordina un modelo de lenguaje con herramientas y expertos visuales | Verificado |
| LLaVA_Plus | LLaVA-Plus: Learning to Use Tools for Creating Multimodal Agents | Shilong Liu et al. | 2023 | [arXiv](https://arxiv.org/abs/2311.05437) | Agente multimodal con repositorio de habilidades para comprensión visual, generación, recuperación y composición de herramientas | Verificado |
| VisualWebArena | VisualWebArena: Evaluating Multimodal Agents on Realistic Visual Web Tasks | Jing Yu Koh et al. | 2024 | [arXiv](https://arxiv.org/abs/2401.13649), [Proyecto](https://jykoh.com/vwa) | Evaluación de agentes web que deben interpretar texto, imágenes e interfaces y ejecutar acciones verificables | Verificado |
| OSWorld | OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments | Tianbao Xie et al. | 2024 | [arXiv](https://arxiv.org/abs/2404.07972), [GitHub](https://github.com/xlang-ai/OSWorld), [Proyecto](https://os-world.github.io/) | Evaluación reproducible de agentes multimodales sobre aplicaciones reales, sistemas operativos y flujos entre múltiples herramientas | Verificado |
| Indirect_Prompt_Injection | Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection | Kai Greshake, Sahar Abdelnabi, Shailesh Mishra, Christoph Endres, Thorsten Holz, Mario Fritz | 2023 | [arXiv](https://arxiv.org/abs/2302.12173) | Fundamento de la inyección indirecta mediante páginas, documentos, correos y contenidos recuperados por aplicaciones integradas con LLMs | Verificado |
| AgentDojo | AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents | Edoardo Debenedetti, Jie Zhang, Mislav Balunović, Luca Beurer-Kellner, Marc Fischer, Florian Tramèr | 2024 | [arXiv](https://arxiv.org/abs/2406.13352), [GitHub](https://github.com/ethz-spylab/agentdojo) | Entorno dinámico para evaluar utilidad, ataques de prompt injection y defensas en agentes con herramientas y datos no confiables | Verificado |
| MM_SafetyBench | MM-SafetyBench: A Benchmark for Safety Evaluation of Multimodal Large Language Models | Xin Liu, Yichen Zhu, Jindong Gu, Yunshi Lan, Chao Yang, Yu Qiao | 2023 | [arXiv](https://arxiv.org/abs/2311.17600), [GitHub](https://github.com/isXinLiu/MM-SafetyBench) | Evaluación de instrucciones dañinas transferidas o encubiertas mediante imágenes en modelos multimodales | Verificado |
| Llama_Guard_3_Vision | Llama Guard 3 Vision: Safeguarding Human-AI Image Understanding Conversations | Jianfeng Chi et al. | 2024 | [arXiv](https://arxiv.org/abs/2411.10414) | Modelo de control para clasificar entradas multimodales y respuestas textuales según categorías de seguridad | Verificado |

#### Papers complementarios orientados al futuro

| Referencia base | Título completo | Autores | Año | Fuente oficial | Uso en el curso | Estado |
|---|---|---|---:|---|---|---|
| AutoGen | AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation | Qingyun Wu et al. | 2023 | [arXiv](https://arxiv.org/abs/2308.08155), [GitHub](https://github.com/microsoft/autogen) | Orquestación de sistemas multiagente con modelos, herramientas, código y participación humana | Complementario |
| Magma | Magma: A Foundation Model for Multimodal AI Agents | Jianwei Yang et al. | 2025 | [arXiv](https://arxiv.org/abs/2502.13130), [Proyecto](https://microsoft.github.io/Magma/) | Modelo fundacional para agentes multimodales en entornos digitales y físicos, con grounding de acciones y planificación espacio-temporal | Complementario |
| ToolEmu | Identifying the Risks of LM Agents with an LM-Emulated Sandbox | Yangjun Ruan et al. | 2023 | [arXiv](https://arxiv.org/abs/2309.15817) | Emulación de herramientas y escenarios de alto riesgo para descubrir fallos sin ejecutar acciones reales sobre sistemas productivos | Complementario |
| InjecAgent | InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents | Qiusi Zhan, Zhixiang Liang, Zifan Ying, Daniel Kang | 2024 | [arXiv](https://arxiv.org/abs/2403.02691), [GitHub](https://github.com/uiuc-kang-lab/InjecAgent) | Evaluación de inyección indirecta, exfiltración de información y acciones perjudiciales en agentes integrados con herramientas | Complementario |
| R_Judge | R-Judge: Benchmarking Safety Risk Awareness for LLM Agents | Tongxin Yuan et al. | 2024 | [arXiv](https://arxiv.org/abs/2401.10019), [GitHub](https://github.com/Lordog/R-Judge) | Medición de la capacidad de identificar riesgos a partir de trayectorias completas de interacción agéntica | Complementario |
| Agent_Security_Bench | Agent Security Bench: Formalizing and Benchmarking Attacks and Defenses in LLM-Based Agents | Hanrong Zhang et al. | 2024 | [arXiv](https://arxiv.org/abs/2410.02644), [GitHub](https://github.com/agiresearch/ASB) | Evaluación integral de ataques y defensas sobre prompts, herramientas, planes, memoria y recuperación | Complementario |
| FigStep | FigStep: Jailbreaking Large Vision-Language Models via Typographic Visual Prompts | Yichen Gong et al. | 2023 | [arXiv](https://arxiv.org/abs/2311.05608), [GitHub](https://github.com/ThuCCSLab/FigStep) | Ataque multimodal que traslada instrucciones problemáticas desde texto hacia contenido tipográfico dentro de imágenes | Complementario |
| Visual_Adversarial_Jailbreak | Visual Adversarial Examples Jailbreak Aligned Large Language Models | Xiangyu Qi, Kaixuan Huang, Ashwinee Panda, Peter Henderson, Mengdi Wang, Prateek Mittal | 2023 | [arXiv](https://arxiv.org/abs/2306.13213) | Análisis de imágenes adversariales capaces de controlar modelos visión-lenguaje y eludir alineamiento textual | Complementario |
| HADES | Images Are Achilles' Heel of Alignment: Exploiting Visual Vulnerabilities for Jailbreaking Multimodal Large Language Models | Yifan Li, Hangyu Guo, Kun Zhou, Wayne Xin Zhao, Ji-Rong Wen | 2024 | [arXiv](https://arxiv.org/abs/2403.09792), [GitHub](https://github.com/RUCAIBox/HADES) | Estudio de vulnerabilidades de alineamiento causadas por la combinación adversarial de texto e imágenes | Complementario |
| VLGuard | Safety Fine-Tuning at Almost No Cost: A Baseline for Vision Large Language Models | Yongshuo Zong, Ondrej Bohdal, Tingyang Yu, Yongxin Yang, Timothy Hospedales | 2024 | [arXiv](https://arxiv.org/abs/2402.02207), [GitHub](https://github.com/ys-zong/VLGuard) | Dataset y estrategia de safety fine-tuning para conservar utilidad y reducir respuestas inseguras en modelos visión-lenguaje | Complementario |
| MLLMGuard | MLLMGuard: A Multi-Dimensional Safety Evaluation Suite for Multimodal Large Language Models | Tianle Gu et al. | 2024 | [arXiv](https://arxiv.org/abs/2406.07594) | Evaluación multidimensional de privacidad, sesgo, toxicidad, veracidad y legalidad con ejemplos bilingües de imagen y texto | Complementario |
| Constitutional_AI | Constitutional AI: Harmlessness from AI Feedback | Yuntao Bai et al. | 2022 | [arXiv](https://arxiv.org/abs/2212.08073) | Uso de principios explícitos, autocrítica y retroalimentación de IA para orientar comportamientos responsables | Complementario |
| USB | USB: A Comprehensive and Unified Safety Evaluation Benchmark for Multimodal Large Language Models | Baolin Zheng et al. | 2025 | [arXiv](https://arxiv.org/abs/2505.23793) | Evaluación conjunta de vulnerabilidad, sobrerrechazo, categorías de riesgo y combinaciones de modalidades | Complementario |
| MCP_Security_Bench | MCP Security Bench: Benchmarking Attacks Against Model Context Protocol in LLM Agents | Dongsen Zhang, Zekun Li, Xu Luo, Xuannan Liu, Peipei Li, Wenjun Xu | 2025 | [arXiv](https://arxiv.org/abs/2510.15994) | Evaluación de ataques sobre planificación, descubrimiento de herramientas, descripciones, invocación y respuestas en agentes MCP | Exploratorio |
| Secure_LLM_Agents | Toward Secure LLM Agents: Threat Surfaces, Attacks, Defenses, and Evaluation | Yuchen Ling, Shengcheng Yu, Zhenyu Chen, Chunrong Fang | 2026 | [arXiv](https://arxiv.org/abs/2606.10749) | Visión de futuro sobre límites de confianza, autoridad delegada, estado persistente, procedencia, ataques y defensas componibles | Exploratorio |

#### Nota para estudiantes

Antes de citar un trabajo, se debe verificar la referencia completa en la fuente oficial. Esta lista sirve como guía de lectura del curso y no reemplaza una ficha bibliográfica formal.

La Semana 13 no se debe interpretar como una introducción exclusiva a frameworks de agentes. El objetivo es comprender qué convierte a un sistema en agéntico, cómo usa herramientas, memoria y recuperación, qué autoridad recibe, qué datos considera confiables, qué acciones puede ejecutar y qué riesgos aparecen cuando texto, imágenes, documentos, páginas web, correos o resultados de herramientas contienen instrucciones adversariales.

#### Ruta sugerida de lectura

1. Leer ReAct para comprender el ciclo de razonamiento, acción y observación.
2. Leer Toolformer para estudiar selección e invocación de herramientas.
3. Leer RAG y MemGPT para diferenciar recuperación externa, memoria de trabajo y memoria persistente.
4. Leer MM-REACT y LLaVA-Plus para analizar agentes que coordinan lenguaje, percepción visual y herramientas.
5. Leer VisualWebArena y OSWorld para estudiar evaluación de agentes web y computer-use mediante estados y resultados verificables.
6. Leer el trabajo de **indirect prompt injection** para comprender la separación incompleta entre datos e instrucciones.
7. Leer ToolEmu, InjecAgent y AgentDojo para comparar evaluación en sandbox, ataques indirectos y defensas adaptativas.
8. Leer MM-SafetyBench, FigStep, HADES y MLLMGuard para estudiar ataques, jailbreaks y evaluación de seguridad multimodal.
9. Leer VLGuard, Llama Guard 3 Vision y Constitutional AI para comparar controles basados en entrenamiento, guard models y principios.
10. Leer Agent Security Bench, Magma, USB, MCP Security Bench y Toward Secure LLM Agents como líneas orientadas al futuro.

#### Advertencia metodológica

Un agente no debe evaluarse solo por completar una tarea en una demostración. Debe reportarse la arquitectura, modelo, herramientas disponibles, permisos, memoria, recuperación, datos externos, estrategia de planificación, cantidad de pasos, costo, latencia, tasa de éxito, acciones incorrectas y condiciones de recuperación ante fallos.

La seguridad agéntica tampoco debe reducirse a comprobar si el modelo rechaza una pregunta problemática. Deben evaluarse datos no confiables, inyección indirecta, descripciones maliciosas de herramientas, exfiltración, uso excesivo de permisos, envenenamiento de memoria, recuperación contaminada, acciones irreversibles, propagación entre agentes y manipulación mediante imágenes.

Los experimentos de seguridad deben ejecutarse en entornos aislados, con herramientas simuladas o cuentas de prueba, límites de gasto, privilegio mínimo, listas explícitas de acciones permitidas, confirmación humana para operaciones sensibles, registros de auditoría y mecanismos de detención.

Una defensa tampoco debe considerarse efectiva únicamente porque reduce la tasa de ataque. Debe medirse su impacto sobre la utilidad, los falsos positivos, el sobrerrechazo, la latencia, el costo, la transferencia entre modelos y su resistencia frente a ataques adaptativos.