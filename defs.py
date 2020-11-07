import numpy as np


def SUM(a, X):
    out = 0.0
    for i in range(X.size):
        out += X[i]**a
    return out


def SUM2(a, X, Y):
    out = 0.0
    for i in range(X.size):
        out += Y[i]*X[i]**a
    return out


def INSERTB(x, M, B):
    out = np.copy(M)
    for a in range(B.size):
        out[a][x] = B[a][0]
    return out


def POLYREG(x, Xn, A):
    out = 0.0
    for a in range(A.size):
        out += A[a][0]*Xn[x]**a
    return out
