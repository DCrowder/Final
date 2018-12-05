#!/usr/bin/python
import sys
from temperature import * 
from evolve import *
from my_vector import *


f = sys.stdin
if isinstance(f, file):
    def ave(x):
        h = int(x)
        k = 0
        s = 0.0
        for k in range(500):
            s += pow((A[int(h * 3)][k] - A[0][k]), 2) + pow((A[int(h * 3 + 1)][k] - A[1][k]), 2) + pow(
                (A[int(h * 3 + 2)][k] - A[2][k]), 2)
        f = float(s / 500)
        return f

    i = 0
    j = 0

    A = mat(10000, 10000)

    # Here A is actually a matrix with 3000 cols and 500 rows,500 rows for 0 to 499 atom,
    # 3000 cols for x y z at t/delta=1000

    while i <= 3000:  # this will be ((total time/(deltat*10)))*3= 3000
        # put every 500 lines(atoms) into one frame 1, each frame takes over 3 cols
        if j < 500:
            s = f.readline()
            if s[0:6] == "ATOM  ":
                # put x y z for atom j into ith, i+1th, i+2th cols.
                A[i][j] = float(s[30:38])
                A[i+1][j] = float(s[39:47])
                A[i+2][j] = float(s[48:56])
                print >> sys.stderr, i, j, A[i][j], A[i+1][j], A[i+2][j]
                j += 1
                if j == 500:
                    j = 0
                    i += 3

    for g in range(1001):  # total time/(delta t*10) +1 =1001
        print >> sys.stdout, .02*g, ave(g)
