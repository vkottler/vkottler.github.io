#!/bin/bash

CWD=.

OUT=$CWD/build/png

mkdir -p $OUT
inkscape $CWD/build/svg/$1.svg -e $OUT/$1_$2_$3.png -w $2 -h $3
