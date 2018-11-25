set encoding iso
set term postscript portrait enhanced color solid "Times-BoldItalic" 16
set output "energy.eps"

set size square

set xrange[0:15]
set yrange[0:*]
set xtics 0,2
set ytics 1,2

set xlabel "n"
set ylabel "{E_n} (h{/Symbol w}/2 {/Symbol p})"

plot "C:/Users/dcrowder/PycharmProjects/Final/Question 2/qharmonic.out" u 1:3 t "" w lp