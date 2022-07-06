#!/bin/bash

CWD=.

OUT=$CWD/build/png
SVG=$CWD/build/svg

mkdir -p $OUT

if [ ! -L $SVG/png ]; then
	ln -s ../png $SVG/png
fi

if [ $# -ne 3 ]; then
	echo "usage: to_png.sh <script_name> <width_px> <height_px>"
fi

inkscape $CWD/build/svg/$1.svg -e $OUT/$1_$2_$3.png -w $2 -h $3
