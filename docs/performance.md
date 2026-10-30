# Performance experiment plan (ENG-2, ENG-3)

Run `make all SF=0.25`, `SF=0.5`, and `SF=1` on the same 16GB laptop, recording machine, Spark version, stage runtimes and bronze/silver/gold sizes in the table below. Capture the Spark UI SQL and stages pages for the report.

| SF | ingest | silver/quality | gold | analytics | total | bronze GB | silver GB | gold GB |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| .25 | pending | pending | pending | pending | pending | pending | pending | pending |
| .5 | pending | pending | pending | pending | pending | pending | pending | pending |
| 1 | pending | pending | pending | pending | pending | pending | pending | pending |

Optimisation A: broadcast the small facility registry to avoid a shuffle join. Optimisation B: partition gold by epidemiological year/division for pruning and enable adaptive query execution for Dhaka skew. Record before/after wall-clock values and Spark UI screenshots; do not replace these placeholders with unmeasured claims.
