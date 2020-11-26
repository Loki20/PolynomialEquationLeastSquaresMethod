# This code uses Neutrium webpage as a guide check they full article here: https://neutrium.net/mathematics/least-squares-fitting-of-a-polynomial/
# In order to use the code just change the X and Y datasets with your data
# Written by: TheLoki2020
# Date: November 7th 2020

import numpy as np
import defs as f
import matplotlib.pyplot as plt


# DATA
X = np.array([-3, -2, -1, -0.2, 1, 3])
Y = np.array([0.9, 0.8, 0.4, 0.2, 0.1, 0])
k = 2  # Polynomial order

# Arrays for plotting
Xn = np.linspace(np.min(X), np.max(X), 2000)
Yn = np.empty(2000)

# Matrices
M = np.empty([k+1, k+1])
B = np.empty([k+1, 1])
A = np.empty([k+1, 1])

# Filing matrices
for x in range(k+1):
    for y in range(k+1):
        M[x][y] = f.SUM(x+y, X)
    if x == 0:
        B[x][0] = f.SUM(1, Y)
    else:
        B[x][0] = f.SUM2(x, X, Y)

for x in range(A.size):
    A[x][0] = (np.linalg.det(f.INSERTB(x, M, B)))/(np.linalg.det(M))

# Printing the output equation on console
out = " y = "
for x in range(A.size):
    if x == 0:
        if A[x][0] < 0:
            out += "- " + str((A[x][0])*-1)
        else:
            out += str(A[x][0])
    else:
        if A[x][0] < 0:
            out += " - " + str((A[x][0])*-1) + " * x**" + str(x)
        else:
            out += " + " + str(A[x][0]) + " * x**" + str(x)

print(out)

# Filing plotting arrays
for x in range(Yn.size):
    Yn[x] = f.POLYREG(x, Xn, A)

# Plotting
plt.plot(X, Y, 'or')
plt.plot(Xn, Yn)
plt.show()
