# Disaster assistance reporting latency

**State: protocol only. No result or novelty claim yet.**

## Decision

How long must analysts wait before a county-level disaster spending comparison becomes stable?

## Target data

- [OpenFEMA data sets](https://www.fema.gov/about/openfema/data-sets) — targeted; exact export and rights must be verified.

## Study design

Revision curves and snapshot-stability analysis.

Historical snapshots required; if unavailable report a data-availability study instead of reconstructed vintages.

## Contribution to test

Evaluate the reliability of early dashboards rather than claiming spending causes recovery. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

data provenance, time series, public finance. The repository must demonstrate these through executed work before they become portfolio claims.
