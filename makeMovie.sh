#! /bin/sh
ffmpeg -i frame_%06d.png -framerate 16 -b:v 4M wip.mpg
