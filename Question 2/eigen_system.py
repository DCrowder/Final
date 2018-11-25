#!/usr/bin/python

import sys
from eigen_solvers import *

A = mat(3, 3)

A[0][0] = 1.0; A[1][0] = -3.0; A[2][0] = 3.0;
A[0][1] = 3.0; A[1][1] = -5.0; A[2][1] = 3.0;
A[0][2] = 6.0; A[1][2] = -6.0; A[2][2] = 4.0;

print A

X = eigen_transformation(A)

print X[0], X[1]
