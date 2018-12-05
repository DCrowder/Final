#!/usr/bin/python

import random

from my_matrix import *
from my_md_box import *
from my_md_atom import *

class md_system:
    def __name__(self):
        self.name = "md_system"
        return self.name

    def __init__(self, N, Lx, Ly, Lz, mass=None, sigma=None, epsilon=None, flag=None):
        "The constructor for md_system"
        self.Ek = 0.0
        self.Eu = 0.0
        self.T = 0.0
        self.P = 0.0
        if not isinstance(N, int) or not isinstance(Lx, float) or not isinstance(Ly, float) or not isinstance(Lz, float):
            exit(0)
        self.N = N
        self.box = md_box(Lx, Ly, Lz)
        a = md_atom()
        self.atoms = [md_atom(a) for x in range(self.N)]
        self.mass = 1.0
        self.sigma = 1.0
        self.epsilon = 1.0

        if isinstance(mass, float):
            self.mass = mass
        if isinstance(sigma, float):
            self.sigma = sigma
        if isinstance(epsilon, float):
            self.epsilon = epsilon

        self.tau = 0.1 * self.sigma * math.sqrt(1.0/self.epsilon)  # Added 11/14 class

        # Depending on flag place the atoms either randomly or on lattice
        count = 0
        while count < self.N:
            x = random.uniform(0.0, Lx)
            y = random.uniform(0.0, Ly)
            z = random.uniform(0.0, Lz)
            a = md_atom(x, y, z)
            self.atoms[count] = a
            
            mu = math.sqrt(self.N*8.31e-3*flag/self.mass)

            vx = random.gauss(mu, 1.0)
            vy = random.gauss(mu, 1.0)
            vz = random.gauss(mu, 1.0)

            V = vec(3)
            V[0] = vx
            V[0] = vx
            V[0] = vx

            self.atoms[count].V(V)
            count += 1

    def __str__(self):
        b = self.box.get()
        s1 = 'CRYST1%9.3f%9.3f%9.3f%7.2f%7.2f%7.2f%11s%4d\n' % (self.sigma*b[0][0], self.sigma*b[1][1], self.sigma*b[2][2], 90.0, 90.0, 90.0, " ", 0)
        name = "Ar"
        s = ""
        count = 0
        while count < self.N:
            s += 'ATOM %5d %4s%c%3s %c%4d%c  %8.3f%8.3f%8.3f%6.2f%6.2f    %-4s%2s%2s\n' % (count, name, ' ', "MDX", ' ', 1, ' ', self.sigma*self.atoms[count].X()[0], self.sigma*self.atoms[count].X()[1], self.sigma*self.atoms[count].X()[2], 1.0, 0.0, "0", name, "")
            count += 1
            s += "END"
            return s1 + s

def Apply_BC(s):
    Lx = s.box.get()[0][0]
    Ly = s.box.get()[1][1]
    Lz = s.box.get()[2][2]

    i = 0
    while i < s.N:
        x = s.atoms[i].X()[0] % Lx
        y = s.atoms[i].X()[1] % Ly
        z = s.atoms[i].X()[2] % Lz

        if x < 0:
            x += Lx
        if x > Lx:
            x -= Lx
        if y < 0:
            y += Ly
        if y > Ly:
            y -= Ly
        if z < 0:
            z += Lz
        if z > Lz:
            z -= Lz

        X = vec(3)

        X[0] = x
        X[1] = y
        X[2] = z

        s.atoms[i].X(X)

        i += 1

    return s
