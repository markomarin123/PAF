import numpy as np
import matplotlib.pyplot as plt

g = 9.81

def gibanje(x0, y0, v0, theta):

    theta = np.deg2rad(theta)

    vx0 = v0 * np.cos(theta)
    vy0 = v0 * np.sin(theta)

    t = np.linspace(0, 10, 1000)
    
    x = np.zeros_like(t)
    y = np.zeros_like(t)
    vx = np.zeros_like(t)
    vy = np.zeros_like(t)

    x[0] = x0
    y[0] = y0
    vx[0] = vx0
    vy[0] = vy0
    

    for i in range(1, len(t)):
        dt = t[i] - t[i-1]
        x[i] = x[i-1] + vx[i-1] * dt
        y[i] = y[i-1] + vy[i-1] * dt
        vx[i] = vx[i-1]
        vy[i] = vy[i-1] - g * dt
    
    plt.figure(figsize=(10, 4))
    
    plt.subplot(1, 2, 1)
    plt.plot(x, y)
    plt.xlabel('X (m)')
    plt.ylabel('Y (m)')
    plt.grid()
    
    plt.subplot(1, 2, 2)
    plt.plot(t, x, label='X')
    plt.plot(t, y, label='Y')
    plt.xlabel('vrijeme (s)')
    plt.ylabel('pozicija (m)')
    plt.legend()
    plt.grid()
    
    plt.show()

v0 = float(input("pocetna brzina u m/s: "))
theta = float(input("kut izbacaja: "))

x0 = 0
y0 = 0

gibanje(x0, y0, v0, theta)
