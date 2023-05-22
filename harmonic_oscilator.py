import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, mass, spring_constant, initial_position, initial_velocity):
        self.mass = mass
        self.spring_constant = spring_constant
        self.position = initial_position
        self.velocity = initial_velocity
    
    def get_acceleration(self):
        return -self.spring_constant / self.mass * self.position
    
    def euler_integration(self, dt, num_steps):
        positions = [self.position]
        velocities = [self.velocity]
        accelerations = [self.get_acceleration()]
        
        for _ in range(num_steps):
            acceleration = self.get_acceleration()
            velocity = self.velocity + acceleration * dt
            position = self.position + velocity * dt
            
            velocities.append(velocity)
            positions.append(position)
            accelerations.append(acceleration)
            
            self.velocity = velocity
            self.position = position
        
        return positions, velocities, accelerations
    
    def compute_period(self, dt, threshold=0.1):
        positions, _, _ = self.euler_integration(dt, num_steps=10000)
        
        crossings = np.where(np.diff(np.sign(positions)))[0]
        
        periods = np.diff(crossings) * dt
        
        avg_period = np.mean(periods)
        valid_periods = periods[np.abs(periods - avg_period) < threshold * avg_period]
        
        period = np.mean(valid_periods)
        
        return period

mass = 1.0
spring_constant = 1.0
initial_position = 0.5
initial_velocity = 0.0
delta_t_values = [0.1, 0.01, 0.001, 0.0001]

oscillator = HarmonicOscillator(mass, spring_constant, initial_position, initial_velocity)

for delta_t in delta_t_values:
    period = oscillator.compute_period(delta_t)
    print(f"za delta t= {delta_t}, period je {period} sekundi")