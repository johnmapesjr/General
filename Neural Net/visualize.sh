for i in `seq -w 1000`;do echo set terminal png';' plot '"'sin$i.dat'"' |gnuplot > sin$i.png;done

#animate -coalesce `echo sin*.png|sort -n`
avconv -r 100 -f image2 -i sin%04d.png sin.avi
