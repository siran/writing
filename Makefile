.PHONY: serve serveb watch watchb clean

PYTHON_VENV := $(firstword $(wildcard $(VIRTUAL_ENV)/Scripts/python.exe $(VIRTUAL_ENV)/bin/python))
PYTHON := $(if $(PYTHON_VENV),$(PYTHON_VENV),$(shell command -v python 2>/dev/null || command -v python3 2>/dev/null))

ifeq ($(strip $(PYTHON)),)
$(error Could not find a usable Python interpreter. Activate a virtualenv or add `python`/`python3` to PATH.)
endif

clean:
	@echo "removing site/"
	rm -r site || true

buildb:
	@echo "building ..."
	$(PYTHON) .scripts/build_site/build_site.py
buildn:
	@echo "building fast (build HTML, skip PDFs/EPUBs)..."
	$(PYTHON) .scripts/build_site/build_site.py --skip-pdf --skip-epub

serve: buildn
	@echo "serving fast build (book HTML, no PDF/EPUB)..."
	$(PYTHON) .scripts/dev_server.py --root site --port 8000
serveb: buildb
	@echo "serving WITH books..."
	$(PYTHON) .scripts/dev_server.py --root site --port 8000
watch: buildn
	@echo "watching fast build (book HTML, no PDF/EPUB)..."
	$(PYTHON) .scripts/dev_server.py --root site --port 8000 --watch --build-mode fast
watchb: buildb
	@echo "watching full build (attempt PDF/EPUB too)..."
	$(PYTHON) .scripts/dev_server.py --root site --port 8000 --watch --build-mode full
