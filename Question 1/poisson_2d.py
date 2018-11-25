#!/usr/bin/python

import sys
from my_matrix import *

epsilon = 1e-2


def apply_BC(x, n_x, n_y):
    i = 0
    while i < n_x:
        alpha=index_1d(i,0,n_x)
        x[alpha] = 0.0
        alpha = index_1d(i, n_y-1, n_x)
        x[alpha] = 0.0
        i = i + 1
    j = 0
    while j < n_y:
        alpha = index_1d(j, 0, n_x)
        x[alpha] = 0.0
        alpha = index_1d(i, n_x - 1, n_x)
        x[alpha] = 0.0
        j = j + 1
    return x


def gauss_seidel_withBC(a, b, n_x, n_y):
    if isinstance(a,mat) and isinstance(b,vec):
        if a.get_cols() == b.get_dim():
            x = vec(b.get_dim())
            x_n = vec(b.get_dim())

            for i in range(x_n.get_dim()):
                x_n[i] = 10.0

            nn = norm(sub_vec(x, x_n))

            while nn > epsilon:
                for i in range(b.get_dim()):
                    s1 = 0.0
                    j = 0
                    while j < i:
                        s1 = s1 + a[j][i]*x[j]
                        j = j+1
                    s2 = 0.0
                    j = i+1
                    while j < x.get_dim():
                        s2 = s2 + a[j][i]*x_n[j]
                        j = j+1
                    x_n[i] = (b[i] - s1 - s2)/float(a[i][i])

                tmp = x
                x = x_n
                x_n = tmp

                apply_BC(x, n_x, n_y)
                nn = norm(sub_vec(x, x_n))
                print >> sys.stderr, nn
            return x


def index_1d(i,j,n_x):
    return i*n_x+j


def index_2d(alpha, n_x):
    return alpha/n_x, alpha % n_x


def Q(i, j, x_max, y_max, delta):
    x_dist = math.exp(-pow((i * delta - x_max / 2.0), 2) / (1.0 * delta * delta))
    y_dist = math.exp(-pow((j * delta - x_max / 2.0), 2) / (1.0 * delta * delta))
    return x_dist*y_dist


C0 = 1.6e-19  # SI Units C
phi0 = 1.0  # Let's say V
epsilon0 = 8.85e-12  # SI units

chi = C0/(phi0*epsilon0)

x_max = 10.0
y_max = 10.0

n_x = 20
n_y = 20
N = n_x*n_y

#  For this delta to be the same in x and y,
#  n_x/n_y must be the same as x_max/y_max
delta = x_max/float(n_x)

A = mat(N, N)
b = vec(N)

# Setup A and b

# i = j = 0 condition
alpha = index_1d(0, 0, n_x)
A[alpha][alpha] = 4.0
A[index_1d(1, 0, n_x)][alpha] = -1.0
A[index_1d(0, 1, n_x)][alpha] = -1.0
b[alpha] = Q(0, 0, x_max, y_max, delta)/delta

# i = 0, j = n_y - 1 condition
alpha = index_1d(0, n_y-1, n_x)
A[alpha][alpha] = 4.0
A[index_1d(1, n_y-1, n_x)][alpha] = -1.0
A[index_1d(0, n_y-2, n_x)][alpha] = -1.0
b[alpha] = Q(0, n_y-1, x_max, y_max, delta)/delta

# i = n_x - 1, j = n_y - 1 condition
alpha = index_1d(n_x-1, n_y-1, n_x)
A[alpha][alpha] = 4.0
A[index_1d(n_x-2, n_y-1, n_x)][alpha] = -1.0
A[index_1d(n_x-1, n_y-2, n_x)][alpha] = -1.0
b[alpha] = Q(n_x-1, n_y-1, x_max, y_max, delta)/delta

# i = n_x - 1, j = 0 condition
alpha = index_1d(n_x-1, 0, n_x)
A[alpha][alpha] = 4.0
A[index_1d(n_x-2, 0, n_x)][alpha] = -1.0
A[index_1d(n_x-1, 1, n_x)][alpha] = -1.0
b[alpha] = Q(n_x-1, 0, x_max, y_max, delta)/delta

# 0 < j < n_y - 1
j = 1

while j < n_y - 1:
    # i = 0 condition
    alpha = index_1d(0, j, n_x)
    A[alpha][alpha] = 4.0
    A[index_1d(1, j, n_x)][alpha] = -1.0
    A[index_1d(0, j-1, n_x)][alpha] = -1.0
    A[index_1d(0, j+1, n_x)][alpha] = -1.0
    b[alpha] = Q(0, j, x_max, y_max, delta)/delta

    # i = n_x - 1 condition
    alpha = index_1d(n_x-1, j, n_x)
    A[alpha][alpha] = 4.0
    A[index_1d(n_x-2, j, n_x)][alpha] = -1.0
    A[index_1d(n_x-1, j-1, n_x)][alpha] = -1.0
    A[index_1d(n_x-1, j+1, n_x)][alpha] = -1.0
    b[alpha] = Q(n_x-1, j, x_max, y_max, delta) / delta

    j = j+1

# 0 < i < n_x - 1 condition
i = 1

while i < n_x - 1:
    # j = 0 condition
    alpha = index_1d(i, 0, n_x)
    A[alpha][alpha] = 4.0
    A[index_1d(i-1, 0, n_x)][alpha] = -1.0
    A[index_1d(i+1, 0, n_x)][alpha] = -1.0
    A[index_1d(i, 1, n_x)][alpha] = -1.0
    b[alpha] = Q(i, 0, x_max, y_max, delta)/delta

    # j = n_y - 1 condition
    alpha = index_1d(i, n_y-1, n_x)
    A[alpha][alpha] = 4.0
    A[index_1d(i-1, n_y-1, n_x)][alpha] = -1.0
    A[index_1d(i+1, n_y-1, n_x)][alpha] = -1.0
    A[index_1d(i, n_y-2, n_x)][alpha] = -1.0
    b[alpha] = Q(i, n_y-1, x_max, y_max, delta)/delta

    j = 1
    while j < n_y - 1:
        alpha = index_1d(i,j,n_x)
        A[alpha][alpha] = 4.0
        A[index_1d(i-1, j, n_x)][alpha] = -1.0
        A[index_1d(i+1, j, n_x)][alpha] = -1.0
        A[index_1d(i, j-1, n_x)][alpha] = -1.0
        A[index_1d(i, j+1, n_x)][alpha] = -1.0
        b[alpha] = Q(i, j, x_max, y_max, delta) / delta
        j = j+1

    i = i + 1


phi = gauss_seidel_withBC(A ,b, n_x, n_y)

alpha = 0

while alpha < N:
    pair = index_2d(alpha,n_x)
    print pair[0]*delta*chi*1.0e9, pair[1]*delta*chi*1.0e9, phi[alpha]*phi0, b[alpha]
    alpha = alpha + 1
