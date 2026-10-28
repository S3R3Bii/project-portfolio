# Road safety rankings that survive exposure choices

**State: protocol only. No result or novelty claim yet.**

## Decision

Which road-user risk comparisons reverse when the exposure denominator changes?

## Target data

- [NHTSA Fatality Analysis Reporting System](https://www.nhtsa.gov/research-data/fatality-analysis-reporting-system-fars) — targeted; exact export and rights must be verified.
- [US Census data APIs](https://www.census.gov/data/developers/data-sets.html) — targeted; exact export and rights must be verified.

## Study design

Standardization and denominator sensitivity analysis.

Recompute public totals; stratify time and road user; explicitly bound unavailable travel exposure.

## Contribution to test

Make the choice of denominator a visible decision rather than burying it in a footnote. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

R, causal reasoning, measurement, visualization. The repository must demonstrate these through executed work before they become portfolio claims.
