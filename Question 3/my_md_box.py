#!/usr/bin/python

from my_matrix import *

class md_box:

    def __name__(self):
        self.name = 'md_box'
        return self.name

    def __init__(self, Lx, Ly=None, Lz=None):
        "The constructor for md_box"

        if isinstance(Lx, float):
            self.box = mat(3, 3)
            self.box[0][0] = Lx
            self.box[1][1] = Lx
            self.box[2][2] = Lx

            if isinstance(Ly, float):
                self.box[1][1] = Ly
            if isinstance(Lz, float):
                self.box[2][2] = Lz
        elif isinstance(Lx, mat):
            if Lx.get_rows() == 3 and Lx.get_cols() == 3:
                self.box = mat(Lx)
        elif isinstance(Lx, md_box):
            self.box = mat(md_box.get())

    def get(self):
        return self.box

# Function that returns the difference vector with periodic boundaries

def dx(x1, x2, b):
    if isinstance(x1, vec) and isinstance(x2, vec) and isinstance(b, md_box):
        dx = sub_vec(x2, x1)

        x = dx[0]
        y = dx[1]
        z = dx[2]

        Lx = b.get()[0][0]
        Ly = b.get()[1][1]
        Lz = b.get()[2][2]

        if x > Lx/2.0:
            x = x - Lx
        if x < -Lx/2.0:
            x = Lx + x
        if y > Ly/2.0:
            y = y - Ly
        if y < -Ly/2.0:
            y = Ly + y
        if z > Lz/2.0:
            z = z - Lz
        if z < -Lz/2.0:
            z = Lz + z

        dx[0]= x
        dx[1]= y
        dx[2]= z

        return norm(dx, "sq"), dx
