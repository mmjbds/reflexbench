# License Scope

The repository-level Apache-2.0 license applies to source code, schemas, benchmark prompts, documentation, and other original material intentionally released by the repository maintainer, unless a file states otherwise.

It does not relicense third-party model outputs, provider names, trademarks, or material for which the maintainer does not control the underlying rights.

| Path | Public purpose | License or rights boundary |
|---|---|---|
| `scripts/`, `.github/` | Validation and repository automation | Apache-2.0 |
| `reflexbench.jsonl`, `scenarios/` | Maintainer-authored benchmark definitions | Apache-2.0 |
| `responses/` | Third-party model outputs released for artifact inspection | Not covered by the repository Apache-2.0 grant; provider terms and applicable law continue to apply |
| `scoring/*.json`, `scoring/*.csv` | Scores, judge traces, and derived summaries | Maintainer-authored transformations are Apache-2.0; embedded third-party output text is not relicensed |
| `paper/` | Research manuscript and presentation files | No blanket software-license grant; citation and scholarly-use norms apply |
| Provider and model names | Identification of evaluated systems | No trademark rights are granted |

The public presence of a file is not a warranty that every downstream use, redistribution, or commercial use is permitted. Reusers must evaluate the applicable provider terms, local law, privacy obligations, and rights in the underlying generated text.

Provenance gaps are recorded in [`responses/README.md`](responses/README.md). A missing provenance field is an unresolved documentation gap, not permission inferred by silence.
