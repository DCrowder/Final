set encoding iso
set term postscript enhanced color solid "Times-BoldItalic" 16
set output "psi.eps"

set zeroaxis
set xrange [-5.5:5.5]
set yrange [-0.25:0.25]
set xtics -5,1.0

set xlabel "x {(h/2{/Symbol p}m{/Symbol w})^{\275}}"
set ylabel "{/Symbol y}(x)"

plot "/home/dcrowder/PycharmProjects/Final/Question 2/finite_well.out" u 2:4 t "n=0" w l, "" u 2:5 t "n=1" w l, "" u 2:6 t "n=2" w l, "" u 2:7 t "n=3" w l, "" u 2:8 t "n=4" w l, "" u 2:9 t "n=5" w l, "" u 2:10 t "n=6" w l