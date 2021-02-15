#!/bin/bash

SVG_LOC=datazen-out
OUT_LOC=../png/logo
SVG=.svg

mkdir -p $OUT_LOC

for LOGO_SIZE in 16 24 32 64 128 256 512
do
	for FILE in $SVG_LOC/logo*$SVG
	do
		BASENAME="$(basename -- $FILE $SVG)"
		inkscape $FILE -e $OUT_LOC/$BASENAME\_$LOGO_SIZE.png -w $LOGO_SIZE -h $LOGO_SIZE
	done
done

# TODO, use icotool to create icons, probably just do this in make
