# ReflexBench Supplementary v2

[![public-ci](https://github.com/mmjbds/reflexbench/actions/workflows/public-ci.yml/badge.svg)](https://github.com/mmjbds/reflexbench/actions/workflows/public-ci.yml)
[![License: Apache 2.0](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](LICENSE)

ReflexBench evaluates observer-participant reasoning: whether an AI system continues to reason correctly as its own output changes users, evidence, incentives, institutions, and other actors.

This GitHub repository is a public development mirror. Its namespace, metadata, and commit history are identity-linkable, so it must not be represented or submitted as an anonymous double-blind artifact. When a venue requires anonymity, use only the separate venue-designated archive and follow that venue's current rules.

## Contents

| Path | Description |
|------|-------------|
| `reflexbench.jsonl` | 80 evaluation prompts: 20 scenarios across four observer-depth levels |
| `scenarios/` | Per-scenario JSON descriptions organized by domain |
| `responses/` | Scenario-level raw response files for four evaluated models (20 files per model; each file contains four prompt parts) |
| `scoring/aggregate_scores.csv` | Four observer-depth means for five additional evaluated models; not per-scenario raw responses |
| `scoring/` | Released score summaries and supporting files |
| `ablations/moe_vs_dense/` | MoE-versus-dense comparison scores |
| `audit/` | Scenario-to-provided-corpus text-disjointness audit |
| `judge_robustness/` | Multi-judge agreement, rank association, and judge-bias checks |

The workshop study reports nine models and 720 scored prompt responses. This public mirror currently exposes different evidence depths for those models: scenario-level raw response files for four models and aggregate observer-depth means for five additional models. It does not contain per-scenario raw responses and per-item scores for all nine models. The machine-readable [public artifact manifest](PUBLIC_ARTIFACT_MANIFEST.json) and CI audit keep that distinction explicit.

Validate the released coverage contract locally with:

```bash
python scripts/audit_public_artifact.py
```

Frozen public version: [`v2.0.0-public.1`](https://github.com/mmjbds/reflexbench/releases/tag/v2.0.0-public.1). Verify selected files against [RELEASE_MANIFEST.json](RELEASE_MANIFEST.json); changes are recorded in [CHANGELOG.md](CHANGELOG.md).

## Interactive Entry

The browser-based [ReflexBench Observer-Depth Check](https://mianzhang.org/demos/reflexbench-observer-depth/) loads all 20 released scenarios and four prompt levels. It creates a local orientation receipt from user-selected causal lenses. The receipt is not an automated ReflexBench score.

## Recompute Public Checks

| Check | Public route | Supported interpretation |
|-------|--------------|--------------------------|
| Scenario/corpus disjointness | `audit/scenario_corpus_disjoint.json` | No detected scenario overlap against the provided comparison corpus under the documented check; not full training-lineage proof |
| Inter-judge agreement | `judge_robustness/inter_judge_kappa.json` | Fleiss kappa reported as 0.69 for the included judge panel and sample |
| Ranking association | `judge_robustness/inter_judge_kappa.json` | Kendall tau values reported at or above 0.86 for the included judges; not universal judge independence |
| MoE/dense comparison | `ablations/moe_vs_dense/moe_vs_dense_scores.csv` | Architecture comparison under the included conditions; not a general MoE premium |

The separate anonymous archive route recorded for venue review is:
https://anonymous.4open.science/r/reflexbench-24E0

The public GitHub mirror and the anonymous venue archive have different roles. Do not substitute one for the other.

## Claim Boundary

The artifact supports recomputation and audit under the released scenarios, responses, judge configurations, and scoring files. It does not establish production trustworthiness, causal deployment effects, complete training-data provenance, universal judge independence, or general architectural superiority. See [CLAIM_BOUNDARY.md](CLAIM_BOUNDARY.md).

## Contributing

Public scenario extensions, artifact mismatches and narrow claim-boundary repairs are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) and use the issue forms. Do not post private logs, credentials, customer data, restricted material or identity-sensitive review artifacts.

- Scenario proposal: https://github.com/mmjbds/reflexbench/issues/new?template=scenario_proposal.yml
- Artifact mismatch: https://github.com/mmjbds/reflexbench/issues/new?template=artifact_mismatch.yml
- Private security route: [SECURITY.md](SECURITY.md)

## License

Maintainer-authored code, schemas, prompts, and documentation are under Apache-2.0 unless a file states otherwise. Third-party model outputs are not relicensed by that grant. See [LICENSE_SCOPE.md](LICENSE_SCOPE.md), [responses/README.md](responses/README.md), and [LICENSE](LICENSE).
