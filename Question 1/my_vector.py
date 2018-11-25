#!/usr/bin/python

import math

negative_inf = -1e20

# Definition of vectors

class vec:
    def __name__(self):
        self.name='vec'
        return 'vec'

    def __init__(self,dim=None):
        if dim is None:
            self.v = []
            self.dim = 0
        elif isinstance(dim,int):
            self.dim=dim
            self.v=[0.0 for x in range(self.dim)]
        elif isinstance(dim,vec):
            self.dim=dim.get_dim()
            self.v=list(dim.v)
        elif isinstance(dim,list):
            self.dim=len(dim)
            self.v=list(dim)

    def __str__(self):
        s=''
        for x in range(self.dim):
            if(x<self.dim-1):
                s=s+'%1f' % (self.v[x]) + ','
            else:
                s=s+'%1f' % (self.v[x])
        return '%d\n' % (self.dim) + '(' + s + ')\n'

    def get_dim(self):
        return self.dim

    def get(self,i,val=None):
        if i<0 or i>=self.dim:
            print 'get out of range %d out of %d\n' % (i,self.dim-1)
            exit(0)
        else:
            if val is None:
                return self.v[i]
            else:
                self.v[i] = val
                return self.v[i]

    def __setitem__(self,i,val):
        if i<0 or i>=self.dim:
            print '__setitem__ out of range %d out of %d\n' % (i,self.dim-1)
            exit(0)
        else:
            self.v[i]=val
            return self.v[i]

    def __getitem__(self,i):
        if i<0 or i>=self.dim:
            print '__getitem__ out of range %d out of %d\n' % (i,self.dim-1)
            exit(0)
        else:
            return self.v[i]

def add_vec(a,b):
    if isinstance(a,vec) and isinstance(b,vec):
        if a.get_dim()==b.get_dim():
            c=[a[i]+b[i] for i in range(a.get_dim())]
            return vec(c)
        else:
            print 'cannot add vectors with dimensions %d and %d' % (a.get_dim(),b.get_dim())
            exit(0)

def sub_vec(a,b):
    if isinstance(a,vec) and isinstance(b,vec):
        if a.get_dim() == b.get_dim():
            c=[a[i]-b[i] for i in range(a.get_dim())]
            return vec(c)
        else:
            print 'cannot subtract vectors with dimensions %d and %d' % (a.get_dim(), b.get_dim())
            exit(0)

def mult_vec(a,b):
    if isinstance(a,float) and isinstance(b,vec):
        c=[a*b[i] for i in range(b.get_dim())]
        return vec(c)
    elif isinstance(a,int) and isinstance(b,vec):
        c=[a*b[i] for i in range(b.get_dim())]
        return vec(c)
    if isinstance(b,float) and isinstance(a,vec):
        c=[b*a[i] for i in range(a.get_dim())]
        return vec(c)
    elif isinstance(b,int) and isinstance(a,vec):
        c=[b*a[i] for i in range(a.get_dim())]
        return vec(c)

def div_vec(a,b):
    if isinstance(a,vec) and isinstance(b,float):
        c = [a[i]/b for i in range(a.get_dim())]
        return vec(c)
    if isinstance(a,vec) and isinstance(b,int):
        c = [a[i]/b for i in range(a.get_dim())]
        return vec(c)

def norm(a,t=None):
    if isinstance(a,vec):
        if t is None:
            s = 0.0;
            for x in a.v:
                s = s + x*x
            return math.sqrt(s)
        if t is "sq":
            s = 0.0
            for x in a.v:
                s = s + x*x
            return s
        if t is "sup":
            big = negative_inf
            for x in a.v:
                if x >= big:
                    big = x
                return big

def inner(a,b):
    if isinstance(a,vec) and isinstance(b,vec):
        if a.get_dim() == b.get_dim():
            s = 0.0
            for i in range(a.get_dim()):
                s = s + a[i]*b[i]
            return s
