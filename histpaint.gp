set term aqua
#set terminal postscript eps enhanced
#set output "history_painting.eps"

unset key
unset xtics
unset ytics

set yrange[0:1]
set samples 38
set boxwidth 0.85
#set style fill solid 0.5
set style fill solid 1.0 border -1

plot "red.dat" with boxes lc rgb "red", "green.dat" with boxes lc rgb "green", "black.dat" with boxes lc rgb "black"