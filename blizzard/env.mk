.PHONY: check-env

$($(PROJ)_DIR)/.secrets:
	@rm -f $@
	@echo "export BLIZZ_API_ID=`secrethub read vdoer/keybinds/blizzard/id`" >> $@
	@echo "export BLIZZ_API_SECRET=`secrethub read vdoer/keybinds/blizzard/secret`" >> $@
	@echo "export GITHUB_API_USER=vkottler" >> $@
	@echo "export GITHUB_API_TOKEN=`secrethub read vkottler/github/tokens/public_repo-api-token`" >> $@
	+@echo "wrote '$@'"

check-env: | $($(PROJ)_DIR)/.secrets
ifndef BLIZZ_API_ID
	$(error BLIZZ_API_ID not set, run 'source $($(PROJ)_DIR)/.secrets')
endif
ifndef BLIZZ_API_SECRET
	$(error BLIZZ_API_SECRET not set, run 'source $($(PROJ)_DIR)/.secrets')
endif
ifndef GITHUB_API_USER
	$(error GITHUB_API_USER not set, run 'source $($(PROJ)_DIR)/.secrets')
endif
ifndef GITHUB_API_TOKEN
	$(error GITHUB_API_TOKEN not set, run 'source $($(PROJ)_DIR)/.secrets')
endif
