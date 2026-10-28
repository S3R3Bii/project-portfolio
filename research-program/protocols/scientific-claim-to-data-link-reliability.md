# Scientific claim-to-data link reliability

**State: protocol only. No result or novelty claim yet.**

## Decision

Which metadata rules find broken research data links without overwhelming maintainers with false alarms?

## Target data

- [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) — targeted; exact export and rights must be verified.
- [OpenAlex API documentation](https://docs.openalex.org/) — targeted; exact export and rights must be verified.

## Study design

DOI and repository-link resolution with calibrated rules.

Public metadata only; bounded requests; human-checked positive/negative sample; time-separated recheck.

## Contribution to test

A reproducibility maintenance tool whose false positives are measured. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

data engineering, record linkage, research operations. The repository must demonstrate these through executed work before they become portfolio claims.
