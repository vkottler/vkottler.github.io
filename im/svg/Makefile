.PHONY: all
.DEFAULT_GOAL = all

# haven't found a good way to avoid this duplication
logo_background_%.png: logo_background.svg
	@inkscape $< -e $@ -w $* -h $*
logo_%.png: logo.svg
	@inkscape $< -e $@ -w $* -h $*
logo_embroider_%.png: logo_embroider.svg
	@inkscape $< -e $@ -w $* -h $*
logo_outline_black_%.png: logo_outline_black.svg
	@inkscape $< -e $@ -w $* -h $*
logo_outline_white_%.png: logo_outline_white.svg
	@inkscape $< -e $@ -w $* -h $*

%.ico: %_16.png %_24.png %_32.png %_64.png %_128.png %_256.png
	@icotool -c $^ -o $@

desktop.png: desktop.svg
	@inkscape $< -e $@ -w 1920 -h 1080

banner.png: banner.svg
	@inkscape $< -e $@ -w 1584 -h 396

business_card_%.png: business_card_%.svg
	@inkscape $< -e $@ -w 1085 -h 635

logo_circular_%.png: logo_circular.svg
	@inkscape $< -e $@ -w $* -h $*

DEPS  = desktop.png
DEPS += logo_background.ico
DEPS += logo_outline_black.ico
DEPS += logo.ico
DEPS += logo_500.png
DEPS += logo_outline_black_500.png
DEPS += logo_outline_white_500.png
DEPS += banner.png
DEPS += business_card_front.png business_card_back.png
DEPS += logo_circular_510.png
DEPS += logo_embroider_500.png

all: $(DEPS)
