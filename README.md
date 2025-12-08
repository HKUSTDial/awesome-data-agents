
<h1 align="center">🌟 Awesome Data Agents 🌟</h1>
<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) 
[![arXiv](https://img.shields.io/badge/arXiv-2510.23587-b31b1b.svg?style=flat)](https://arxiv.org/abs/2510.23587)


</div>

> [!NOTE]
> Curated papers and resources on **Data Agents**. Companion repo and paper list for our survey on data agents - *A Survey of Data Agents: Emerging Paradigm or Overstated Hype?* [[Paper]](reports/Data_Agents_Survey.pdf)
>
> We also release slides for a recent talk (Chinese): [[Slides]](slides/从智能问数到数据智能体：范式演进与反思.pdf)
>
> If you find our work useful or inspiring, please kindly give us a star ⭐️ and cite our survey:

```bibtex
@misc{zhu2025surveydataagentsemerging,
      title={A Survey of Data Agents: Emerging Paradigm or Overstated Hype?}, 
      author={Yizhang Zhu and Liangwei Wang and Chenyu Yang and Xiaotian Lin and Boyan Li and Wei Zhou and Xinyu Liu and Zhangyang Peng and Tianqi Luo and Yu Li and Chengliang Chai and Chong Chen and Shimin Di and Ju Fan and Ji Sun and Nan Tang and Fugee Tsung and Jiannan Wang and Chenglin Wu and Yanwei Xu and Shaolei Zhang and Yong Zhang and Xuanhe Zhou and Guoliang Li and Yuyu Luo},
      year={2025},
      eprint={2510.23587},
      archivePrefix={arXiv},
      primaryClass={cs.DB},
      url={https://arxiv.org/abs/2510.23587}, 
}
```

## Contents

- [🎯 Introduction](#introduction)
- [🪜 Levels of Data Agents](#levels-of-data-agents) 
- [📑 Paper List](#paper-list)
  - [💬 L0-L1: From Manual Labor to Preliminary Assistance](#-l0-l1-from-manual-labor-to-preliminary-assistance)
    - [Data Management](#data-management)
    - [Data Preparation](#data-preparation)
    - [Data Analysis](#data-analysis)
    - [Comparison of L1 Data Agents](#comparison-of-l1-data-agents)
  - [🌏 L2: Perceive the Environment](#-l2-perceive-the-environment)
    - [Data Management](#data-management-1)
    - [Data Preparation](#data-preparation-1)
    - [Data Analysis](#data-analysis-1)
    - [Comparison of L2 Data Agents](#comparison-of-l2-data-agents)
  - [🤖 Proto-L3: Striving for Autonomous Data Agents](#-proto-l3-striving-for-autonomous-data-agents)
    - [Academia Research](#academia-research)
    - [Industry Products](#industry-products)
    - [Comparison of Proto-L3 Data Agents](#comparison-of-proto-l3-data-agents-from-academia-research-and-industry-products)
  - [🔮 L4-L5: Vision of Proactive and Generative Data Agents (Prospect)](#-l4-l5-vision-of-proactive-and-generative-data-agents-prospect)
  - [📚 Survey and Tutorial](#-survey-and-tutorial)
- [🔬 Research Opportunites](#-research-opportunities)

## 🎯 Introduction

<p align="center"><img src="assets/overview.jpg" alt="Teaser" width="100%"></p>

The rapid advancement of large language models (LLMs) has spurred the emergence of data agents — autonomous systems designed to orchestrate Data + AI ecosystems for tackling complex data-related tasks. However, the term "data agent" currently suffers from terminological ambiguity and inconsistent adoption, conflating simple query responders with sophisticated autonomous architectures. This terminological ambiguity fosters mismatched user expectations, accountability challenges, and barriers to industry growth.

Inspired by the SAE J3016 standard for driving automation, this survey introduces the first systematic hierarchical taxonomy for data agents, comprising six levels that delineate and trace progressive shifts in autonomy, from manual operations (L0) to a vision of generative, fully autonomous data agents (L5), thereby clarifying capability boundaries and responsibility allocation. 

Through this lens, we offer a structured review of existing research arranged by increasing autonomy, encompassing specialized data agents for data management, preparation, and analysis, alongside emerging efforts toward versatile, comprehensive systems with enhanced autonomy. We further analyze critical evolutionary leaps and technical gaps for advancing data agents, especially the ongoing L2-to-L3 transition, where data agents evolve from procedural execution to autonomous orchestration.
Finally, we conclude with a forward-looking roadmap, envisioning the advent of proactive, generative data agents.


## 🪜 Levels of Data Agents

As mentioned above, to bring clarity to the diverse landscape of data agents, we propose a hierarchical taxonomy based on their degree of autonomy. This framework maps the progressive shift of responsibility from human to agent, defining the distinct roles each plays at every stage, as summarized in the overview figure and the table below. 

| Level | Degree of Autonomy | Human Role | Data Agent Role |
|:-----:|------|------------|------------|
| L0 | Manual/No Autonomy | Dominator (Solo) | N/A (None) |
| L1 | Assisted | Dominator (Integrating) | Assistant (Responder) |
| L2 | Partial Autonomy | Dominator (Orchestrating) | Executor (Procedural) |
| L3 | Conditional Autonomy | Supervisor (Overseeing) | Dominator (Autonomous) |
| L4 | High Autonomy | Onlooker (Delegating) | Dominator (Proactive) |
| L5 | Full Autonomy | N/A (None) | Dominator (Generative) |

The transition between these levels represents more than just incremental progress; each step up the hierarchy requires a significant evolutionary leap as shown below. These leaps involve fundamental shifts in a data agent's capabilities—such as gaining environmental perception (L1→L2), achieving autonomous orchestrating and dominating the task (L2→L3), attaining proactive self-governance with supervision removed (L3→L4), and innovating or pioneering new paradigm (L4→L5).

<p align="center"><img src="assets/leaps.jpg" alt="Leaps" width="100%"></p>


## 📑 Paper List

<p align="center"><img src="assets/representative_work.jpg" alt="Leaps" width="100%"></p>


We index papers **by autonomy level**, then **by data-related tasks** across Data Management, Data Preparation, and Data Analysis. Most existing work clusters in L1–L3, while L4–L5 are aspirational. We also list relevant surveys and tutorials.

### 💬 L0-L1: From Manual Labor to Preliminary Assistance

In L0 level, data-related tasks are performed entirely by human experts without any automation. The process is completely human-driven, requiring extensive domain knowledge and solid technical expertise, making it highly specialized and time-consuming.

<p align="center"><img src="assets/l1_agent.jpg" alt="L1" width="50%"></p>

At L1 level, data agents start to have the capabilities to provide preliminary and single-point assistance through typical question-answering interactions. While they can help with atomic tasks like code pieces generation, they lack environmental perception and require considerable human validation, editing, and optimization.

#### Data Management
##### Configuration Tuning
- [LLMTune: Accelerate Database Knob Tuning with Large Language Models](https://arxiv.org/abs/2404.11581v1) - *arXiv 2024*
- [LATuner: An LLM-Enhanced Database Tuning System Based on Adaptive Surrogate Model](https://dl.acm.org/doi/abs/10.1007/978-3-031-70362-1_22) - *ECML PKDD 2024*
- [GPTuner: A Manual-Reading Database Tuning System via GPT-Guided Bayesian Optimization](https://vldb.org/pvldb/vol17/p1939-tang.pdf) - *VLDB 2024*
- [λ-Tune: Harnessing Large Language Models for Automated Database System Tuning](https://dl.acm.org/doi/abs/10.1145/3709652) - *SIGMOD 2025*
- [E2ETune: End-to-End Knob Tuning via Fine-tuned Generative Language Model](https://arxiv.org/abs/2404.11581) - *VLDB 2025*
##### Query Optimization
- [DB-GPT: Large Language Model Meets Database](https://link.springer.com/article/10.1007/s41019-023-00235-6) - *Data Science and Engineering 2024*
- [LLM-R2: A Large Language Model Enhanced Rule-Based Rewrite System for Boosting Query Efficiency](https://dl.acm.org/doi/abs/10.14778/3696435.3696440) - *VLDB 2024*
- [Query Rewriting via Large Language Models](https://arxiv.org/abs/2403.09060) - *arXiv 2024*
- [Query Rewriting via LLMs](https://arxiv.org/abs/2502.12918) - *arXiv 2025*
- [Can Large Language Models Be Query Optimizer for Relational Databases?](https://arxiv.org/abs/2502.05562) - *arXiv 2025*
- [A Query Optimization Method Utilizing Large Language Models](https://arxiv.org/abs/2503.06902) - *arXiv 2025*
- [E3-Rewrite: Learning to Rewrite SQL for Executability, Equivalence, and Efficiency](https://arxiv.org/abs/2508.09023) - *arXiv 2025*
##### System Diagnosis
- [DBG-PT: A Large Language Model Assisted Query Performance Regression Debugger](https://dl.acm.org/doi/abs/10.14778/3685800.3685869) - *VLDB 2024*
- [Automatic Database Configuration Debugging using Retrieval-Augmented Language Models](https://dl.acm.org/doi/abs/10.1145/3709663) - *SIGMOD 2025*
#### Data Preparation
##### Data Cleaning
- [Can Foundation Models Wrangle Your Data?](https://arxiv.org/abs/2205.09911) - *VLDB 2022*
- [RetClean: Retrieval-Based Data Cleaning Using LLMs and Data Lakes](https://arxiv.org/abs/2303.16909) - *VLDB demo 2024*
- [Data Imputation with Limited Data Redundancy Using Data Lakes](https://www.vldb.org/pvldb/vol18/p3354-tang.pdf) - *VLDB 2025*
- [UNIDM: A UNIFIED FRAMEWORK FOR DATA MANIPULATION WITH LARGE LANGUAGE MODELS](https://arxiv.org/pdf/2405.06510) - *MLSys 2024*
- [LLMClean: Context-Aware Tabular Data Cleaning via LLM-Generated OFDs](https://arxiv.org/abs/2404.18681) - *ADBIS 2024*
##### Data Integration
- [Table-GPT: Table-tuned GPT for Diverse Table Tasks](https://arxiv.org/pdf/2310.09263) - *SIGMOD 2024*
- [Cost-Effective In-Context Learning for Entity Resolution: A Design Space Exploration](https://arxiv.org/pdf/2312.03987) - *ICDE 2024*
- [Jellyfish: Instruction-Tuning Local Large Language Models for Data Preprocessing](https://aclanthology.org/2024.emnlp-main.497/) - *EMNLP 2024*
##### Data Discovery
- [ArcheType: A Novel Framework for Open-Source Column Type Annotation using Large Language Models](https://arxiv.org/pdf/2310.18208) - *VLDB 2024*
- [RACOON: An LLM-based Framework for Retrieval-Augmented Column Type Annotation with a Knowledge Graph](https://arxiv.org/abs/2409.14556) - *arXiv 2024*
- [Cocoon: Semantic table profiling using large language model](https://dl.acm.org/doi/abs/10.1145/3665939.3665957) - *HILDA 2024*
- [Autoddg: Automated dataset description generation using large language models](https://arxiv.org/abs/2502.01050) - *arXiv 2025*
- [Pneuma: Leveraging llms for tabular data representation and retrieval in an end-to-end system](https://dl.acm.org/doi/abs/10.1145/3725337) - *SIGMOD 2025*
- [Evaluating Knowledge Generation and Self-refinement Strategies for LLM-Based Column Type Annotation](https://link.springer.com/chapter/10.1007/978-3-032-05281-0_8) - *ADBIS 2025*
- [Columbo: Expanding Abbreviated Column Names for Tabular Data Using Large Language Models](https://arxiv.org/abs/2508.09403) - *EMNLP 2025*
#### Data Analysis
##### TableQA
- [Large Language Models are Versatile Decomposers: Decomposing Evidence and Questions for Table-based Reasoning](https://dl.acm.org/doi/10.1145/3539618.3591708) - *SIGIR 2023*
- [Binding Language Models in Symbolic Languages](https://arxiv.org/abs/2210.02875) - *ICLR 2023*
- [Table Meets LLM: Can Large Language Models Understand Structured Table Data? A Benchmark and Empirical Study](https://dl.acm.org/doi/abs/10.1145/3616855.3635752) - *WSDM 2024*
- [TableLlama: Towards Open Large Generalist Models for Tables](https://aclanthology.org/2024.naacl-long.335/) - *NAACL 2024*
##### NL2SQL
- [DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction.](https://arxiv.org/abs/2304.11015) - *NeurIPS 2023*
- [Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation](https://arxiv.org/abs/2308.15363) - *VLDB 2023*
- [ACT-SQL: In-Context Learning for Text-to-SQL with Automatically-Generated Chain-of-Thought](https://arxiv.org/pdf/2310.17342) - *EMNLP 2023*
- [The Dawn of Natural Language to SQL: Are We Fully Ready?](https://arxiv.org/pdf/2406.01265) - *VLDB 2024*
##### NL2VIS
- [Chat2VIS: Generating Data Visualizations via Natural Language Using ChatGPT, Codex and GPT-3 Large Language Models](https://ieeexplore.ieee.org/document/10121440) - *IEEE Access 2023*
- [Generating Analytic Specifications for Data Visualization from Natural Language Queries using Large Language Models](https://arxiv.org/html/2408.13391v2) - *VIS 2024*
- [prompt4vis: prompting large language models with example mining for tabular data visualization: Prompt4Vis: prompting large language models with example mining](https://dl.acm.org/doi/abs/10.1007/s00778-025-00912-0) - *VLDB 2025*
- [nvBench 2.0: Resolving Ambiguity in Text-to-Visualization through Stepwise Reasoning](https://arxiv.org/abs/2503.12880) - *NeurIPS 2025*
##### Unstructured Data Analysis
- [LongRAG: A Dual-Perspective Retrieval-Augmented Generation Paradigm for Long-Context Question Answering](https://aclanthology.org/2024.emnlp-main.1259.pdf) - *EMNLP 2024*
- [RAPTOR: Recursive Abstractive Processing for Tree-Organized Retrieval](https://arxiv.org/abs/2401.18059) - *ICLR 2024*
- [PDFTriage: Question Answering over Long, Structured Documents](https://aclanthology.org/2024.emnlp-industry.13.pdf) - *EMNLP 2024*
- [Unifying Multimodal Retrieval via Document Screenshot Embedding](https://arxiv.org/pdf/2406.11251) - *EMNLP 2024*
- [VisDoM: Multi-Document QA with Visually Rich Elements Using Multimodal Retrieval-Augmented Generation](https://aclanthology.org/2025.naacl-long.310.pdf) - *NAACL 2025*
- [Docopilot: Improving Multimodal Models for Document-Level Understanding](https://openaccess.thecvf.com/content/CVPR2025/papers/Duan_Docopilot_Improving_Multimodal_Models_for_Document-Level_Understanding_CVPR_2025_paper.pdf) - *CVPR 2025*
##### Report Generation
- [DataTales: Investigating the use of Large Language Models for Authoring Data-Driven Articles](https://arxiv.org/abs/2308.04076) - *VIS 2023*
- [Enhancing Data Literacy On-demand: LLMs as Guides for Novices in Chart Interpretation](https://ieeexplore.ieee.org/document/10555321) - *TVCG 2024*
- [ReportGPT: Human‑in‑the‑Loop Verifiable Table‑to‑Text Generation](https://aclanthology.org/2024.emnlp-industry.39/) - *EMNLP Industry 2025*
- [InterChat: Enhancing Generative Visual Analytics using Multimodal Interactions](https://onlinelibrary.wiley.com/doi/10.1111/cgf.70112?af=R) - *EuroVis 2025*
- [VizTA: Enhancing Comprehension of Distributional Visualization with Visual-Lexical Fused Conversational Interface](https://onlinelibrary.wiley.com/doi/full/10.1111/cgf.70110) - *EuroVis 2025*
- [ChartLens: Fine-grained Visual Attribution in Charts](https://aclanthology.org/2025.acl-long.1094/) - *ACL 2025*

#### Comparison of L1 Data Agents
ICL: In-Context Learning; RAG: Retrieval-Augmented Generation; SFT: Supervised Fine-Tuning; RL: Reinforcement Learning. Data complexity dimensions include Multi-source (Multis.), Heterogeneous (Hete.), and Multimodal (Multim.) data support.
<p align="center"><img src="assets/l1_comparison.png" width="100%"></p>

### 🌏 L2: Perceive the Environment

<p align="center"><img src="assets/l2_agent.jpg" alt="L2" width="50%"></p>

At L2, data agents gain the ability to perceive and interact with their environment, including data lakes, code interpreters, APIs, and other resources. In addition, L2 data agents can possess memory, invoke external tools, and adaptively optimize their actions based on environmental feedback, enabling partial autonomy in task-specific procedures. At this level, they evolve from simple responders to procedural executors operating within human-orchestrated pipelines, where humans remain responsible for managing the overall workflow and still retain dominance over data-related tasks.

#### Data Management
##### Configuration Tuning
- [Is Large Language Model Good at Database Knob Tuning? A Comprehensive Experimental Evaluation](https://arxiv.org/pdf/2408.02213) - *arXiv 2024*
- [LLMIdxAdvis: Resource-Efficient Index Advisor Utilizing Large Language Model](https://arxiv.org/abs/2503.07884) - *arXiv 2025*
- [Rabbit: Retrieval-Augmented Generation Enables Better Automatic Database Knob Tuning](https://ieeexplore.ieee.org/document/11113071) - *ICDE 2025*
- [MCTuner: Spatial Decomposition-Enhanced Database Tuning via LLM-Guided Exploration](https://arxiv.org/abs/2509.06298) - *arXiv 2025*
- [AgentTune: An Agent-Based Large Language Model Framework for Database Knob Tuning](https://dl.acm.org/doi/10.1145/3769758) - *SIGMOD 2026*
##### Query Optimization
- [SERAG: Self-Evolving RAG System for Query Optimization](https://viterbi-web.usc.edu/~sabek/pdf/25_workshop_serag.pdf) - *SIGMOD Workshop 2025*
- [QUITE: A Query Rewrite System Beyond Rules with LLM Agents](https://arxiv.org/abs/2506.07675) - *arXiv 2025*
- [R-Bot: An LLM-Based Query Rewrite System](https://arxiv.org/abs/2412.01661) - *VLDB 2025*
- [Cracking SQL Barriers: An LLM-based Dialect Translation System](https://dl.acm.org/doi/10.1145/3725278) - *SIGMOD 2025*
##### System Diagnosis
- [Panda: Performance Debugging for Databases using LLM Agents](https://www.vldb.org/cidrdb/papers/2024/p6-singh.pdf) - *CIDR 2024*
- [D-Bot: Database Diagnosis System using Large Language Models](https://arxiv.org/abs/2312.01454) - *VLDB 2024*
- [DBAIOps: A Reasoning LLM-Enhanced Database Operation and Maintenance System using Knowledge Graphs](https://arxiv.org/abs/2508.01136) - *arXiv 2025*
#### Data Preparation
##### Data Cleaning
- [SketchFill: Sketch-Guided Code Generation for Imputing Derived Missing Values](https://arxiv.org/abs/2412.19113) - *arXiv 2024*
- [IterClean: An Iterative Data Cleaning Framework with Large Language Models](https://dl.acm.org/doi/pdf/10.1145/3674399.3674436) - *ACM-TURC 2024*
- [AutoPrep: Natural Language Question-Aware Data Preparation with a Multi-Agent Framework](https://arxiv.org/pdf/2412.10422) - *VLDB 2025*
- [AutoDCWorkflow: LLM-based Data Cleaning Workflow Auto-Generation and Benchmark](https://arxiv.org/abs/2412.06724) - *EMNLP Findings 2025*
- [CleanAgent: Automating Data Standardization with LLM-based Agents](https://www.vldb.org/2025/Workshops/VLDB-Workshops-2025/DATAI/DATAI25_8.pdf) - *VLDB Workshop 2025*
- [Exploring LLM Agents for Cleaning Tabular Machine Learning Datasets](https://arxiv.org/pdf/2503.06664) - *ICLR Workshop 2025*
- [Weak-to-Strong Prompts with Lightweight-to-Powerful LLMs for High-Accuracy, Low-Cost, and Explainable Data Transformation](https://www.vldb.org/pvldb/vol18/p2371-tang.pdf) - *VLDB 2025*
##### Data Integration
- [Agent-OM: Leveraging LLM Agents for Ontology Matching](https://arxiv.org/pdf/2312.00326) - *VLDB 2024*
- [Ontology Matching with Large Language Models and Prioritized Depth-First Search](https://arxiv.org/pdf/2501.11441) - *Information Fusion 2025*
- [Match, Compare, or Select? An Investigation of Large Language Models for Entity Matching](https://arxiv.org/pdf/2405.16884) - *COLING 2025*
##### Data Discovery
- [Chorus: Foundation Models for Unified Data Discovery and Exploration](https://dl.acm.org/doi/abs/10.14778/3659437.3659461) - *VLDB 2024*
- [Data-driven Discovery with Large Generative Models](https://arxiv.org/pdf/2402.13610) - *arXiv 2024*
- [DATALORE: Can a Large Language Model Find All Lost Scrolls in a Data Repository?](https://ieeexplore.ieee.org/abstract/document/10597732) - *ICDE 2024*
- [LEDD: Large Language Model-Empowered Data Discovery in Data Lakes](https://arxiv.org/abs/2502.15182) - *arXiv 2025*
- [Automated Metadata Generation Using Large Language Models: A GPT-4 Case Study for Enterprise Data Profiling](https://sarcouncil.com/download-article/SJECS-221-2025-769-775.pdf) - *Journal for Engineering and Computer Science 2025*
- [Automatic database description generation for Text-to-SQL](https://arxiv.org/abs/2502.20657) - *arXiv 2025*
- [Towards Operationalizing Heterogeneous Data Discovery](https://arxiv.org/pdf/2504.02059) - *arXiv 2025*
#### Data Analysis
##### TableQA
- [StructGPT: A General Framework for Large Language Model to Reason over Structured Data](https://aclanthology.org/2023.emnlp-main.574/) - *EMNLP 2023*
- [ReAcTable: Enhancing ReAct for Table Question Answering](https://dl.acm.org/doi/10.14778/3659437.3659452) - *VLDB 2024*
- [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding](https://arxiv.org/abs/2401.04398) - *ICLR 2024*
- [AutoTQA: Towards Autonomous Tabular Question Answering through Multi-Agent Large Language Models](https://www.vldb.org/pvldb/vol17/p3920-zhu.pdf) - *VLDB 2024*
- [Table-Critic: A Multi-Agent Framework for Collaborative Criticism and Refinement in Table Reasoning](https://aclanthology.org/2025.acl-long.853/) - *ACL 2025*
- [ST-Raptor: LLM-Powered Semi-Structured Table Question Answering](https://arxiv.org/abs/2508.18190) - *SIGMOD 2026*
##### NL2SQL
- [MAC-SQL: A Multi-Agent Collaborative Framework for Text-to-SQL](https://arxiv.org/abs/2312.11242) - *COLING 2023*
- [Chatbi: Towards natural language to complex business](https://arxiv.org/pdf/2405.00527) - *arXiv 2024*
- [CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL](https://arxiv.org/abs/2410.01943) - *ICLR 2024*
- [Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search](https://arxiv.org/pdf/2502.17248) - *ICML 2025*
- [OpenSearch-SQL: Enhancing Text-to-SQL with Dynamic Few-shot and Consistency Alignment.](https://arxiv.org/pdf/2502.14913) - *SIGMOD 2025*
- [ReFoRCE: A Text-to-SQL Agent with Self-Refinement, Consensus Enforcement, and Column Exploration](https://arxiv.org/pdf/2502.00675) - *arXiv 2025*
- [DeepEye-SQL: A Software-Engineering-Inspired Text-to-SQL Framework](https://www.arxiv.org/pdf/2510.17586) - *arXiv 2025*
##### NL2VIS
- [MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization](https://arxiv.org/pdf/2402.11453) - *ACL 2024*
- [Text2Chart31: Instruction Tuning for Chart Generation with Automatic Feedback](https://arxiv.org/pdf/2410.04064) - *EMNLP 2024*
- [NVAGENT: Automated Data Visualization from Natural Language via Collaborative Agent Workflow](https://arxiv.org/pdf/2502.05036) - *ACL 2025*
- [DeepVIS: Bridging Natural Language and Data Visualization Through Step-wise Reasoning](https://arxiv.org/pdf/2508.01700) - *VIS 2025*
##### Unstructured Data Analysis
- [Active Retrieval Augmented Generation](https://arxiv.org/pdf/2305.06983) - *NeurIPS 2023*
- [A Human-Inspired Reading Agent with Gist Memory of Very Long Contexts](https://arxiv.org/pdf/2402.09727) - *ICML 2024*
- [GraphReader: Building Graph-based Agent to Enhance Long-Context Abilities of Large Language Models](https://arxiv.org/pdf/2406.14550) - *EMNLP 2024*
- [Self-RAG: Learning to Retrieve, Generate, and Critique through Self-Reflection](https://arxiv.org/pdf/2310.11511) - *ICLR 2024*
- [REAR: A Relevance-Aware Retrieval-Augmented Framework for Open-Domain Question Answering](https://aclanthology.org/2024.emnlp-main.321.pdf) - *EMNLP 2024*
- [QUEST: Query Optimization in Unstructured Document Analysis](https://dl.acm.org/doi/pdf/10.14778/3749646.3749713) - *VLDB 2025*
- [Doctopus: Budget-aware Structural Table Extraction from Unstructured Documents](https://www.vldb.org/pvldb/vol18/p3695-chai.pdf) - *VLDB 2025*
- [Visual Document Understanding and Question Answering: A Multi-Agent Collaboration Framework with Test-Time Scaling](https://arxiv.org/pdf/2508.03404) - *arXiv 2025*
- [DataPuzzle: Breaking Free from the Hallucinated Promise of LLMs in Data Analysis](https://arxiv.org/abs/2504.10036) - *arXiv 2025*
##### Report Generation
- [DataNarrative: Automated Data-Driven Storytelling with Visualizations and Texts](https://aclanthology.org/2024.emnlp-main.1073/) - *EMNLP 2024*
- [From Data to Story: Towards Automatic Animated Data Video Creation with LLM-based Multi-Agent Systems](https://ieeexplore.ieee.org/document/10766492) - *VIS  workshop 2024*
- [LightVA: Lightweight Visual Analytics with LLM Agent-Based Task Planning and Execution](https://ieeexplore.ieee.org/document/10753451) - *TVCG 2024*
- [Multimodal DeepResearcher: Generating Text–Chart Interleaved Reports with an Agentic Framework](https://arxiv.org/abs/2506.02454) - *arXiv 2025*
- [DAgent: A Relational Database-Driven Data Analysis Report Generation Agent](https://arxiv.org/abs/2503.13269) - *arXiv 2025*
- [ChartInsighter: An Approach for Mitigating Hallucination in Time-Series Chart Summary Generation With a Benchmark Dataset](https://ieeexplore.ieee.org/document/10988687) - *TVCG 2025*
- [ProactiveVA: Proactive Visual Analytics with LLM-Based UI Agent](https://arxiv.org/abs/2507.18165) - *VIS 2025*
- [VOICE: Visual Oracle for Interaction, Conversation, and Explanation](https://ieeexplore.ieee.org/document/11037292) - *TVCG 2025*
- [NLI4VolVis: Natural Language Interaction for Volume Visualization  via LLM Multi-Agents and Editable 3D Gaussian Splatting (VIS'25)](https://arxiv.org/abs/2507.12621) - *VIS 2025*

#### Comparison of L2 Data Agents
RAG: Retrieval-Augmented Generation; Percept: Environmental Perception; Plan: Planning; Mem: Memory; Tool: Tool invocation; Reflect: Self-reflection mechanism; MAS: Multi-agent system; SFT: Supervised Fine-Tuning; RL: Reinforcement Learning. Data complexity dimensions include Multi-source (Multis.), Heterogeneous (Hete.), and Multimodal (Multim.) data support.
<p align="center"><img src="assets/l2_comparison.png" width="100%"></p>

### 🤖 Proto-L3: Striving for Autonomous Data Agents

<p align="center"><img src="assets/l3_agent.jpg" alt="L3" width="50%"></p>

L3 data agents are expected to autonomously orchestrate tailored data pipelines for a wide range of diverse and comprehensive data-related tasks under supervision, extending beyond human-defined workflows or specific tasks. This level marks a critical transition in which the data agent assumes a dominant role in data-related tasks, while humans act as supervisors overseeing the data agents' operation.
To date, no existing system has fully realized such versatile, self-directed orchestration capabilities that define a complete L3 data agent. However, emerging efforts from both academia and industry are beginning to address these challenges, giving rise to what we term "Proto-L3" data agents.

#### Academia Research
- [AgenticData: An Agentic Data Analytics System for Heterogeneous Data](https://arxiv.org/pdf/2508.05002) - *arXiv 2025*
- [DeepAnalyze: Agentic Large Language Models for Autonomous Data Science](https://arxiv.org/abs/2510.16872v1) - *arXiv 2025*
- [AOP: Automated and Interactive LLM Pipeline Orchestration for Answering Complex Queries](https://www.vldb.org/cidrdb/papers/2025/p32-wang.pdf) - *CIDR 2025*
- [iDataLake: An LLM-Powered Analytics System on Data Lakes](http://sites.computer.org/debull/A25mar/p57.pdf) - *IEEE Data Engineering Bulletin 2025*
- [SiriusBI: A Comprehensive LLM-Powered Solution for Data Analytics in Business Intelligence](https://dl.acm.org/doi/10.14778/3750601.3750610) - *VLDB 2025*
- [Data Interpreter: An LLM Agent For Data Science](https://arxiv.org/pdf/2402.18679) - *ACL Findings 2024*

#### Industry Products
- [JoyAgent](https://github.com/jd-opensource/joyagent-jdgenie/tree/data_agent) — *JDCHO*
- [TabTab](https://tabtabai.com/) — *TabTab AI*
- [Assist. DS Agent](https://www.databricks.com/blog/introducing-databricks-assistant-data-science-agent) — *Databricks*
- [Data Agent](https://www.volcengine.com/product/DataAgent) — *Bytedance*
- [BigQuery](https://cloud.google.com/blog/products/data-analytics/a-closer-look-at-bigquery-data-engineering-agent) — *Google*
- [Cortex](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents) — *Snowflake*
- [Xata Agent](https://xata.io/blog/dba-to-db-agent) — *Xata*

#### Comparison of Proto-L3 Data Agents from Academia Research and Industry Products
Compares Open-source: availability; Undef Ops.: capabilities in utilizing unpredefined operators; data-related task coverage across data management, preparation, analysis; data complexity dimensions: Multi-source (Multis.), Heterogeneous (Hete.), and Multimodal (Multim.)
<p align="center"><img src="assets/l3_comparison.png" width="100%"></p>

### 🔮 L4-L5: Vision of Proactive and Generative Data Agents (Prospect)

#### L4: Vision of Proactive Data Agents

At L4, data agents are expected to achieve a high level of autonomy and reliability, eliminating the need for human supervision and explicit task instructions. They can proactively identify issues worthy of investigation through continuous monitoring and exploration of data lakes, and selectively orchestrate pipelines to tackle self-discovered problems. At this level, data agents take initiative in their operations while humans fully delegate responsibility, becoming onlookers.

<p align="center"><img src="assets/l4_agent.jpg" alt="L4" width="50%"></p>

#### L5: The Ultimate Vision of Ubiquitous and Generative Data Agents

At the ultimate level of L5, beyond applying existing methods, data agents are envisioned to be capable of inventing novel solutions and pioneering new paradigms. In doing so, they advance the state-of-the-art in data management, preparation, and analysis, making any form of human involvement unnecessary.

<p align="center"><img src="assets/l5_agent.jpg" alt="L4" width="50%"></p>

### 📚 Survey and Tutorial

- [A Survey of Text-to-SQL in the Era of LLMs: Where are we, and where are we going?](https://ieeexplore.ieee.org/document/11095853) - *TKDE 2025*
- [Natural Language to SQL: State of the Art and Open Problems](https://www.vldb.org/pvldb/vol18/p5466-luo.pdf) - *VLDB Tutorial 2025*
- [A Survey of LLM × DATA](https://arxiv.org/abs/2505.18458) - *arXiv 2025*
- [LLM/Agent-as-Data-Analyst: A Survey](https://arxiv.org/abs/2509.23988) - *arXiv 2025*
- [Large Language Model-based Data Science Agent: A Survey](https://www.arxiv.org/abs/2508.02744) - *arXiv 2025*
- [LLM-Based Data Science Agents: A Survey of Capabilities, Challenges, and Future Directions](https://arxiv.org/abs/2510.04023) - *arXiv 2025*
- [Large Language Models for Data Science: A Survey](https://rgdoi.net/10.13140/RG.2.2.14003.75042) - *arXiv 2025*
- [A Survey on Large Language Model-based Agents for Statistics and Data Science](https://arxiv.org/abs/2412.14222) - *The American Statistician 2025*
- [Large Language Models for Data Discovery and Integration: Challenges and Opportunities](http://sites.computer.org/debull/A25mar/p3.pdf) - *IEEE Data Eng. Bull. 2025*
- [Data+AI: LLM4Data and Data4LLM](https://dl.acm.org/doi/pdf/10.1145/3722212.3725641) - *SIGMOD Tutorial 2025*
- [LLM for Data Management](https://www.vldb.org/pvldb/vol17/p4213-li.pdf) - *VLDB Tutorial 2024*
- [Large Language Models for Data Annotation and Synthesis: A Survey](https://aclanthology.org/2024.emnlp-main.54.pdf) - *ACL 2024*
- [Data Management for Machine Learning: A Survey](https://ieeexplore.ieee.org/document/9705125) - *TKDE 2023*
- [LLM As DBA](https://arxiv.org/pdf/2308.05481) - *arXiv 2023*
- [Demystifying Artificial Intelligence for Data Preparation](https://dl.acm.org/doi/pdf/10.1145/3555041.3589406) - *SIGMOD Tutorial 2023*

## 🔬 Research Opportunities

Enhancing the core components of data agents can involve advancing five key aspects: **Perception** (e.g., environmental understanding), **Planning** (e.g., task decomposition and reflection), **Actions** (e.g., autonomous pipeline orchestration), **Tools** (e.g., tool invocation and discovery), and **Memory** (e.g., strategic knowledge retention).

<p align="center"><img src="assets/opportunities_talk_cn.png" width="100%"></p>

Our survey also identifies and discusses that while significant progress has been made, a substantial chasm still separates current "Proto-L3" systems from the expected true L3 autonomy. Bridging this gap, and eventually progressing to L4/L5, requires addressing several fundamental challenges, which represent key research opportunities for the field. For more information, please refer to our [[Survey]](reports/Data_Agents_Survey.pdf) and [[Slides]](slides/从智能问数到数据智能体：范式演进与反思.pdf) of a recent (Chinese) talk.

### The Critical L2-to-L3 Transition
The primary bottleneck lies in elevating data agents from **procedural executors (L2)** to **autonomous dominators (L3)**. As highlighted in the figure above, this requires significant advancements across five key aspects of agentic architecture: **Perception, Planning, Actions, Tools, and Memory**. Successfully bridging this gap involves overcoming four main deficiencies:

* **1. Limited Autonomy in Pipeline Orchestration:**
    Current data agents heavily rely on a *predefined set of operators and tools*. While some systems demonstrate "Tool Evolution" through recombination, a key opportunity lies in **automatic data-skill discovery**. Future research should focus on enabling data agents to *generate, validate, and deploy* emergent skills *ab initio*, transcending fixed toolsets.

* **2. Incomplete Coverage of the Data Lifecycle:**
    Most Proto-L3 systems are "predominantly centered on data analysis". Crucial **data management tasks**—such as configuration tuning, system diagnosis, and query optimization—remain "largely unaddressed". A major research direction is enhancing data agent **versatility** to create "data experts" that can reason about and autonomously orchestrate tasks across the *full data lifecycle*.

* **3. Deficiencies in Advanced Reasoning:**
    Data agents exhibit strong *tactical* capabilities (e.g., fixing immediate errors) but lack *strategic* "higher-order reasoning". This can trap them in "unproductive loops". This highlights a need for research in **integrated causal reasoning and meta-reasoning**. Furthermore, data agents require **sophisticated memory architectures** that capture abstract strategic knowledge, not just task execution history.

* **4. Inadequate Adaptation to Dynamic Environments:**
    Most systems are designed and evaluated against *static data and tasks*. They lack the ability to "genuinely self-evolve" when faced with data drift or changing schemas. Developing **effective and human-free adaptation methods**—and **robust evaluation benchmarks** for dynamic conditions—remains a promising and critical research direction.

### The L4-L5 Vision: The Research Odyssey Ahead
Moving beyond L3 supervision towards proactive (L4) and generative (L5) data agents presents a long-term research odyssey. Key frontiers include:

* **Autonomous Problem Discovery (L4):** Shifting from *reacting* to user tasks to *proactively* identifying valuable tasks. This requires endowing data agents with **intrinsic motivation** and "curiosity" to independently monitor and explore data lakes to discover anomalies or opportunities worthy of investigation.

* **Long-Horizon and Holistic Planning (L4):** Moving beyond local, step-by-step optimization to **long-horizon planning**. L4 data agents must be able to make strategic trade-offs, such as balancing the immediate cost of data cleaning against long-term analytical benefits.

* **Generative Innovation (L5):** The ultimate vision is a data agent that can *innovate and pioneer new paradigms*. Instead of merely applying existing methods, an L5 data agent would recognize the limitations of current approaches and *invent novel algorithms, theories, or frameworks* to advance the state-of-the-art.
