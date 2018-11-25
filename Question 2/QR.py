#!/usr/bin/python

import sys
from my_matrix import *

def ortho_basis(A):
    if isinstance(A,mat):
        e = mat()
        u = mat()
        
        k = 0
        while k < A.get_cols():
            tmp_u = A[k]

            j = 0
            while j <= k - 1:
                num = inner(e[j], A[k])
                tmp_s = mult_vec(num,e[j])
                tmp_u = sub_vec(tmp_u,tmp_s)
                j = j + 1

            if u.get_cols() == 0:
                u = mat(tmp_u)
            else:
                u = mat(u,tmp_u)
            tmp_e = div_vec(tmp_u, norm(tmp_u))
            if e.get_cols() == 0:
                e = mat(tmp_e)
            else:
                e = mat(e,tmp_e)
            k = k + 1
        return mat(e)
def QR(A):
    Q = ortho_basis(A)
    R = mat(Q.get_rows(), Q.get_cols())

    i = 0
    while i < Q.get_cols():
        j = 0
        while j <= i:
            val = inner(Q[j], A[i])
            R[i][j] = val
            j = j + 1
        i = i + 1

    return mat(Q), mat(R)

A = mat(3, 3)

A[0][0] = 1.0; A[0][1] = 0.0; A[0][2] = 0.0
A[1][0] = 0.0; A[1][1] = 1.0; A[1][2] = 1.0
A[1][0] = 1.0; A[2][1] = 1.0; A[2][2] = 0.0

print A

X = QR(A)
Q = X[0]
R = X[1]
Qt = transpose(Q)

print Q, R, inner_prod(Qt, A), inner_prod(Qt, Q)
