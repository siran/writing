.PHONY: serve serveb watch watchb build buildb clean

PYTHON_VENV := $(firstword $(wildcard $(VIRTUAL_ENV)/Scripts/python.exe $(VIRTUAL_ENV)/bin/python))
PYTHON := $(if $(PYTHON_VENV),$(PYTHON_VENV),$(shell command -v python 2>/dev/null || command -v python3 2>/dev/null))

ifeq ($(strip $(PYTHON)),)
$(error Could not find a usable Python interpreter. Activate a virtualenv or add `python`/`python3` to PATH.)
endif

clean:
	@echo "removing site/"
	rm -r site || true

build:
	@echo "building (concatenated book HTML + .pdf markers, no EPUB)..."
	$(PYTHON) .scripts/build_site/build_site.py --skip-pdf --skip-epub
buildb:
	@echo "building with EPUB (book HTML + EPUB + .pdf markers, no book PDFs)..."
	$(PYTHON) .scripts/build_site/build_site.py --skip-pdf

serve: build
	@echo "serving..."
	$(PYTHON) .scripts/dev_server.py --root site --port 8000
serveb: buildb
	@echo "serving with EPUB..."
	$(PYTHON) .scripts/dev_server.py --root site --port 8000
watch: build
	@echo "watching (concatenated book HTML + .pdf markers)..."
	$(PYTHON) .scripts/dev_server.py --root site --port 8000 --watch --build-mode books
watchb: buildb
	@echo "watching with EPUB..."
	$(PYTHON) .scripts/dev_server.py --root site --port 8000 --watch --build-mode epub
