# MLOps Makefile for Enterprise AI Strategy Framework

.PHONY: install test lint docker-build analyze-roi help

install:
	pip install -r requirements.txt

test:
	pytest tests/

lint:
	flake8 advisory/ blueprints/

docker-build:
	docker build -t raymond-ai-framework:latest .

analyze-roi:
	python advisory/tco_engine.py --gpu_count 16 --server_cost 500000 --power_kwh 0.15

help:
	@echo "Enterprise AI Strategy Framework Commands:"
	@echo "  make install      Install dependencies"
	@echo "  make analyze-roi  Run default TCO/ROI analysis"
	@echo "  make docker-build Build NVIDIA-optimized container"
