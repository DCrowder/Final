#!/usr/bin/python

import sys
from evolve import *

if len(sys.argv) < 2:
    print "Usage: ", sys.argv[0], " <Temperature float>"
    exit(0)

T_0 = float(sys.argv[1])

s = md_system(500, 10.0, 10.0, 10.0, 39.96, 3.4, 0.997, T_0)

t = 0.0
dt = 0.002

count = 0

compute_forces(s)

while t <= 20:
    print >> sys.stderr, t*s.tau, s.epsilon * s.Ek / float(s.N), s.epsilon * s.Eu/float(s.N), s.T
    evolve_Berendsen(t, dt, T_0, s)
    temperature(s)
    
    if count%10 == 0:
        print s

    count += 1
    t += dt
