import numpy as np
import matplotlib.pyplot as plt


F = float(input("unesi silu: "))
m = float(input("unesi masu: "))

x0 = 0
v0 = 0

t = np.linspace(0, 10, 1000)
dt = t[1] - t[0]

def f(x, v, t):
    return F / m

x = np.zeros_like(t)
v = np.zeros_like(t)

x[0] = x0
v[0] = v0

for i in range(1, len(t)):
    x[i] = x[i-1] + v[i-1] * dt
    v[i] = v[i-1] + f(x[i-1], v[i-1], t[i-1]) * dt

plt.subplot(2, 1, 1)
plt.plot(t, x)
plt.xlabel('vrime (s)')
plt.ylabel('pomak (m)')
plt.grid()

plt.subplot(2, 1, 2)
plt.plot(t, v)
plt.xlabel('vrijeme (s)')
plt.ylabel('brzina (m/s)')
plt.grid()

plt.show()
