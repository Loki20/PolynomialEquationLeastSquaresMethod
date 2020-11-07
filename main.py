import numpy as np
import defs as f
import matplotlib.pyplot as plt


# DATA
X = np.array([0.08279, 0.41415, 0.82851, 1.24302, 1.65767, 2.07242, 2.48726, 2.90216, 3.31709, 3.73203, 4.14696])
Y = np.array([200, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000])
k = 5  # Polynomial order

# Arrays for plotting
Xn = np.linspace(np.min(X), np.max(X), 200)
Yn = np.empty(200)

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

print(A)

# Filing plotting arrays
for x in range(Yn.size):
    Yn[x] = f.POLYREG(x, Xn, A)

# Plotting
plt.plot(X, Y, 'or')
plt.plot(Xn, Yn)
plt.show()
