import numpy as np
import matplotlib.pyplot as plt

M = np.array([0.052, 0.124, 0.168, 0.236, 0.284, 0.336])
phi = np.array([0.1745, 0.3491, 0.5236, 0.6981, 0.8727, 1.0472])


n = len(phi)
x_mean = np.mean(phi)
y_mean = np.mean(M)
xy_mean = np.mean(phi * M)
x_kvadrat_mean = np.mean(phi ** 2)

nagib = (xy_mean - x_mean * y_mean) / (x_kvadrat_mean - x_mean ** 2)
presjek = y_mean - nagib * x_mean

Dt = nagib

print("Modul torzije Dt =", Dt)

plt.plot(phi, M, 'o', label='Originalni podaci')
plt.plot(phi, presjek + nagib * phi, 'r', label='Linearna regresija')
plt.xlabel('kut')
plt.ylabel('moment sile')
plt.legend()
plt.show()
