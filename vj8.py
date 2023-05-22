import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def draw_particle_path(q, m, v0, E, B, dt, num_steps):
    t = 0
    v = np.array(v0)
    r = np.array([0, 0, 0])
    path = [r]

    for _ in range(num_steps):
        F_e = q * np.array(E)

        F_m = q * np.cross(v, np.array(B))

        F = F_e + F_m

        a = F / m

        v = v + a * dt
        r = r + v * dt

        path.append(r.copy())

        t += dt

    return np.array(path)

q = 1  
m = 1 

v0 = [10, 20, 10] 

E = [0, 0, 0]

B = [0, 0, 1] 

dt = 0.001
num_steps = 10000

path = draw_particle_path(q, m, v0, E, B, dt, num_steps)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot(path[:, 0], path[:, 1], path[:, 2])
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()