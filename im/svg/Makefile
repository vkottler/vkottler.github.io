.PHONY: all
.DEFAULT_GOAL = all

# haven't found a good way to avoid this duplication
logo_background_%.png: logo_background.svg
	@inkscape $< -e $@ -w $* -h $*
logo_%.png: logo.svg
	@inkscape $< -e $@ -w $* -h $*
logo_outline_black_%.png: logo_outline_black.svg
	@inkscape $< -e $@ -w $* -h $*

%.ico: %_16.png %_24.png %_32.png %_64.png %_128.png %_256.png
	@icotool -c $^ -o $@

desktop.png: desktop.svg
	@inkscape $< -e $@ -w 1920 -h 1080

all: desktop.png logo_background.ico logo_outline_black.ico logo.ico
