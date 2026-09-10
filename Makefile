###############################################################################
# Riemann Research Workspace
###############################################################################

PYTHON := python
PIP := pip
PYTEST := pytest

PAPER_DIR := paper
DOCS_DIR := docs

MAIN_TEX := $(PAPER_DIR)/main.tex

ARCH_MD := $(DOCS_DIR)/architecture_guide.md
ARCH_PDF := $(DOCS_DIR)/architecture_guide.pdf

###############################################################################
# HELP
###############################################################################

.PHONY: help

help:
	@echo ""
	@echo "Riemann Research Workspace"
	@echo ""
	@echo "Available targets:"
	@echo ""
	@echo "  install           Install project"
	@echo "  install-dev       Install development dependencies"
	@echo "  test              Execute pytest suite"
	@echo "  test-zeta         Run zeta tests"
	@echo "  test-zeros        Run zero tests"
	@echo "  lint              Scientific language check"
	@echo "  experiment        Run default experiment"
	@echo "  paper             Compile LaTeX paper"
	@echo "  architecture      Generate architecture PDF"
	@echo "  clean             Remove temporary files"
	@echo ""

###############################################################################
# INSTALLATION
###############################################################################

.PHONY: install

install:
	$(PIP) install -e .

.PHONY: install-dev

install-dev:
	$(PIP) install -e ".[dev]"

###############################################################################
# TESTS
###############################################################################

.PHONY: test

test:
	$(PYTEST) -v

.PHONY: test-zeta

test-zeta:
	$(PYTEST) tests/test_zeta.py -v

.PHONY: test-zeros

test-zeros:
	$(PYTEST) tests/test_zeros.py -v

###############################################################################
# LINTING
###############################################################################

.PHONY: lint

lint:
	$(PYTHON) scripts/check_claim_language.py .

###############################################################################
# EXPERIMENTS
###############################################################################

.PHONY: experiment

experiment:
	$(PYTHON) experiments/001_zeta_sanity/run.py

###############################################################################
# PAPER
###############################################################################

.PHONY: paper

paper:
	cd $(PAPER_DIR) && latexmk -pdf -interaction=nonstopmode main.tex

###############################################################################
# DOCUMENTATION
###############################################################################

.PHONY: architecture

architecture:
	pandoc $(ARCH_MD) \
		--from markdown \
		--to pdf \
		--pdf-engine=xelatex \
		--toc \
		--number-sections \
		-o $(ARCH_PDF)

###############################################################################
# CLEAN
###############################################################################

.PHONY: clean

clean:
	@echo "Cleaning repository..."

	find . -type d -name "__pycache__" -exec rm -rf {} +

	find . -type f -name "*.pyc" -delete

	find $(PAPER_DIR) -type f \( \
	-name "*.aux" -o \
	-name "*.bbl" -o \
	-name "*.bcf" -o \
	-name "*.blg" -o \
	-name "*.fdb_latexmk" -o \
	-name "*.fls" -o \
	-name "*.log" -o \
	-name "*.out" -o \
	-name "*.run.xml" -o \
	-name "*.synctex.gz" -o \
	-name "*.toc" \
	\) -delete

	@echo "Cleanup completed."