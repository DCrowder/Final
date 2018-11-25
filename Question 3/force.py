#!/usr/bin/python

from my_md_system import *

def compute_forces(s):

    def interaction(x1, x2, b):
        if isinstance(x1, vec) and isinstance(x2, vec) and isinstance(b, md_box):
            f = vec(3)
            R = dx(x1, x2, b)
            r_sq = R[0]
            ddx = R[1]
            term = -24.0*(2.0/pow(r_sq, 7) - 1.0/pow(r_sq, 4))
            
            f[0] = term * ddx[0]
            f[1] = term * ddx[1]
            f[2] = term * ddx[2]

            Eu = 2.0 * (1.0/pow(r_sq, 6) - 1.0/pow(r_sq, 3))

            return Eu, f

    if isinstance(s, md_system):
        i = 0
        while i < s.N:
            f = vec(3)
            s.Eu = 0.0

            j = 0
            while j < s.N:
                if j != i:
                    F = interaction(s.atoms[i].X(), s.atoms[j].X(), s.box)
                    Eu = F[0]
                    f1 = F[1]
                    f = add_vec(f, f1)
                    s.Eu += Eu
                j += 1

            s.atoms[i].F_old(s.atoms[i].F())
            s.atoms[i].F(f)
            i += 1
        return

