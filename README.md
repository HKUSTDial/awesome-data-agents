
<h1 align="center">Awesome Data Agents</h1>
<div align="center">

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re) 
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)
</div>

> Curated papers and resources on **Data Agents** — from the perspective of proposed *autonomy levels*. Companion list for our (incoming) survey.

If you find this repository useful or inspiring, please kindly give us a star ⭐️ and cite our survey:

```bibtex
Coming soon
```

## Contents

- [Introduction](#introduction)
- [Levels of Data Agents](#levels-of-data-agents)
- [How the List is Organized](#how-the-list-is-organized)
- [Paper List](#paper-list)

## Introduction

![Teaser](assets/overview.jpg)

The way humans interact with data is undergoing a profound transformation. Data agents — LLM-powered systems designed to orchestrate the Data + AI ecosystem — are emerging as a promising solution for automating and democratizing data-related tasks across the full lifecycle, from management and preparation to analysis.

However, the term "data agent" is currently used inconsistently across research and industry, resulting in considerable ambiguity. Systems with vastly different capabilities in autonomy, reliability, and task complexity are often labeled the same way. This creates a "Babel Tower" crisis where mismatched expectations and unclear accountability threaten to undermine user trust and impede healthy development of the field.

This repository — a companion to our survey — introduces a layered taxonomy (L0-L5) for data agents based on their degree of autonomy, providing a common framework to clarify capability boundaries and lines of accountability at each level.



## Levels of Data Agents

| Level | Name | Human Role | Agent Role |
|:-----:|------|------------|------------|
| L0 | Manual/No Autonomy | Dominator (Solo) | N/A (None) |
| L1 | Assisted | Dominator (Editing) | Assistant (Auxiliary) |
| L2 | Partial Autonomy | Dominator (Orchestrating) | Executor (Procedural) |
| L3 | Conditional Autonomy | Supervisor (Overseeing) | Dominator (Autonomous) |
| L4 | High Autonomy | Onlooker (Delegating) | Dominator (Proactive) |
| L5 | Full Autonomy | N/A (None) | Dominator (Generative) |

## How the List is Organized

We index papers **by autonomy level**, then **by domain**:
- **Domains**: Data Management · Data Preparation · Data Analysis (and sub‑classes).
- **Per paper** we list: *title*, *link*, and *venue*.
- Levels **L4–L5** are aspirational; most existing work clusters in **L1–L3**.

## Paper List

### L0-L1: From Manual Labor to Preliminary Assistance

In L0 level, data-related tasks are performed entirely by human experts without any automation. The process is completely human-driven, requiring extensive domain knowledge and solid technical expertise, making it highly specialized and time-consuming.

At L1 level, data agents start to have the capabilities to provide preliminary and single-point assistance through typical question-answering interactions. While they can help with atomic tasks like code peices generation, they lack environmental perception and require considerable human validation, editing, and optimization.

#### Data Management

##### Autonomous DB

- [Query Rewriting via LLMs](https://arxiv.org/abs/2502.12918) — *arXiv*
- [Query Performance Explanation through LLM for HTAP Systems](https://arxiv.org/abs/2412.01709) — *arXiv*
- [LLM-PM: Training-Free Query Optimization via LLM-Based Plan Mapping](https://arxiv.org/abs/2506.05853) — *arXiv*
- [Database is All You Need: Serving LLMs with Relational DBMS (EDBT'25)](https://openproceedings.org/2025/conf/edbt/paper-326.pdf) — *EDBT'25*

#### Data Preparation

##### Data Cleaning

- [LLMClean: Context-Aware Tabular Data Cleaning via LLM-Generated OFDs](https://arxiv.org/abs/2404.18681) — *arXiv*
- [LLM-GDO: Using Large Language Models for Generic Data Operators](https://arxiv.org/abs/2312.12051) — *arXiv*
- [HAIPipe: Combining Human-generated and Machine-generated Pipelines for Data Preparation (SIGMOD'23)](https://dl.acm.org/doi/10.1145/3588945) — *SIGMOD'23*

##### Data Integration (Entity Matching)

- [BoostER: Harnessing LLMs for Entity Resolution (WWW'24)](https://dl.acm.org/doi/10.1145/3589334.3645418) — *WWW'24*
- [Leveraging Large Language Models for Entity Matching](https://arxiv.org/abs/2407.05547) — *arXiv*
- [Entity Matching using Large Language Models](https://arxiv.org/pdf/2310.11244) — *arXiv*
- [Match, Compare, or Select? An Investigation of Large Language Models for Entity Matching (COLING'25)](https://aclanthology.org/2025.coling-main.8.pdf) — *COLING'25*
- [Cost-Effective In-Context Learning for Entity Resolution (ICDE'24)](https://ieeexplore.ieee.org/document/10598274) — *ICDE'24*

##### Data Integration (Schema/Ontology Matching)

- [Schema Matching with Large Language Models: An Experimental Study (PVLDB'24)](https://arxiv.org/abs/2407.11852) — *PVLDB'24*
- [Magneto: Scaling Schema Matching by Combining Small and Large Language Models](https://arxiv.org/abs/2409.03166) — *arXiv*
- [Large Language Models for JSON Schema Discovery](https://arxiv.org/abs/2407.03286) — *arXiv*
- [LLM-Matcher: Zero-shot Text-to-Relational Schema Matching (VLDB'24 Demo)](https://www.vldb.org/pvldb/vol17/p4556-wu.pdf) — *VLDB'24*
- [Matchmaker: Self-Improving LLM Programs for Schema Matching](https://arxiv.org/abs/2410.24105) — *arXiv*
- [LLMs4SchemaDiscovery: A Human-in-the-Loop Workflow for Scientific Schema Discovery using LLMs](https://arxiv.org/abs/2504.00752) — *arXiv*

#### Data Analysis

##### TableQA (Structured)

- [Table Meets LLM: Can Large Language Models Understand Structured Table Data? A Benchmark and Empirical Study (WSDM'24)](https://dl.acm.org/doi/10.1145/3616855.3635752) — *WSDM'24*
- [TableLlama: Towards Open Large Generalist Models for Tables (NAACL'24)](https://arxiv.org/abs/2311.09206) — *NAACL'24*
- [Tab-CoT: Zero-shot Tabular Chain of Thought (ACL'23 Finding)](https://aclanthology.org/2023.findings-acl.651/) — *ACL'23*

##### NL2SQL (Structured)

- [Evaluating the Text-to-SQL Capabilities of Large Language Models](https://arxiv.org/pdf/2204.00498) — *arXiv*
- [C3: Zero-shot Text-to-SQL with ChatGPT](https://arxiv.org/abs/2307.07306) — *arXiv*
- [DIN-SQL: Decomposed In-Context Learning of Text-to-SQL with Self-Correction (NeurIPS'23)](https://arxiv.org/pdf/2304.11015) — *NeurIPS'23*
- [ACT-SQL: In-context learning for text-to-SQL with automatically-generated chain-of-thought (EMNLP'23 Finding)](https://aclanthology.org/2023.findings-emnlp.227/) — *EMNLP'23*
- [Text-to-SQL Empowered by Large Language Models: A Benchmark Evaluation (VLDB'24)](https://arxiv.org/abs/2308.15363) — *VLDB'24*

##### NL2VIS (Structured)

- [Data2Vis: Automatic Generation of Data Visualizations from Natural Language](https://arxiv.org/abs/1804.03126) — *arXiv*
- [Automated Data Visualization from Natural Language via Large Language Models (SIGMOD'2024)](https://arxiv.org/abs/2404.17136) — *SIGMOD'24*
- [HAIChart: Human and AI Paired Visualization System (PVLDB'24)](https://www.vldb.org/pvldb/vol17/p3178-luo.pdf) — *PVLDB'24*

### L2: Perceive the Environment

At this level, data agents gain environmental perception and tool-invocation capabilities, enabling them to execute bounded sub-tasks and multi-step procedures. While they can follow human-orchestrated workflows, the overall process is still dominated by human direction.

#### Data Management

##### Autonomous DB

- [DB-GPT: Next-Generation Data Interaction System (PVLDB'24 Demo)](https://www.vldb.org/pvldb/vol17/p4365-chen.pdf) — *PVLDB'24*
- [GPTuner: A Manual-Reading Database Tuning System (PVLDB'24)](https://www.vldb.org/pvldb/vol17/p3727-su.pdf) — *PVLDB'24*
- [D-Bot: Database Diagnosis System using Large Language Models (PVLDB'24)](https://www.vldb.org/pvldb/vol17/p4220-wang.pdf) — *PVLDB'24*
- [Automatic Database Configuration Debugging using Retrieval-Augmented LMs](https://arxiv.org/abs/2412.19447) — *arXiv*
- [R-Bot: An LLM-based Query Rewrite System (PVLDB'25)](https://www.vldb.org/pvldb/vol18/p5031-li.pdf) — *PVLDB'25*
- [QUITE: A Query Rewrite System Beyond Rules with LLM Agents](https://arxiv.org/pdf/2506.07675) — *arXiv*

#### Data Preparation

##### Data Cleaning

- [ChatPipe: Orchestrating Data Preparation Pipelines by Optimizing Human–ChatGPT Interactions (SIGMOD'24 Demo)](https://dl.acm.org/doi/10.1145/3626246.3654727) — *SIGMOD'24*
- [CleanAgent: Automating Data Standardization with LLM-based Agents](https://arxiv.org/abs/2403.08291) — *arXiv*
- [AutoDCWorkflow: LLM-based Data Cleaning Workflow Auto-Generation](https://arxiv.org/abs/2412.06724) — *arXiv*
- [Text-to-Pipeline: Bridging Natural Language and Data Preparation Pipelines](https://arxiv.org/abs/2505.15874) — *arXiv*
- [Weak-to-Strong Prompts with Lightweight-to-Powerful LLMs for High-Accuracy, Low-Cost, and Explainable Data Transformation](https://www.vldb.org/pvldb/vol18/p2371-tang.pdf) — *VLDB'24*
- [AutoPrep: Natural Language Question-Aware Data Preparation with a Multi-Agent Framework (VLDB'25)](https://dbgroup.cs.tsinghua.edu.cn/ligl/papers/VLDB25-AutoPrep.pdf) — *VLDB'25*

##### Data Integration (Schema/Ontology Matching)

- [Agent-OM: Leveraging LLM Agents for Ontology Matching (PVLDB'25)](https://www.vldb.org/pvldb/vol18/p516-qiang.pdf) — *PVLDB'25*
- [Knowledge Graph-based Retrieval-Augmented Generation for Schema Matching](https://arxiv.org/pdf/2501.08686) — *arXiv*

#### Data Analysis

##### TableQA (Structured)

- [Binder: Binding Language Models in Symbolic Languages (ICLR'23)](https://arxiv.org/abs/2210.02875) — *ICLR'23*
- [StructGPT: A General Framework for Large Language Model on Structured Data (EMNLP'23)](https://arxiv.org/abs/2305.09645) — *EMNLP'23*
- [ReAcTable: Enhancing ReAct for Table Question Answering (VLDB'24)](https://dl.acm.org/doi/10.14778/3659437.3659452) — *VLDB'24*
- [Table-Critic: A Multi-Agent Framework for Collaborative Criticism and Refinement in Table Reasoning (ACL'25)](https://aclanthology.org/2025.acl-long.853.pdf) — *ACL'25*
- [Large Language Models are Versatile Decomposers: Decomposing Evidence and Questions for Table-based Reasoning (SIGIR'23)](https://dl.acm.org/doi/pdf/10.1145/3539618.3591708) — *SIGIR'23*
- [Chain-of-Table: Evolving Tables in the Reasoning Chain for Table Understanding (ICLR'24)](https://openreview.net/forum?id=4L0xnS4GQM) — *ICLR'24*
- [AutoTQA: Towards Autonomous Tabular Question Answering through Multi-Agent Large Language Models (PVLDB'24)](http://dl.acm.org/doi/10.14778/3685800.3685816) — *PVLDB'24*

##### NL2SQL (Structured)

- [CHASE-SQL: Multi-Path Reasoning and Preference Optimization for Text-to-SQL (ICLR'25)](https://proceedings.iclr.cc/paper_files/paper/2025/file/974ff7b5bf08dbf9400b5d599a39c77f-Paper-Conference.pdf) — *ICLR'25*
- [MAC-SQL: A Multi-Agent Collaborative Framework for Text-to-SQL (COLING'25)](https://arxiv.org/abs/2312.11242) — *COLING'25*
- [Alpha-SQL: Zero-Shot Text-to-SQL using Monte Carlo Tree Search](https://arxiv.org/abs/2502.17248) — *arXiv*
- [ReFoRCE: A Text-to-SQL Agent with Self-Refinement, Consensus Enforcement, and Column Exploration](https://arxiv.org/abs/2502.00675) — *arXiv*
- [ChatBI: Towards Natural Language to Complex Business Intelligence SQL (arXiv'24)](https://arxiv.org/pdf/2405.00527) — *arXiv*

##### NL2VIS (Structured)

- [MatPlotAgent: Method and Evaluation for LLM-Based Agentic Scientific Data Visualization](https://arxiv.org/pdf/2402.11453) — *arXiv*
- [DeepVIS: Bridging Natural Language and Data Visualization Through Step-wise Reasoning (VIS'25)](https://arxiv.org/pdf/2508.01700) — *VIS'25*
- [nvAgent: Automated Data Visualization from Natural Language via Collaborative Agent Workflow (ACL'25)](https://aclanthology.org/2025.acl-long.960/) — *ACL'25*

##### Data Storytelling

- [DataNarrative: Automated Data-Driven Storytelling with Visualizations and Texts (EMNLP'24)](https://aclanthology.org/2024.emnlp-main.1073/) — *EMNLP'24*
- [Multimodal DeepResearcher: Generating Text–Chart Interleaved Reports with an Agentic Framework (arXiv'25)](https://arxiv.org/abs/2506.02454) — *arXiv*

##### Unstructured

- [QUEST: Query Optimization in Unstructured Document Analysis (VLDB'25)](https://arxiv.org/abs/2507.06515) — *VLDB'25*

#### Data System

- [Semantic Operators: A Declarative Model for Rich, AI-Augmented Data Analytics](https://arxiv.org/abs/2407.11418) — *arXiv*
- [LAMBDA: A Large Model Based Data Agent](https://arxiv.org/pdf/2407.17535) — *arXiv*
- [InfiAgent-DABench: Evaluating Agents on Data Analysis Tasks (ICML'24)](https://proceedings.mlr.press/v235/hu24s.html) — *ICML'24*

### L3: Striving for Autonomous Data Agent

L3 level marks a critical transition where data agents evolve from data-related task executors to task directors. They can autonomously decompose high-level goals and orchestrate tailored end-to-end workflows, while humans shift to a supervisory role. Current efforts show progress but are still in early stages (Proto-L3).

#### Data Management

##### Autonomous DB

- [DBAIOps: A Reasoning LLM-Enhanced Database Operation and Maintenance System using Knowledge Graphs](https://arxiv.org/pdf/2508.01136) — *arXiv*
- [GaussMaster: An LLM-based Database Copilot System](https://arxiv.org/pdf/2506.23322) — *arXiv*

#### Data Analysis

##### Unstructured

- [Unify: A System For Unstructured Data Analytics (ICDE'25 & PVLDB'25)](https://www.vldb.org/pvldb/vol18/p5287-wang.pdf) — *PVLDB'25*
- [DataMosaic: Explainable and Verifiable Multi-Modal Data Analytics through Extract–Reason–Verify (arXiv'25)](https://arxiv.org/abs/2504.10036) — *arXiv*

#### Data System

- [AOP: Automated and Interactive LLM Pipeline Orchestration for Answering Complex Queries (CIDR'25)](https://www.cidrdb.org/cidr2025/papers/p32-wang.pdf) — *CIDR'25*
- [Data Interpreter: An LLM Agent For Data Science (Findings ACL'25)](https://aclanthology.org/2025.findings-acl.1016/) — *ACL'25*
- [Chat2Data: An Interactive Data Analysis System with RAG, Vector Databases and LLMs (VLDB'24 demo)](https://dl.acm.org/doi/pdf/10.14778/3685800.3685905) — *VLDB'24*
- [AgenticData: An Agentic Data Analytics System for Heterogeneous Data (arXiv'25)](https://arxiv.org/abs/2508.05002) — *arXiv*
- [DataMosaic: Explainable and Verifiable Multi-Modal Data Analytics through Extract–Reason–Verify (arXiv'25)](https://arxiv.org/abs/2504.10036) — *arXiv*
- [A Holistic Architecture for Orchestrating Data+AI Ecosystems (ICDE'25 Keynote + arXiv'25)](https://arxiv.org/abs/2507.01599) — *arXiv*


### L4-L5: Vision towards Proactive and Generative Data Agents
#### L4: Vision of Proactive Data Agent

At this level, data agents achieve sustained self-governance with proactive monitoring and optimization across the data lifecycle. They can operate autonomously for extended periods without human supervision, actively providing insights and feedback while maintaining reliability.

#### L5: The Ultimate Vision

The ultimate vision of fully autonomous data agents that can function as expert data scientists, capable of cross-domain generalization, knowledge creation, and paradigm innovation. This represents a theoretical endpoint where human involvement becomes optional.


