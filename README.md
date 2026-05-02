# ReflexBench Supplementary v2 (NeurIPS 2026 Datasets & Benchmarks Track)

This v2 supplementary supersedes the v1 release of 2026-04-29 by adding two
new audit appendices that strengthen the self-evaluation disclosure of the
main paper.

## Contents (additions in v2 marked with [NEW])

| Path | Description |
|------|-------------|
| `reflexbench.jsonl`              | All 80 evaluation prompts (20 scenarios x 4 OD levels) |
| `scenarios/`                     | Per-scenario JSON descriptions, organised by domain |
| `responses/`                     | Raw model responses for the 9 evaluated public LLMs |
| `scoring/`                       | LLM-as-judge scoring scripts and rubric definitions |
| `ablations/moe_vs_dense/`        | MoE vs Dense ablation scores (App. A of main paper) |
| `audit/` [NEW]                   | SHA-256 disjointness check between ReflexBench scenarios and Trained MoE training corpus (supports App. C) |
| `judge_robustness/` [NEW]        | 3-judge Cohen's kappa + Fleiss kappa + per-judge bias permutation test (supports App. B) |

## Reproduce key claims

| Claim | Path |
|-------|------|
| Trained MoE arm did not see ReflexBench at training time | `audit/scenario_corpus_disjoint.json` |
| LLM judge agreement is substantial (kappa = 0.69 Fleiss) | `judge_robustness/inter_judge_kappa.json` |
| 9-model ranking is judge-independent (Kendall tau >= 0.86) | `judge_robustness/inter_judge_kappa.json` |
| MoE provides architectural premium | `ablations/moe_vs_dense/moe_vs_dense_scores.csv` |

## Anonymisation

This supplementary contains no author identifiers. All file paths are
relative; no usernames, machine names, or training cluster identifiers are
present. The anonymous repository is at:
https://anonymous.4open.science/r/reflexbench-24E0
