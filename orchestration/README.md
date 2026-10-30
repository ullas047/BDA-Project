# Orchestration

`run.py` is the documented portable DAG: generate -> pipeline -> analytics -> serving. Each stage is restartable because bronze manifests are checksum-idempotent.
