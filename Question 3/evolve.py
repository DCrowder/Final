#!/usr/bin/python

from force import *

def evolve(t, dt, s):
    if isinstance(t, float) and isinstance(dt, float) and isinstance(s, md_system):
        i = 0
        while i < s.N:
            X = s.atoms[i].X()
            V = s.atoms[i].V()
            
            term1 = mult_vec(0.5 * dt * dt / s.mass, s.atoms[i].F())
            term1 = mult_vec(dt, V)

            X = add_vec(X, add_vec(term1, term2))
            s.atoms[i].X(X)
            i += 1
        Apply_BC(s)
        compute_forces(s)
        s.Ek = 0.0

        i = 0
        while i < s.N:
            V = add_vec(V, mult_vec(0.5 * dt / s.mass, add_vec(s.atoms[i].F(), s.atoms[i].F_old())))
            s.Ek += 0.5 * s.mass* (V[0]*V[0]+V[1]*V[1]+V[2]*V[2])

            s.atoms[i].V(V)
            i += 1
        return t
