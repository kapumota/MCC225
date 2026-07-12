SHELL := /bin/bash

.DEFAULT_GOAL := help

.PHONY: help clean clean-python clean-jupyter clean-tests clean-build \
        clean-generated clean-all check-clean

help:
	@echo "MCC225 - tareas disponibles"
	@echo ""
	@echo "  make check-clean      Muestra archivos temporales encontrados"
	@echo "  make clean            Elimina caches Python, Jupyter y pruebas"
	@echo "  make clean-python     Elimina __pycache__ y archivos compilados"
	@echo "  make clean-jupyter    Elimina .ipynb_checkpoints"
	@echo "  make clean-tests      Elimina caches de herramientas de calidad"
	@echo "  make clean-build      Elimina artefactos de empaquetado"
	@echo "  make clean-generated  Elimina caches y temporales de outputs"
	@echo "  make clean-all        Ejecuta toda la limpieza segura"

check-clean:
	@echo "Artefactos temporales encontrados:"
	@find . \
		-type d \( \
			-name "__pycache__" -o \
			-name ".ipynb_checkpoints" -o \
			-name ".pytest_cache" -o \
			-name ".mypy_cache" -o \
			-name ".ruff_cache" \
		\) \
		-print 2>/dev/null
	@find . \
		-type f \( \
			-name "*.pyc" -o \
			-name "*.pyo" -o \
			-name "*.pyd" \
		\) \
		-print 2>/dev/null

clean: clean-python clean-jupyter clean-tests
	@echo "Limpieza básica completada."

clean-python:
	@find . -type d -name "__pycache__" -prune -exec rm -rf {} +
	@find . -type f \( -name "*.pyc" -o -name "*.pyo" -o -name "*.pyd" \) -delete
	@echo "Caches de Python eliminadas."

clean-jupyter:
	@find . -type d -name ".ipynb_checkpoints" -prune -exec rm -rf {} +
	@echo "Checkpoints de Jupyter eliminados."

clean-tests:
	@find . -type d \( \
		-name ".pytest_cache" -o \
		-name ".mypy_cache" -o \
		-name ".ruff_cache" \
		\) -prune -exec rm -rf {} +
	@find . -type f -name ".coverage" -delete
	@echo "Caches de pruebas y análisis eliminadas."

clean-build:
	@find . -type d \( \
		-name "build" -o \
		-name "dist" -o \
		-name "*.egg-info" -o \
		-name ".eggs" \
		\) -prune -exec rm -rf {} +
	@echo "Artefactos de construcción eliminados."

clean-generated:
	@find . -type d \( \
		-path "*/outputs/cache" -o \
		-path "*/outputs/tmp" -o \
		-path "*/outputs/logs" \
		\) -prune -exec rm -rf {} +
	@echo "Caches, temporales y logs generados eliminados."

clean-all: clean clean-build clean-generated
	@echo "Limpieza completa finalizada."
