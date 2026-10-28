# Research evidence retrieval with an abstain option

**State: protocol only. No result or novelty claim yet.**

## Decision

Can a transparent retrieval system return the right supporting study and decline weak matches?

## Target data

- [OpenAlex API documentation](https://docs.openalex.org/) — targeted; exact export and rights must be verified.
- [Crossref REST API](https://www.crossref.org/documentation/retrieve-metadata/rest-api/) — targeted; exact export and rights must be verified.

## Study design

Lexical retrieval versus embeddings on a hand-audited question set.

Frozen corpus; independent relevance labels; topic-held-out evaluation; citation verification.

## Contribution to test

Evaluate evidence sufficiency and abstention, not fluent answer generation. This is a proposed contribution, not a verified gap in the literature. Prior work must be reviewed before any novelty claim.

## Evidence to retain

- Exact source snapshot, request, retrieval time, observation window, definitions, units and redistribution terms.
- Prespecified splits, baseline, search space, tuning budget, seed and decision metric.
- All candidate results, including failures; final holdout used only after model selection.
- Independent headline recomputation, leakage checks and reviewed figures with units and uncertainty.
- Reproduction command and environment; private LaTeX manuscript written from measured results.

## Skills

information retrieval, AI evaluation, NLP. The repository must demonstrate these through executed work before they become portfolio claims.
