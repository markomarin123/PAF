import numpy as np
import matplotlib.pyplot as plt

class Projectile:
    def __init__(self, mass, initial_position, initial_velocity, drag_coefficient):
        self.mass = mass
        self.position = initial_position
        self.velocity = initial_velocity
        self.drag_coefficient = drag_coefficient
    
    def get_acceleration(self, velocity):
        acceleration_x = -self.drag_coefficient * velocity[0] / self.mass
        acceleration_y = -self.drag_coefficient * velocity[1] / self.mass - 9.81
        return np.array([acceleration_x, acceleration_y])
    
    def euler_integration(self, dt, num_steps):
        positions = [self.position]
        velocities = [self.velocity]
        
        for _ in range(num_steps):
            acceleration = self.get_acceleration(self.velocity)
            velocity = self.velocity + acceleration * dt
            position = self.position + velocity * dt
            
            velocities.append(velocity)
            positions.append(position)
            
            self.velocity = velocity
            self.position = position
        
        return positions, velocities
    
    def runge_kutta_integration(self, dt, num_steps):
        positions = [self.position]
        velocities = [self.velocity]
        
        for _ in range(num_steps):
            k1_v = self.get_acceleration(self.velocity)
            k1_x = self.velocity
            k2_v = self.get_acceleration(self.velocity + k1_v * dt / 2)
            k2_x = self.velocity + k1_v * dt / 2
            k3_v = self.get_acceleration(self.velocity + k2_v * dt / 2)
            k3_x = self.velocity + k2_v * dt / 2
            k4_v = self.get_acceleration(self.velocity + k3_v * dt)
            k4_x = self.velocity + k3_v * dt
            
            acceleration = (k1_v + 2 * k2_v + 2 * k3_v + k4_v) / 6
            velocity = self.velocity + acceleration * dt
            position = self.position + (k1_x + 2 * k2_x + 2 * k3_x + k4_x) * dt / 6
            
            velocities.append(velocity)
            positions.append(position)
            
            self.velocity = velocity
            self.position = position
        
        return positions, velocities


mass = 1.0
initial_position = np.array([0.0, 0.0])
initial_velocity = np.array([30.0, 30.0])
drag_coefficient = 0.1
delta_t = 0.01
num_steps = 500

projectile = Projectile(mass, initial_position, initial_velocity, drag_coefficient)

euler_positions, euler_velocities = projectile.euler_integration(delta_t, num_steps)
rk_positions, rk_velocities = projectile.runge_kutta_integration(delta_t, num_steps)

euler_x = [pos[0] for pos in euler_positions]
euler_y = [pos[1] for pos in euler_positions]

rk_x = [pos[0] for pos in rk_positions]
rk_y = [pos[1] for pos in rk_positions]

plt.plot(euler_x, euler_y, label='Eulerova metoda')
plt.plot(rk_x, rk_y)
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()