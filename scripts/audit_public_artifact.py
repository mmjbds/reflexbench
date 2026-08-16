from __future__ import annotations

import csv
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "PUBLIC_ARTIFACT_MANIFEST.json"


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    expected = manifest["current_public_github_mirror"]

    scenarios = [
        json.loads(line)
        for line in (ROOT / "reflexbench.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    response_dirs = sorted(path for path in (ROOT / "responses").iterdir() if path.is_dir())
    response_files = sorted((ROOT / "responses").glob("*/*.json"))
    with (ROOT / "scoring" / "aggregate_scores.csv").open(encoding="utf-8", newline="") as handle:
        aggregate_rows = list(csv.DictReader(handle))

    actual = {
        "scenario_records": len(scenarios),
        "prompt_parts": sum(
            sum(part in scenario for part in ("part_a", "part_b", "part_c", "part_d"))
            for scenario in scenarios
        ),
        "raw_response_model_directories": len(response_dirs),
        "raw_response_scenario_files": len(response_files),
        "raw_response_prompt_parts_represented": len(response_files) * 4,
        "aggregate_only_model_rows": len(aggregate_rows),
        "aggregate_observer_depth_cells": len(aggregate_rows) * 4,
        "raw_response_models": [path.name for path in response_dirs],
        "aggregate_only_models": [row["Model"] for row in aggregate_rows],
    }

    errors = []
    for key, value in actual.items():
        if value != expected[key]:
            errors.append(f"{key}: manifest={expected[key]!r}, actual={value!r}")

    reported = manifest["reported_workshop_study"]
    if reported["scenario_count"] * reported["observer_depth_levels"] * reported["model_count"] != reported["scored_prompt_responses"]:
        errors.append("reported study dimensions do not multiply to scored_prompt_responses")

    if errors:
        print("Public artifact audit failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print(
        "Public artifact audit passed: "
        f"{actual['scenario_records']} scenarios, "
        f"{actual['raw_response_model_directories']} raw-response model directories, "
        f"{actual['aggregate_only_model_rows']} aggregate-only model rows."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
