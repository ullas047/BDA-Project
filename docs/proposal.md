# EpiScope proposal (M1)

## Problem and stakeholders

EpiScope turns delayed, heterogeneous routine health, weather, population and stock signals into early warnings, 1–4-week forecasts and defensible response allocations. National policymakers need a comparable overview; epidemiologists need transparent thresholds; district officers need actionable forecasts; hospital managers need demand uncertainty; vector-control units need seasonal timing; the public needs prompt protection without re-identification.

## Conflicts and decisions

| Conflict | Decision and evidence plan |
|---|---|
| C1 sensitivity vs specificity | EARS-style rolling threshold; sweep 1–4 sigma and report sensitivity, false alerts and median delay. Default 2 sigma. |
| C2 granularity vs privacy | Aggregate district-week counts; suppress 1–4 and avoid complementary total disclosure. No identifiers after bronze. |
| C3 efficiency vs equity | Allocate severity-weighted need subject to an equity floor; compare five budgets to population-proportional allocation. |
| C4 freshness vs cost | Daily micro-batches: aligns with logistics decisions while tolerating up to 21 days of late reports. |
| C5 accuracy vs interpretability | Start with lagged rolling/seasonal forecasts and report interval coverage against seasonal-naive baseline. |

## Architecture and tools

PySpark performs ingestion, validation, hashing, joins and weekly aggregation. Immutable bronze retains source/checksum/batch metadata; silver removes direct identifiers and quarantines defects; partitioned Parquet gold is the analytics source. A small JSON export feeds a D3 v7-only dashboard. Spark AQE and broadcast facility joins are selected optimisations; their measured before/after evidence belongs in `performance.md`.

## CEP attributes P1–P7

P1 combines distributed data engineering, surveillance statistics, optimisation and visual design. P2 is resolved through the five documented trade-offs. P3 is addressed by backtests, threshold sweeps and baselines. P4 handles late reports, duplicate IDs, orphan facilities and a reporting artefact. P5 applies health coding and privacy principles with local judgement. P6 maps views and safeguards to each stakeholder. P7 preserves lineage from each alert to its bronze batch.

## Roles and risks

Replace placeholders before submission: Data engineer [name/ID]; Analytics engineer [name/ID]; Visualisation engineer [name/ID].

| Risk | Mitigation |
|---|---|
| Laptop memory at SF=1 | Partitioned Parquet, local Spark tuning, scale test early |
| Late/revised reports | Idempotent batch manifest and recomputation of affected weeks |
| False alerts from silent facility | Compare against reporting completeness before escalation |
| Leakage of small counts | Serving-only suppression tests; no line-level browser files |
| Misleading forecasts | intervals, baseline backtest, explicit limitations |

