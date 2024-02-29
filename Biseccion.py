import numpy as np
import pandas as pd

# ------------------
# DATOS DE ENTRADA DEL MÉTODO DE BISECCIÓN:
# f(X)=0 Y EL INTERVALO [a,b]
# --------------------
f = lambda x: x ** 2 - 3
a = 1
b = 2
tol = 1e-2


def Biseccion(f, a, b, tol):
    if f(a) * f(b) > 0:
        print('La función cumple el teorema')
    else:
        i = 0
        Data = []
        while np.abs(b - a) > tol:
            c = (a + b) / 2
            Data.append([a, b, c, f(a), f(c), np.sign(f(a) * f(c)), np.abs(b - a)])
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
            i += 1
    return c, Data


c, Data = Biseccion(f, a, b, tol)
print('La raiz de la función f es:', c)
D = pd.DataFrame(Data, columns=['a', 'b', 'c', 'f(a)', 'f(c)', 'sgn', '|b-a|'])
print(D)
