# ReflexBench v1.0

**The first benchmark for evaluating reflexive reasoning in large language models.**

## What is Reflexive Reasoning?

Existing AI benchmarks (MMLU, HumanEval, GSM8K, MATH) evaluate capabilities in **observer-invariant** domains where the correct answer is independent of the agent. Yet many consequential real-world systems—financial markets, policy-making, content recommendation, epidemiology—are **observer-participant environments** where the agent's actions alter the ground truth it aims to predict.

**ReflexBench** measures whether LLMs can reason about their own causal impact on the environments they analyze.

## The Soros Test

We propose the **Soros Test**: *given a scenario where the agent's own actions alter the system being analyzed, does the model spontaneously account for its own causal impact?*

No current LLM reliably passes the Soros Test at Observer Depth 2+.

## Benchmark Structure

- **20 scenarios** across **6 domains**: Financial Markets, Policy & Governance, Social Technology, Healthcare, Autonomous Systems, Education & Labor
- **4 Observer Depth levels** per scenario:
  - **OD-0**: Surface decision-making
  - **OD-1**: First-order impact awareness
  - **OD-2**: Multi-agent reflexive modeling
  - **OD-n**: Equilibrium reasoning

## Key Results

We evaluated **9 LLMs** spanning 9 providers:

| Model | OD-0 | OD-1 | OD-2 | OD-n | Total | Δ |
|-------|------|------|------|------|-------|---|
| Gemini 2.5 Pro | **1.00** | **0.95** | **0.85** | 0.45 | 3.25 | -0.33 |
| Claude Opus 4.6 | 0.93 | 0.88 | 0.75 | **0.63** | **3.19** | -0.43 |
| DeepSeek-R1 | 0.90 | 0.85 | 0.70 | 0.55 | 3.00 | -0.50 |
| Kimi-K2 (Thinking) | 0.88 | 0.83 | 0.68 | 0.53 | 2.92 | -0.50 |
| Doubao-Seed-2.0 | 0.90 | 0.83 | 0.65 | 0.45 | 2.83 | -0.47 |
| GLM-5.1 | 0.88 | 0.80 | 0.65 | 0.50 | 2.83 | -0.53 |
| Qwen3 | 0.85 | 0.78 | 0.60 | 0.48 | 2.71 | -0.55 |
| MiniMax-Text-01 | 0.63 | 0.58 | 0.38 | 0.38 | 1.95 | -0.43 |
| Mimo-V2-Pro | 0.70 | 0.70 | 0.53 | 0.45 | 2.38 | -0.43 |

**All models exhibit systematic degradation at higher observer depths** (mean Δ = -0.44).

## Four Failure Modes

1. **The Textbook Trap** (31%): Models correctly identify reflexive concepts but fail to apply them to their own situation
2. **The Convergence Abort** (38%): Models enumerate levels of recursion then abort the analysis
3. **The Enumeration Fallacy** (19%): Models produce exhaustive lists rather than analyzing convergence or impossibility
4. **The Perspective Collapse** (12%): Models collapse all adversaries into a single "rational agent" instead of modeling heterogeneous strategic responses

## Repository Structure

```
reflexbench/
├── README.md
├── scenarios/          # 20 benchmark scenarios with rubrics
│   ├── financial/      # F01-F08
│   └── non_financial/  # NF01-NF12
├── responses/          # Complete model responses
│   ├── gemini_2_5_pro/
│   ├── claude_opus/
│   ├── deepseek_r1/
│   ├── kimi_k2/
│   ├── doubao_seed/
│   ├── glm_5_1/
│   ├── qwen3/
│   ├── minimax_text_01/
│   └── mimo_v2_pro/
├── scoring/            # Scoring rubrics and results
│   └── aggregate_scores.csv
└── paper/              # LaTeX source
    └── paper2_reflexbench.tex
```

## Citation

```bibtex
@inproceedings{anonymous2026reflexbench,
  title={ReflexBench: Measuring Observer Depth in Large Language Models via Phase Transition Analysis},
  author={Anonymous},
  booktitle={NeurIPS 2026 Evaluations \& Datasets Track},
  year={2026}
}
```

## Dataset

The dataset is also available on HuggingFace: [reflexbench](https://huggingface.co/datasets/maga666/reflexbench)

## License

CC BY 4.0
