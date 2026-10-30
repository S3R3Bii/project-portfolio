# Commercial building energy residuals

## Execution update — 30 October 2026

A scoped study is executed and released at https://github.com/S3R3Bii/building-energy-review. With 20 review slots among 192 screened buildings, the peer-relative and largest-consumption lists share only 2 properties. Median floor areas are 41,062.5 and 707,905.0 square feet. A local CSV scorer compares peer, consumption and EUI rankings. On 119 held annual pairs, peer MAE is 22.958 versus 26.547 pooled and 9.773 own-history. Nine of 20 peer selections lack usable next-year follow-up. Engineering usefulness and savings remain unmeasured. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

## Decision

Can peer-adjusted energy-use residuals identify buildings worth an engineering review without ranking them on size alone?

## Target data

- [NYC energy and water benchmarking](https://www.nyc.gov/site/buildings/codes/benchmarking.page) — targeted; exact export and rights must be verified.
- [NOAA integrated surface observations](https://www.ncei.noaa.gov/products/land-based-station/integrated-surface-database) — targeted; exact export and rights must be verified.

## Study design

Robust GAM and gradient-boosted residual benchmarks.

Building-held-out and future-year test; weather normalization; floor-area quality checks.

## Contribution to test

Use calibrated review bands and abstention for implausible records. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

R, ML, regression diagnostics, business communication. The repository must demonstrate these through executed work before they become portfolio claims.
