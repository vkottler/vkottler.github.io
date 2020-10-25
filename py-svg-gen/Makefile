.PHONY: lint test clean clean-venv

.DEFAULT_GOAL  := run
PYTHON_VERSION := 3.8
SVG_GEN_DIR    := .
BUILD_DIR      := $(SVG_GEN_DIR)/build
VENV_DIR       := $(SVG_GEN_DIR)/venv
PYTHON_BIN     := $(VENV_DIR)/bin

$(BUILD_DIR):
	@mkdir -p $@

$(VENV_DIR):
	python$(PYTHON_VERSION) -m venv $(VENV_DIR)

$(BUILD_DIR)/req-%.txt: $(SVG_GEN_DIR)/%.txt | $(BUILD_DIR) $(VENV_DIR)
	$(PYTHON_BIN)/pip install -r $<
	@date > $@

$(BUILD_DIR)/venv.txt: $(BUILD_DIR)/req-requirements.txt $(BUILD_DIR)/req-dev_requirements.txt
	@date > $@

lint-%: $(BUILD_DIR)/venv.txt
	$(PYTHON_BIN)/$* svg_gen tests main.py

lint: lint-flake8 lint-pylint

run: $(BUILD_DIR)/venv.txt
	$(SVG_GEN_DIR)/main.py -v -o $(BUILD_DIR) render test
	@cat $(BUILD_DIR)/test.svg

test: $(BUILD_DIR)/venv.txt
	$(PYTHON_BIN)/pytest --cov=svg_gen --cov-report html
	@$(BROWSER) htmlcov/index.html

clean:
	find -iname '*.pyc' -delete
	find -iname '__pycache__' -delete
	rm -rf $(BUILD_DIR)
	rm -rf cover .coverage build dist *.egg-info htmlcov .pytest_cache

clean-venv:
	rm -rf $(VENV_DIR) $(BUILD_DIR)/venv.txt
