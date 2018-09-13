.PHONY: serve view

BROWSER       = firefox
PYTHON_BIN    = python3

serve:
	@$(PYTHON_BIN) -m http.server

view:
	@$(BROWSER) http://localhost:8000/index.html
