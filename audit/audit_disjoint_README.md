# Audit: ReflexBench evaluation prompts disjoint from training corpus

This audit supports App. C ("Scenario Provenance and Training-Set Hash Check") of the main paper.

## How to reproduce

1. From the main repository, run the scenario regeneration pipeline (released
   alongside the paper) to obtain the full 1,332-prompt training corpus.
2. Compute SHA-256 of each prompt: `find . -name '*.json' -exec shasum -a 256 {} \;`
3. Compute SHA-256 of each ReflexBench scenario in `scenarios/`.
4. Run `python3 scoring/audit_disjoint.py` (released) -- it expects two hash
   files and outputs a disjointness report.

The released pipeline produces the same hashes as `scenario_corpus_disjoint.json`.

## Why this matters

Reviewers asked: "is the trained MoE arm's lead in Table 3 caused by overlap
between training prompts and benchmark scenarios?" This audit provides
deterministic evidence that the answer is no.
