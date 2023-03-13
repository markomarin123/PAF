import numpy as np
import matplotlib.pyplot as plt

g = 9.81

def jednoliko_gibanje(v0, t, x0=0):
    x = x0 + v0 * t
    
    plt.plot(t, x)
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.title('Uniform Motion')
    plt.grid()
    plt.show()

def kosi_hitac(v0, theta, m, t):

    theta = np.deg2rad(theta)
    

    vx0 = v0 * np.cos(theta)
    vy0 = v0 * np.sin(theta)
    

    x = np.zeros_like(t)
    y = np.zeros_like(t)
    vx = np.zeros_like(t)
    vy = np.zeros_like(t)
    

    x[0] = 0
    y[0] = 0
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
    plt.title('Projectile Motion')
    plt.grid()
    
    plt.subplot(1, 2, 2)
    plt.plot(t, x, label='X')
    plt.plot(t, y, label='Y')
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.legend()
    plt.grid()
    
    plt.show()
