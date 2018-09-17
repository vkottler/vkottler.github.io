.PHONY: all
.DEFAULT_GOAL = all

logo_background_%.png: logo_background.svg
	@inkscape $< -e $@ -w $* -h $*

logo_%.png: logo.svg
	@inkscape $< -e $@ -w $* -h $*

%.ico: %_16.png %_24.png %_32.png %_64.png %_128.png %_256.png
	@icotool -c $^ -o $@

desktop.png: desktop.svg
	@inkscape $< -e $@ -w 1920 -h 1080

all: desktop.png logo_background.ico logo.ico
