###############################################################################
MK_INFO := https://pypi.org/project/vmklib
ifeq (,$(shell which mk))
$(warning "No 'mk' in $(PATH), install 'vmklib' with 'pip' ($(MK_INFO))")
endif
ifndef MK_AUTO
$(error target this Makefile with 'mk', not '$(MAKE)' ($(MK_INFO)))
endif
###############################################################################

.PHONY: all sync clean serve
.DEFAULT_GOAL = all

SVG_TAR := $(BUILD_DIR)/svg.tar.gz

all: $(SVG_TAR)

$($(PROJ)_DIR)/config:
	ln -s $($(PROJ)_DIR)/../svg/config $@

$(DZ_PREFIX)sync: | $($(PROJ)_DIR)/config

sync: $(DZ_PREFIX)sync

$(SVG_TAR): $(DZ_PREFIX)sync | $(BUILD_DIR)
	@rm -f $@
	cd $(BUILD_DIR)/svg-minified && tar -czvf $@ *.svg
	cd $(BUILD_DIR) && tar xvf $@

clean: $(DZ_PREFIX)clean
	@rm -rf $(BUILD_DIR)/svg-minified
	@rm -rf $(BUILD_DIR)/*.svg
	@rm -f $(SVG_TAR)

serve:
	cd $($(PROJ)_DIR)/datazen-out && python -m http.server 0
