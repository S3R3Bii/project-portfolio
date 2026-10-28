# Crop-price alerts under changing product grades

**State: protocol only. No result or novelty claim yet.**

## Decision

Can an alert retain precision when reporting markets change product-grade definitions?

## Target data

- [USDA agricultural market reports](https://mymarketnews.ams.usda.gov/) — targeted; exact export and rights must be verified.

## Study design

Schema-aware anomaly detection and hierarchical price models.

Market-held-out and future-period evaluation; grade crosswalk audits.

## Contribution to test

Treat taxonomy drift as part of the model rather than silently concatenating prices. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

data engineering, anomaly detection, forecasting. The repository must demonstrate these through executed work before they become portfolio claims.
