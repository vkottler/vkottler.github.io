.PHONY: all clean
.DEFAULT_GOAL = logo.ico

IMAGE_NAME = logo

$(IMAGE_NAME)_%.png: $(IMAGE_NAME).svg
	@inkscape $< -e $@ -w $* -h $*

%.ico: %_16.png %_24.png %_32.png %_64.png %_128.png %_256.png
	@icotool -c $^ -o $@

clean:
	@rm -f $(IMAGE_NAME)_* $(IMAGE_NAME).ico
