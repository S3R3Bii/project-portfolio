# Plant-level fuel efficiency and dispatch mix

## Source-readiness update — 29 October 2026

Unreleased: the fixed source-key and plant-year CHP-classification gate failed before decomposition. Read the [bounded source hold](../source-holds/study25-chp-key-conflict.md). No completed study counted.

**State: protocol only. No result or novelty claim yet.**

## Decision

How much of a change in fleet heat rate comes from plant operation versus changing generation shares?

## Target data

- [EIA electricity generator inventory](https://www.eia.gov/electricity/data/eia860/) — targeted; exact export and rights must be verified.
- [EIA power plant operations](https://www.eia.gov/electricity/data/eia923/) — targeted; exact export and rights must be verified.

## Study design

Index decomposition and uncertainty-aware peer comparison.

Plant-generator key checks; unit reconciliation; matched-fleet sensitivity.

## Contribution to test

Separate operational improvement from composition effects in energy reporting. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

SQL, decomposition, energy analytics. The repository must demonstrate these through executed work before they become portfolio claims.
