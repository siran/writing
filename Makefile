.PHONY: serve serveb watch watchb watchp clean

PYTHON_VENV := $(firstword $(wildcard $(VIRTUAL_ENV)/Scripts/python.exe $(VIRTUAL_ENV)/bin/python))
PYTHON := $(if $(PYTHON_VENV),$(PYTHON_VENV),$(shell command -v python 2>/dev/null || command -v python3 2>/dev/null))

ifeq ($(strip $(PYTHON)),)
$(error Could not find a usable Python interpreter. Activate a virtualenv or add `python`/`python3` to PATH.)
endif

clean:
	@echo "removing site/"
	rm -r site || true

buildb:
	@echo "building books..."
	$(PYTHON) .scripts/build_site/build_site.py --skip-pdf --skip-epub --skip-book-markers
buildn:
	@echo "building fast (HTML + dotfile markers)..."
	$(PYTHON) .scripts/build_site/build_site.py --skip-books --skip-pdf --skip-epub
buildp:
	@echo "building PDFs (honor .pdf markers, no books)..."
	$(PYTHON) .scripts/build_site/build_site.py --skip-books --skip-epub --skip-book-markers

serve: buildn
	@echo "serving fast build (HTML only, no books/PDF/EPUB)..."
	$(PYTHON) .scripts/dev_server.py --root site --port 8000
serveb: buildb
	@echo "serving WITH books..."
	$(PYTHON) .scripts/dev_server.py --root site --port 8000
watch: buildn
	@echo "watching fast (HTML only, no books/PDF/EPUB)..."
	$(PYTHON) .scripts/dev_server.py --root site --port 8000 --watch --build-mode fast
watchb: buildb
	@echo "watching books (HTML, no PDF/EPUB)..."
	$(PYTHON) .scripts/dev_server.py --root site --port 8000 --watch --build-mode books
watchp: buildp
	@echo "watching PDFs (honor .pdf markers, no books)..."
	$(PYTHON) .scripts/dev_server.py --root site --port 8000 --watch --build-mode pdf
