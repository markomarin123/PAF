import numpy as np
import matplotlib.pyplot as plt

class Calculus:
    def rectangular_approximation(self, func, lower_bound, upper_bound, num_partitions):
        step = (upper_bound - lower_bound) / num_partitions
        x = np.linspace(lower_bound, upper_bound, num=num_partitions)
        integral_lower = np.sum(func(x) * step)
        integral_upper = np.sum(func(x + step) * step)
        return integral_lower, integral_upper

    def trapezoidal_formula(self, func, lower_bound, upper_bound, num_partitions):
        step = (upper_bound - lower_bound) / num_partitions
        x = np.linspace(lower_bound, upper_bound, num=num_partitions+1)
        integral = np.sum((func(x[:-1]) + func(x[1:])) * step / 2)
        return integral

def example_function(x):
    return np.sin(x)

lower_bound = 0
upper_bound = np.pi
num_partitions = 10

calculus = Calculus()

analytical_integral = 2

integral_lower_rect, integral_upper_rect = calculus.rectangular_approximation(example_function, lower_bound, upper_bound, num_partitions)

integral_trapezoidal = calculus.trapezoidal_formula(example_function, lower_bound, upper_bound, num_partitions)

num_partitions_range = np.arange(1, 21)
errors_rect = []
errors_trap = []

for num in num_partitions_range:
    integral_lower, integral_upper = calculus.rectangular_approximation(example_function, lower_bound, upper_bound, num)
    error_rect = np.abs(analytical_integral - integral_upper)
    errors_rect.append(error_rect)

    integral_trap = calculus.trapezoidal_formula(example_function, lower_bound, upper_bound, num)
    error_trap = np.abs(analytical_integral - integral_trap)
    errors_trap.append(error_trap)

plt.figure(figsize=(10, 6))
plt.title("greskice")
plt.xlabel("N")
plt.ylabel("Pogreska")
plt.plot(num_partitions_range, errors_rect, label="pravokutna aproksimacija")
plt.plot(num_partitions_range, errors_trap, label="trapezna formula")
plt.legend()
plt.grid(True)
plt.show()