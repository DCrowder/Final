#!/usr/bin/python

from my_md_system import *

def temperature(s):
    s.T = 1.0/3.0*s.Ek/float(s.N)/8.31*1000.0*s.epsilon
    return s.T
