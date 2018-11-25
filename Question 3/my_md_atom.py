#!/usr/bin/python

from my_matrix import *


class md_atom:
    def __name__(self):
        self.name = 'md_atom'
        return self.name

    def __init__(self, x=None, v=None, f=None, f_old=None):
        "The constructor for md_atom"

        if x is None and v is None and f is None and f_old is None:
            self.x = vec(3)
            self.v = vec(3)
            self.f = vec(3)
            self.f_old = vec(3)
        elif isinstance(x, vec) and v is None and f is None and f_old is None:
            self.x = vec(x)
            self.v = vec(3)
            self.f = vec(3)
            self.f_old = vec(3)
        elif isinstance(x, vec) and isinstance(v, vec) and f is None and f_old is None:
            self.x = vec(x)
            self.v = vec(v)
            self.f = vec(3)
            self.f_old = vec(3)
        elif isinstance(x, vec) and isinstance(v, vec) and isinstance(f, vec) and f_old is None:
            self.x = vec(x)
            self.v = vec(v)
            self.f = vec(f)
            self.f_old = vec(3)
        elif isinstance(x, vec) and isinstance(v, vec) and isinstance(f, vec) and isinstance(f_old, vec):
            self.x = vec(x)
            self.v = vec(v)
            self.f = vec(f)
            self.f_old = vec(f_old)
        elif isinstance(x, float) and isinstance(v, float) and isinstance(f, float) and f_old is None:
            self.x = vec(3)
            self.x[0] = x
            self.x[1] = v
            self.x[2] = f
            self.v = vec(3)
            self.f = vec(3)
            self.f_old = vec(3)

    def X(self, x=None):
        if x is None:
            return self.x
        else:
            self.x = vec(x)
            return self.x

    def V(self, x=None):
        if x is None:
            return self.v
        else:
            self.v = vec(x)
            return self.v

    def F(self, x=None):
        if x is None:
            return self.f
        else:
            self.f = vec(x)
            return self.f

    def F_old(self, x=None):
        if x is None:
            return self.f_old
        else:
            self.f_old = vec(x)
            return self.f_old
