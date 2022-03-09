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

.PHONY: edit setup host-svg

.DEFAULT_GOAL := setup

$($(PROJ)_DIR)/svgen:
	ln -s $(GIT_ROOT)/../svgen $@

$($(PROJ)_DIR)/config:
	ln -s $($(PROJ)_DIR)/../svg/config $@

MK_CONC := $(call to_concrete, vmklib-install)
$(MK_CONC): | $(VENV_CONC)
	$(PIP) install --upgrade vmklib
	$(call generic_concrete,$@)

SVGEN_CONC := $(call to_concrete, svgen-editable)
$(SVGEN_CONC): | $(VENV_CONC) $(MK_CONC)
	$(PIP) install -e $(GIT_ROOT)/../svgen
	$(call generic_concrete,$@)

setup: $($(PROJ)_DIR)/svgen $($(PROJ)_DIR)/config $(SVGEN_CONC)

edit: setup $(PY_PREFIX)edit

SCRIPT_DIR := $($(PROJ)_DIR)/$(PROJ)
SVG_DIR := $(BUILD_DIR)/svg

$(SVG_DIR):
	mkdir -p $@

host-svg: | $(SVG_DIR)
	cd $(SVG_DIR) && \
		$(PYTHON) -m http.server 0

script-%: | setup $(SVG_DIR)
	$(PYTHON_BIN)/svgen \
		-c $(SCRIPT_DIR)/$*/json \
		-o $(SVG_DIR)/$*.svg \
		$(SCRIPT_DIR)/$*.py
