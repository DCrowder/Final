#!/usr/bin/python

from analysis import *
F = read_frame(sys.stdin)
print F[0], F[1].get()
i=0
while i < F[0]:
    print F[2][i].X()
    i += 1

F = read_frame(sys.stdin)
print F[0], F[1].get()
i=0
while i < F[0]:
    print F[2][i].X()
    i += 1

