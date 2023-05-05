import numpy as np
import matplotlib.pyplot as plt

class HarmonicOscillator:
    def __init__(self, mass, spring_constant, initial_position, initial_velocity):
        self.mass = mass
        self.spring_constant = spring_constant
        self.initial_position = initial_position
        self.initial_velocity = initial_velocity

    def position(self, time):
        omega = np.sqrt(self.spring_constant / self.mass)
        return self.initial_position * np.cos(omega * time)

    def velocity(self, time):
        omega = np.sqrt(self.spring_constant / self.mass)
        return -self.initial_position * omega * np.sin(omega * time)

    def acceleration(self, time):
        omega = np.sqrt(self.spring_constant / self.mass)
        return -self.spring_constant / self.mass * self.initial_position * np.cos(omega * time)

    def simulate(self, total_time, time_step):
        num_steps = int(total_time / time_step) + 1
        times = np.linspace(0, total_time, num=num_steps)
        positions = self.position(times)
        velocities = self.velocity(times)
        accelerations = self.acceleration(times)
        return times, positions, velocities, accelerations


mass = 1.0
spring_constant = 1.0
initial_position = 2.0
initial_velocity = 0.0
total_time = 10.0
time_step = 0.01

oscillator = HarmonicOscillator(mass, spring_constant, initial_position, initial_velocity)
times, positions, velocities, accelerations = oscillator.simulate(total_time, time_step)

plt.figure(figsize=(10, 6))
plt.plot(times, positions)
plt.title("Polozaj x - t")
plt.xlabel("Vrijeme t")
plt.ylabel("Polozaj x")
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 6))
plt.plot(times, velocities)
plt.title("Brzina v - t")
plt.xlabel("Vrijeme t")
plt.ylabel("Brzina v")
plt.grid(True)
plt.show()


plt.figure(figsize=(10, 6))
plt.plot(times, accelerations)
plt.title("Ubrzanje a - t")
plt.xlabel("Vrijeme t")
plt.ylabel("Ubrzanje a")
plt.grid(True)
plt.show()

class HarmonicOscillator:
    def __init__(self, mass, spring_constant, initial_position, initial_velocity):
        self.mass = mass
        self.spring_constant = spring_constant
        self.initial_position = initial_position
        self.initial_velocity = initial_velocity

    def position(self, time):
        omega = np.sqrt(self.spring_constant / self.mass)
        return self.initial_position * np.cos(omega * time)

    def velocity(self, time):
        omega = np.sqrt(self.spring_constant / self.mass)
        return -self.initial_position * omega * np.sin(omega * time)

    def acceleration(self, time):
        omega = np.sqrt(self.spring_constant / self.mass)
        return -self.spring_constant / self.mass * self.initial_position * np.cos(omega * time)

    def simulate(self, total_time, time_step):
        num_steps = int(total_time / time_step) + 1
        times = np.linspace(0, total_time, num=num_steps)
        positions = self.position(times)
        velocities = self.velocity(times)
        accelerations = self.acceleration(times)
        return times, positions, velocities, accelerations

    def calculate_period(self, time_step):
        times, positions, _, _ = self.simulate(10.0, time_step)
        max_indices = np.where(positions[1:-1] > positions[:-2] + positions[2:])[0]
        periods = 2 * (times[max_indices + 1] - times[max_indices])
        return np.mean(periods)


mass = 1.0
spring_constant = 1.0
initial_position = 2.0
initial_velocity = 0.0

oscillator = HarmonicOscillator(mass, spring_constant, initial_position, initial_velocity)

time_steps = np.logspace(-3, -1, num=30)
periods = []

for time_step in time_steps:
    period = oscillator.calculate_period(time_step)
    periods.append(period)

plt.figure(figsize=(10, 6))
plt.loglog(time_steps, periods, marker='o')
plt.title("Preciznost")
plt.xlabel("dt")
plt.ylabel("Period")
plt.grid(True)
plt.show()