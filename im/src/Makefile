###############################################################################
MK_INFO := https://pypi.org/project/vmklib
ifeq (,$(shell which mk))
$(warning "No 'mk' in $(PATH), install 'vmklib' with 'pip' ($(MK_INFO))")
endif
ifndef MK_AUTO
$(error target this Makefile with 'mk', not '$(MAKE)' ($(MK_INFO)))
endif
###############################################################################

.PHONY: all sync clean serve unpack renders pngs host-pngs
.DEFAULT_GOAL = all

SVG_TAR := $(BUILD_DIR)/svg.tar.gz
PNG_TAR := $(BUILD_DIR)/png.tar.gz

all: $(SVG_TAR)

$($(PROJ)_DIR)/config:
	ln -s $($(PROJ)_DIR)/../svg/config $@

$(DZ_PREFIX)sync: | $($(PROJ)_DIR)/config

renders: | $($(PROJ)_DIR)/config $(DZ_CONC)
	$(PYTHON_BIN)/dz $(DZ_ARGS) groups-all-renders

pngs: | $($(PROJ)_DIR)/config $(DZ_CONC)
	$(PYTHON_BIN)/dz $(DZ_ARGS) groups-all-pngs
	mkdir -p $(BUILD_DIR)/pngs
	-mv $(DZ_DIR)/*.png $(BUILD_DIR)/pngs/

$(PNG_TAR): pngs | $(BUILD_DIR)
	@rm -f $@
	cd $(BUILD_DIR)/pngs && tar -czvf $@ *.png

host-pngs: $(PNG_TAR)
	cd $(BUILD_DIR)/pngs && $(PYTHON_BIN)/python -m http.server 0

sync: $(DZ_PREFIX)sync

$(SVG_TAR): $(DZ_PREFIX)sync | $(BUILD_DIR)
	@rm -f $@
	cd $(BUILD_DIR)/svg-minified && tar -czvf $@ *.svg

unpack: $(SVG_TAR)
	cd $(BUILD_DIR) && tar xvf $<
	cd $(BUILD_DIR) && $(PYTHON_BIN)/python -m http.server 0

clean: $(DZ_PREFIX)clean
	@rm -rf $(BUILD_DIR)/svg-minified
	@rm -rf $(BUILD_DIR)/pngs
	@rm -rf $(BUILD_DIR)/*.svg
	@rm -f $(SVG_TAR) $(PNG_TAR)

serve:
	cd $(DZ_DIR) && $(PYTHON_BIN)/python -m http.server 0
