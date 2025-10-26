
<h1 align="center">Awesome Data Agents</h1>
<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) 
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)


</div>

> Curated papers and resources on **Data Agents**. Companion list for our (incoming) survey of data agents: [[Paper]](reports/Data_Agents_Survey.pdf)
>
> We also release slides for a recent talk (Chinese): [[Slides]](slides/从智能问数到数据智能体：范式演进与反思.pdf)

If you find this repository useful or inspiring, please kindly give us a star ⭐️ and cite our survey:

```bibtex
Coming soon
```

## Contents

- [Introduction](#introduction)
- [Levels of Data Agents](#levels-of-data-agents)
- [Paper List](#paper-list)

## 🎯 Introduction

<p align="center"><img src="assets/overview.jpg" alt="Teaser" width="100%"></p>

The way humans interact with data is undergoing a profound transformation. Data agents — LLM-powered systems designed to orchestrate the Data + AI ecosystem — are emerging as a promising solution for automating and democratizing data-related tasks across its lifecycle, from management and preparation to analysis.

However, the term "data agent" is currently used inconsistently across research and industry, resulting in considerable ambiguity. Systems with vastly different capabilities in autonomy, reliability, and task complexity are often labeled the same way. This creates a terminological ambiguity leading to mismatched expectations and unclear accountability challenge user trust and healthy development of the field.

This repository — a companion to our survey — introduces a hierarchical taxonomy (L0-L5) for data agents based on their degree of autonomy, providing a common framework to clarify capability boundaries and lines of accountability at each level.


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


We index papers **by autonomy level**, then **by data-related tasks** across Data Management, Data Preparation, and Data Analysis. Most existing work clusters in L1–L3, L4–L5 are aspirational. We also list relevant surveys, tutorials and benchmarks.

### 💬 L0-L1: From Manual Labor to Preliminary Assistance

In L0 level, data-related tasks are performed entirely by human experts without any automation. The process is completely human-driven, requiring extensive domain knowledge and solid technical expertise, making it highly specialized and time-consuming.

<p align="center"><img src="assets/l1_agent.jpg" alt="L1" width="50%"></p>

At L1 level, data agents start to have the capabilities to provide preliminary and single-point assistance through typical question-answering interactions. While they can help with atomic tasks like code peices generation, they lack environmental perception and require considerable human validation, editing, and optimization.

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

### 🌏 L2: Perceive the Environment

<p align="center"><img src="assets/l2_agent.jpg" alt="L2" width="50%"></p>

At this level, data agents gain environmental perception and tool-invocation capabilities, enabling them to execute bounded sub-tasks and multi-step procedures. While they can follow human-orchestrated workflows, the overall process is still dominated by human direction.

#### Data Management
##### Configuration Tuning
- [Is Large Language Model Good at Database Knob Tuning? A Comprehensive Experimental Evaluation](https://arxiv.org/pdf/2408.02213) - *arXiv 2024*
- [LLMIdxAdvis: Resource-Efficient Index Advisor Utilizing Large Language Model](https://arxiv.org/abs/2503.07884) - *arXiv 2025*
- [Rabbit: Retrieval-Augmented Generation Enables Better Automatic Database Knob Tuning](https://ieeexplore.ieee.org/document/11113071) - *ICDE 2025*
- [MCTuner: Spatial Decomposition-Enhanced Database Tuning via LLM-Guided Exploration](https://arxiv.org/abs/2509.06298) - *arXiv 2025*
##### Query Optimization
- [SERAG: Self-Evolving RAG System for Query Optimization](https://viterbi-web.usc.edu/~sabek/pdf/25_workshop_serag.pdf) - *SIGMOD Workshop 2025*
- [QUITE: A Query Rewrite System Beyond Rules with LLM Agents](https://arxiv.org/abs/2506.07675) - *arXiv 2025*
- [R-Bot: An LLM-Based Query Rewrite System](https://arxiv.org/abs/2412.01661) - *VLDB 2025*
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
##### NL2SQL
- [MAC-SQL: A Multi-Agent Collaborative Framework for Text-to-SQL](https://arxiv.org/abs/2312.11242) - *COLING 2023*
- [Chatbi: Towards natural language to complex business](https://arxiv.org/pdf/2405.00527) - *arXiv 2024*
- [CHASE-SQL: Multi-Path Reasoning and Preference Optimized Candidate Selection in Text-to-SQL](https://arxiv.org/abs/2410.01943) - *ICLR 2024*
- [Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search](https://arxiv.org/pdf/2502.17248) - *ICML 2025*
- [OpenSearch-SQL: Enhancing Text-to-SQL with Dynamic Few-shot and Consistency Alignment.](https://arxiv.org/pdf/2502.14913) - *SIGMOD 2025*
- [ReFoRCE: A Text-to-SQL Agent with with Self-Refinement, Consensus Enforcement, and Column Exploration](https://arxiv.org/pdf/2502.00675) - *arXiv 2025*
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

### 🤖 Proto-L3: Striving for Autonomous Data Agents

<p align="center"><img src="assets/l3_agent.jpg" alt="L3" width="50%"></p>

Level L3 marks a critical transition where data agents evolve from procedural executors into autonomous directors for data-related tasks. At this stage, they can independently decompose high-level goals, orchestrate and optimize tailored, end-to-end pipelines, shifting the human to a supervisory role. While recent pioneering efforts show promise, they are largely considered very early-stage "Proto-L3" systems. Consequently, the pursuit of more autonomous, reliable, versitile and comprehensive L3 data agents remains a key objective in both academia and industry.

- [AgenticData: An Agentic Data Analytics System for Heterogeneous Data](https://arxiv.org/pdf/2508.05002) - *arXiv 2025*
- [DeepAnalyze: Agentic Large Language Models for Autonomous Data Science](https://arxiv.org/abs/2510.16872v1) - *arXiv 2025*
- [AOP: Automated and Interactive LLM Pipeline Orchestration for Answering Complex Queries](https://www.vldb.org/cidrdb/papers/2025/p32-wang.pdf) - *CIDR 2025*
- [iDataLake: An LLM-Powered Analytics System on Data Lakes](http://sites.computer.org/debull/A25mar/p57.pdf) - *IEEE Data Engineering Bulletin 2025*
- [SiriusBI: A Comprehensive LLM-Powered Solution for Data Analytics in Business Intelligence](https://dl.acm.org/doi/10.14778/3750601.3750610) - *VLDB 2025*
- [Data Interpreter: An LLM Agent For Data Science](https://arxiv.org/pdf/2402.18679) - *ACL Findings 2024*
- [JoyAgent](https://github.com/jd-opensource/joyagent-jdgenie/tree/data_agent) — *JDCHO*
- [TabTab](https://tabtabai.com/) — *TabTab AI*
- [Assist. DS Agent](https://www.databricks.com/blog/introducing-databricks-assistant-data-science-agent) — *Databricks*
- [Data Agent](https://www.volcengine.com/product/DataAgent) — *Bytedance*
- [BigQuery](https://cloud.google.com/blog/products/data-analytics/a-closer-look-at-bigquery-data-engineering-agent) — *Google*
- [Cortex](https://docs.snowflake.com/en/user-guide/snowflake-cortex/cortex-agents) — *Snowflake*
- [Xata Agent](https://xata.io/blog/dba-to-db-agent) — *Xata*

### 🔮 L4-L5: Vision of Proactive and Generative Data Agents

#### L4: Vision of Proactive Data Agents

Data agents at L4 can achieve sustained self-governance with proactive monitoring and optimization across the data lifecycle. They can operate autonomously for extended periods without human supervision, actively providing insights and feedback while maintaining reliability.

<p align="center"><img src="assets/l4_agent.jpg" alt="L4" width="50%"></p>

#### L5: The Ultimate Vision of Ubiquitous and Generative Data Agents

The ultimate vision of fully autonomous data agents that can function as expert data scientists, capable of knowledge creation and paradigm innovation for data-related tasks.

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

