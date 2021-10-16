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

all: sync

$($(PROJ)_DIR)/config:
	ln -s $($(PROJ)_DIR)/../svg/config $@

$(DZ_PREFIX)sync: | $($(PROJ)_DIR)/config

sync: $(DZ_PREFIX)sync

clean: $(DZ_PREFIX)clean

serve:
	cd $($(PROJ)_DIR)/datazen-out && python -m http.server 0
