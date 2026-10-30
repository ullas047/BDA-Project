.DEFAULT_GOAL := all
SF ?= 0.01
SEED ?= 2026

all:
	python run.py --scale $(SF) --seed $(SEED)

test:
	pytest -q

serve:
	python -m http.server 8080 --directory dashboard
