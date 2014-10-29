#!/bin/bash
rm *png
./Main.py |grep -f pat|sed -e 's/Board is //' -e 's/ .*$//'|while read line;do echo python ~/Downloads/fen-0.1.8/fen.py $line --outfile $i.png;((i++));done|sh
animate --coalesce -delay 50 `ls -v *png`
convert -delay 1 `ls -v *png` game.gif
