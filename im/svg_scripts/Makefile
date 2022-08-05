# =====================================
# generator=datazen
# version=1.13.4
# hash=9f51ee84fc4074d84a64f7dcae923c31
# =====================================
###############################################################################
MK_INFO := https://pypi.org/project/vmklib
ifeq (,$(shell which mk))
$(warning "No 'mk' in $(PATH), install 'vmklib' with 'pip' ($(MK_INFO))")
endif
ifndef MK_AUTO
$(error target this Makefile with 'mk', not '$(MAKE)' ($(MK_INFO)))
endif
###############################################################################

.PHONY: edit setup host-svg edit-deps

.DEFAULT_GOAL := setup

$($(PROJ)_DIR)/config:
	ln -s $($(PROJ)_DIR)/../svg/config $@

$($(PROJ)_DIR)/%:
	ln -s $(GIT_ROOT)/../svgen/$* $@

MK_CONC := $(call to_concrete, vmklib-install)
$(MK_CONC): | $(VENV_CONC)
	$(PIP) install --upgrade vmklib
	$(call generic_concrete,$@)

SVGEN_CONC := $(call to_concrete, svgen-editable)
$(SVGEN_CONC): | $(VENV_CONC) $(MK_CONC)
	$(PIP) install -e $(GIT_ROOT)/../svgen
	$(call generic_concrete,$@)

LINKS := $($(PROJ)_DIR)/svgen \
	 $($(PROJ)_DIR)/config \
	 $($(PROJ)_DIR)/.flake8

# Generate tags for 'svgen' sources.
setup: $(LINKS) $(SVGEN_CONC)

# This is a copy of the dependencies for '$(PY_PREFIX)edit'.
edit-deps: $(BUILD_DIR)/$(VENV_NAME)/edit_venv.txt $(PY_PREFIX)tags | $(VENV_CONC)
	ctags -f $($(PROJ)_DIR)/tags -a -R $($(PROJ)_DIR)/svgen

edit: setup edit-deps
	. $(VENV_ACTIVATE) && cd $($(PROJ)_DIR) && $(EDITOR)

SCRIPT_DIR := $($(PROJ)_DIR)/$(PROJ)
SVG_DIR := $(BUILD_DIR)/svg

$(SVG_DIR):
	mkdir -p $@

host-svg: | $(SVG_DIR)
	cd $(SVG_DIR) && \
		$(PYTHON) -m http.server 0

SCRIPT_ARGS ?=

script-%: | setup $(SVG_DIR)
	@$(PYTHON_BIN)/svgen \
		$(SCRIPT_ARGS) \
		-c $(SCRIPT_DIR)/$*.json \
		-o $(SVG_DIR)/$*.svg \
		$(SCRIPT_DIR)/$*.py
