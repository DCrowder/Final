#!/usr/bin/python

from eigen_solvers import *


def get_index(x, xmin, xmax, n):
    return int(float(n - 1) / float(xmax - xmin) * (x - xmin))


def get_inv_index(i, xmin, xmax, n):
    return float(xmax - xmin) / float(n - 1) * i + xmin


def get_potential(x):
    if abs(x) > 2:  # if outside well
        return 0
    else:  # if inside well
        return -5


xmin = -5.0
xmax = 5.0

n = 100  # 100 default

delta = float(xmax - xmin) / float(n)
delta1 = float(xmax - xmin) / float(n - 1)

A = mat(n, n)

A[0][0] = 2.0 + get_potential(xmin) * delta * delta
A[1][0] = -1.0

A[n - 1][n - 1] = 2.0 + get_potential(xmax) * delta * delta
A[n - 2][n - 1] = -1.0

i = 1
while i < n - 1:
    A[i][i] = 2.0 + get_potential((i*delta1)+xmin) * delta * delta
    A[i + 1][i] = -1.0
    A[i - 1][i] = -1.0
    i += 1

X = eigen_transformation(A)

i = 0
while i < n - 1:
    print >> sys.stdout, "%d\t%1f\t%1f\t%1f\t%1f\t%1f\t%1f\t%1f\t%1f\t%1f\t%1f\t%1f\t%1f" \
          % (i, get_inv_index(i, xmin, xmax, n),
             X[0][n - 1 - i][n - 1 - i] / (2.0 * delta * delta),
             X[1][n - 1][i], X[1][n - 2][i], X[1][n - 3][i], X[1][n - 4][i], X[1][n - 5][i],
             X[1][n - 6][i], X[1][n - 7][i], X[1][n - 8][i], X[1][n - 9][i], X[1][n - 10][i])
    i += 1
