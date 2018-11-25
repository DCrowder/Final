#!/usr/bin/python

import sys

from my_matrix import *

epsilon = 1e-2  # default e-6


def ortho_basis(A):
    if isinstance(A, mat):
        e = mat()
        u = mat()

        k = 0
        while k < A.get_cols():
            tmp_u = A[k]

            j = 0
            while j <= k-1:
                num = inner(e[j], A[k])
                tmp_s = mult_vec(num, e[j])
                tmp_u = sub_vec(tmp_u, tmp_s)
                j += 1
            if u.get_cols() == 0:
                u = mat(tmp_u)
            else:
                u = mat(u, tmp_u)
            tmp_e = div_vec(tmp_u, norm(tmp_u))
            if e.get_cols() == 0:
                e = mat(tmp_e)
            else:
                e = mat(e, tmp_e)
            k += 1
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


def eigen_transformation(A):

    def norm_sq_of_lower_triangle(A):
        if isinstance(A, mat):
            s = 0.0
            i = 0
            while i < A.get_cols():
                j = i + 1
                while j < A.get_rows():
                    s += A[i][j]*A[i][j]
                    j += 1
                i += 1
            return s

    if isinstance(A, mat):
        Ak = mat(A)
        S = mat(A.get_rows(), A.get_cols())

        i = 0
        while i < S.get_cols():
            S[i][i] = 1.0
            i += 1

        tmp_norm = norm_sq_of_lower_triangle(Ak)

        # print >> sys.stderr, tmp_norm

        while tmp_norm >= epsilon:
            X = QR(Ak)
            Q = X[0]
            R = X[1]
            Ak = inner_prod(R, Q)
            S = inner_prod(S, Q)
            tmp_norm = norm_sq_of_lower_triangle(Ak)
            # print >> sys.stderr, tmp_norm

        return mat(Ak), mat(S)
