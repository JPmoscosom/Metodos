suma = 1
error = 1
n = 1
while abs(error) > 10**-6:
    suma = suma + 0.5**n
    n += 1
    error = 2 - suma
print(n-1)
