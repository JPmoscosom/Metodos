import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
from math import factorial

x = sp.symbols('x')
f = sp.exp(x) * sp.sin(2 * x)
N = 3  # Grado del polinomio
xo = 0  # Construccion de polinomio alrededor alrededor del centro xo
Sum = 0
for k in range(N + 1):
    df = sp.diff(f, x, k)
    df = sp.lambdify(x, df)
    T = df(xo) / factorial(k) * (x - xo) ** k
    Sum = Sum + T
print(Sum)

X = np.arange(0, 3, 0.01)
poly = sp.lambdify(x, Sum)
func = sp.lambdify(x, f)

print('P(0.5)=', poly(0.5), 'f(0.5)=', func(0.5), 'Error=', np.abs((poly(0.5) - func(0.5))))
plt.plot(X, poly(X), 'r', X, func(X))
plt.show()
