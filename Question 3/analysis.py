#!/usr/bin/python

import sys
from temperature import *
from evolve import *


def read_frame(f):
    if isinstance(f, file):
        
        s = f.readline()
        atoms = []
        box = md_box(1.0, 1.0, 1.0)
        count = 0

        while s != "" and s[0:3] != "END":
            if s[0:6] == "CRYST1":
                Lx = float(s[6:15])
                Ly = float(s[16:25])
                Lz = float(s[26:35])
            if s[0:6] == "ATOM ":
                x = float(s[30:38])
                y = float(s[39:47])
                z = float(s[48:56])

                atoms.append(md_atom(x, y, z))
                count += 1
            s = f.readline()
        
        return (count, box, atoms)
