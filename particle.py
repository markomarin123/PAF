import numpy as np
import matplotlib.pyplot as plt

class Particle:
    def __init__(self, x0, y0, v0, angle):
        self.x0 = x0
        self.y0 = y0
        self.v0 = v0
        self.angle = np.radians(angle)
        self.reset()

    def reset(self):
        self.x = self.x0
        self.y = self.y0
        self.vx = self.v0 * np.cos(self.angle)
        self.vy = self.v0 * np.sin(self.angle)
        self.t = 0

    def __move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt - 0.5 * 9.81 * dt ** 2
        self.vx = self.vx
        self.vy += -9.81 * dt
        self.t += dt

    def range(self, dt):
        self.reset()
        while self.y >= 0:
            self.__move(dt)
        return self.x

    def plot_trajectory(self, dt):
        self.reset()
        x_list = []
        y_list = []
        while self.y >= 0:
            x_list.append(self.x)
            y_list.append(self.y)
            self.__move(dt)
        plt.plot(x_list, y_list)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.show()

v0 = 10  
angle = 45 
x0 = 0  
y0 = 0 
dt = 0.01  

projektil = Particle(x0, y0, v0, angle)
domet = projektil.range(dt)

print("Domet projektila je:", domet, "m")

domet_numericki = projektil.range(dt)
print("Numericki domet projektila je:", domet_numericki, "m")
