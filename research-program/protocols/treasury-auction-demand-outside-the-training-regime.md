# Treasury auction demand outside the training regime

**State: protocol only. No result or novelty claim yet.**

## Decision

Do demand models generalize across maturity and auction-size changes after respecting announcement timing?

## Target data

- [Treasury auction query](https://treasurydirect.gov/auctions/auction-query/) — targeted; exact export and rights must be verified.

## Study design

Hierarchical residual forecasts and rolling model comparison.

Rolling-origin test; maturity holdout; announcement-time feature audit; no investment-return claim.

## Contribution to test

Predict auction mechanics rather than backtest a trading strategy with unavailable pre-auction facts. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

time series, quant research, validation, Python. The repository must demonstrate these through executed work before they become portfolio claims.
