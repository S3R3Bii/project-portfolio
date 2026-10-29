# Research evidence retrieval with an abstain option

## Execution update — 29 October 2026

A scoped study is executed and released at https://github.com/S3R3Bii/research-paper-recommender. Working explainable local UI, CLI and API plus learner exercise and reference solution. Frozen Jaccard threshold 0.3 recovers a deposited citation in the top five for 12/29 evaluable held queries (41.4%), exactly matching the simple baseline; all 29 are answered. It abstains on 8/8 authored unrelated controls. Only 86/536 catalog titles enter citation scoring; 17 held no-hit suggestions remain unjudged. No human relevance or claim-support certification. Read its fixed executable protocol, complete exclusions and validation. The broader proposal below is retained as historical design context; it is not the release specification. Independent program manuscripts are public after checks; separate formal-publication projects remain private.

**Historical proposal, superseded by the scoped release above.**

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
