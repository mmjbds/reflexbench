# ReflexBench Supplementary v2

[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

ReflexBench evaluates observer-participant reasoning: whether an AI system continues to reason correctly as its own output changes users, evidence, incentives, institutions, and other actors.

This repository is an anonymized supplementary artifact for a double-blind 2026 submission. Do not add author identities, personal homepages, institutional clues, or cross-links that can de-anonymize the submission while review is active.

## Contents

| Path | Description |
|------|-------------|
| `reflexbench.jsonl` | 80 evaluation prompts: 20 scenarios across four observer-depth levels |
| `scenarios/` | Per-scenario JSON descriptions organized by domain |
| `responses/` | Raw responses for nine evaluated public LLMs |
| `scoring/` | Judge scripts and rubric definitions |
| `ablations/moe_vs_dense/` | MoE-versus-dense comparison scores |
| `audit/` | Scenario-to-provided-corpus text-disjointness audit |
| `judge_robustness/` | Multi-judge agreement, rank association, and judge-bias checks |

## Recompute Public Checks

| Check | Public route | Supported interpretation |
|-------|--------------|--------------------------|
| Scenario/corpus disjointness | `audit/scenario_corpus_disjoint.json` | No detected scenario overlap against the provided comparison corpus under the documented check; not full training-lineage proof |
| Inter-judge agreement | `judge_robustness/inter_judge_kappa.json` | Fleiss kappa reported as 0.69 for the included judge panel and sample |
| Ranking association | `judge_robustness/inter_judge_kappa.json` | Kendall tau values reported at or above 0.86 for the included judges; not universal judge independence |
| MoE/dense comparison | `ablations/moe_vs_dense/moe_vs_dense_scores.csv` | Architecture comparison under the included conditions; not a general MoE premium |

The anonymous archive route recorded for the review artifact is:
https://anonymous.4open.science/r/reflexbench-24E0

## Claim Boundary

The artifact supports recomputation and audit under the released scenarios, responses, judge configurations, and scoring files. It does not establish production trustworthiness, causal deployment effects, complete training-data provenance, universal judge independence, or general architectural superiority. See [CLAIM_BOUNDARY.md](CLAIM_BOUNDARY.md).

## License

Intentionally released repository code and artifact files are under Apache-2.0 unless a file states otherwise. See [LICENSE](LICENSE).
