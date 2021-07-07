# =====================================
# generator=datazen
# version=1.3.4
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

.PHONY: bapi-sync host validate start

.DEFAULT_GOAL := bapi-sync

include $($(PROJ)_DIR)/env.mk

$(BUILD_DIR)/blizzard:
	@mkdir -p $@
	@touch $@

$(BUILD_DIR)/blizzard/generic.json: $($(PROJ)_DIR)/generic.json | $(BUILD_DIR)/blizzard
	cp -f $< $@

start: check-env | $(VENV_CONC)
	sudo -E $(PYTHON_BIN)/python server.py

bapi-sync: check-env | $(VENV_CONC) $(BUILD_DIR)/blizzard/generic.json
	$(PYTHON_BIN)/bapi -v -o $(BUILD_DIR)/cache
	cp $(BUILD_DIR)/cache/*.json $(BUILD_DIR)/blizzard

host:
	cd $($(PROJ)_DIR)/static  && python -m http.server

validate: | $(VENV_CONC)
	$(PYTHON_BIN)/html5validator --root $($(PROJ)_DIR)/static --also-check-css

config: $(BUILD_DIR)/blizzard/generic.json
	ln -s ../im/svg/$@ $@

clean-logs:
	rm $($(PROJ)_DIR)/*.log
