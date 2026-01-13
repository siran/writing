.PHONY: serve clean


clean:
	@echo "removing site/"
	rm -r site || true

buildb:
	@echo "building ..."
	.scripts/build_site/build_site.py
buildn:
	@echo "building fast (skip PDFs/EPUBs and book renders)..."
	.scripts/build_site/build_site.py --skip-books --skip-pdf --skip-epub

serve: buildn
	@echo "serving fast build (no book renders, no PDF/EPUB)..."
	python3 -m http.server -d site 8000
serveb: buildb
	@echo "serving WITH books..."
	python3 -m http.server -d site 8000
