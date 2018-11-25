#!/usr/bin/python

from my_vector import *

class mat:

    def __name__(self):
        self.name = 'mat'
        return 'mat'

    def __init__(self,rows=None,cols=None):
        if rows is None and cols is None:
            self.rows=0
            self.cols=0
            self.m=[[]]
        elif isinstance(rows,int) and isinstance(cols,int):
            self.rows=rows
            self.cols=cols
            v=vec(self.rows)
            self.m=[vec(v) for x in range(self.cols)]
        elif isinstance(rows,vec) and isinstance(cols,vec):
            if rows.get_dim()==cols.get_dim():
                self.rows=rows.get_dim()
                self.cols=2
                self.m=[vec(rows),vec(cols)]
            else:
                print "Cannot form matrix with %d and %d dimensional vectors" % (rows.get_dim(), cols.get_dim())
                exit(0)
        elif isinstance(rows,vec) and cols is None:
            self.rows=rows.get_dim()
            self.cols=1
            self.m=[vec(rows)]
        elif isinstance(rows,mat) and isinstance(cols,vec):
            if rows.get_rows()==cols.get_dim():
                self.rows=rows.get_rows()
                self.cols=rows.get_cols()+1
                m1=[vec(rows[i]) for i in range(rows.get_cols())]
                m1.extend([vec(cols)])
                self.m=m1
            else:
                print "Dimension %d of vector is not the same as the number of rows %d of matrix" % (cols.get_dim(), rows.get_rows())
                exit(0)
        elif isinstance(rows,mat) and cols is None:
            self.rows = rows.get_rows()
            self.cols = rows.get_cols()
            m1=[vec(rows[i]) for i in range(rows.get_cols())]
            self.m=m1
        elif isinstance(rows,mat) and isinstance(cols,mat):
            if rows.get_rows()==cols.get_rows():
                self.rows = rows.get_rows()
                self.cols = rows.get_cols()+cols.get_cols()
                m1=[vec(rows[i]) for i in range(rows.get_cols())]
                m2=[vec(cols[i]) for i in range(cols.get_cols())]
                m1.extend(m2)
                self.m=m1
            else:
                print "Number of rows %d and %d are not the same" % (rows.get_rows(),cols.get_rows())
                exit(0)

    def __str__(self):
        s1='\n'
        for i in range(self.rows):
            s=''
            for j in range(self.cols):
                if(j<self.cols-1):
                    s=s+'%1f'%(self.m[j][i])+'\t'
                else:
                    s=s+'%1f'%(self.m[j][i])
            s1=s1+'|'+s+'|\n'
        return s1

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def __setitem__(self,i,val):
        if isinstance(val,vec):
            if i < self.cols and i >= 0:
                self.m[i] = vec(val)
                return self.m[i]

    def __getitem__(self,i):
        if i < self.cols and i >= 0:
            return self.m[i]

def add_mat(a,b):
    if isinstance(a,mat) and isinstance(b,mat):
        if a.get_rows() == b.get_rows() and a.get_cols() == b.get_cols():
            c = mat(a.get_rows(),a.get_cols())
            for i in range(a.get_cols()):
                for j in range(a.get_rows()):
                    c[i][j]=a[i][j]+b[i][j]
            return c
        else:
            print "Cannot add matrices of different sizes"
            exit(0)
    
def sub_mat(a,b):
    if isinstance(a,mat) and isinstance(b,mat):
        if a.get_rows() == b.get_rows() and a.get_cols() == b.get_cols():
            c = mat(a.get_rows(),a.get_cols())
            for i in range(a.get_cols()):
                for j in range(a.get_rows()):
                    c[i][j]=a[i][j]-b[i][j]
            return c
        else:
            print "Cannot subtract matrices of different sizes"

def mult_mat(a,b):
    if (isinstance(a,float) or isinstance(a,int)) and isinstance(b,mat):
        c=mat(b.get_rows(),b.get_cols())
        for i in range(b.get_cols()):
           c[i][j]=a*b[i][j]
        return c
    elif (isinstance(b,float) or isinstance(b,int)) and isinstance(a,mat):
        c = mat(a.get_rows(),a.get_cols())
        for i in range(a.get_cols()):
           for j in range(a.get_rows()):
               c[i][j]=b*a[i][j]
        return c

def transpose(a):
    if isinstance(a,mat):
        c=mat(a.get_cols(),a.get_rows())
        for i in range(a.get_cols()):
            for j in range(a.get_rows()):
                c[j][i]=a[i][j]
        return c

def inner_prod(a,b):
    if isinstance(a,mat) and isinstance(b,mat):
        if a.get_cols() == a.get_rows():
            c = mat(a.get_rows(),b.get_cols())
            for i in range(a.get_rows()):
                for j in range(b.get_cols()):
                    s = 0.0
                    for k in range(a.get_cols()):
                        s = s + a[k][i]*b[j][k]
                    c[j][i]=s
            return c
        else:
            print "Cannot take inner product here"
            exit(0)
    if isinstance(a,mat) and isinstance(b,vec):
        if a.get_cols() == b.get_dim():
            c = vec(a.get_rows())
            for i in range(a.get_rows()):
                s = 0.0
                for k in range(a.get_cols()):
                    s = s + a[k][i]*b[k]
                    c[i] = s
            return c
        else:
            print "Cannot take inner product"
            exit(0)
