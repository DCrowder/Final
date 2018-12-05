#!/usr/bin/python

from temperature import *
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


def evolve_Berendsen(t, dt, T_0, s):
    if isinstance(t, float) and isinstance(dt, float) and isinstance(s, md_system):
        i = 0
        while i < s.N:
            
            X = s.atoms[i].X()
            V = s.atoms[i].V()

            term1 = mult_vec(0.5*dt*dt/s.mass, s.atoms[i].F())
            term2 = mult_vec(dt, V)

            X = add_vec(X, add_vec(term1, term2))
            s.atoms[i].X(X)
            i += 1
        Apply_BC(s)
        compute_forces(s)
        s.Ek = 0.0

        i = 0
        while i < s.N:
            V = add_vec(V, mult_vec(0.5*dt/s.mass, add_vec(s.atoms[i].F(), s.atoms[i].F_old())))
            
            s.Ek += 0.5*s.mass*(V[0]*V[0] + V[1]*V[1] + V[2]*V[2])
            s.atoms[i].V(V)
            i += 1
        
        temperature(s)
        lambd = math.sqrt(1.0 + 1.0/5.0 * (s.T/T_0 - 1.0))

        i = 0
        
        while i < s.N:
            V = mult_vec(1.0/lambd, s.atoms[i].V())
            s.Ek += 0.5*s.mass*(V[0]*V[0] + V[1]*V[1] + V[2]*V[2])
            s.atoms[i].V(V)
            i += 1
        return t
