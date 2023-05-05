import numpy as np

class Calculus:
    def calculate_derivative(self, func, x, epsilon=1e-6, method="three-step"):
        if method == "three-step":
            return (func(x + epsilon) - func(x - epsilon)) / (2 * epsilon)
        elif method == "two-step":
            return (func(x + epsilon) - func(x)) / epsilon
        else:
            raise ValueError

    def calculate_numerical_derivatives(self, func, lower_bound, upper_bound, epsilon=1e-6, method="three-step"):
        points = np.linspace(lower_bound, upper_bound, num=100)
        derivatives = []

        for x in points:
            derivative = self.calculate_derivative(func, x, epsilon, method)
            derivatives.append((x, derivative))

        return derivatives
    
import numpy as np
import matplotlib.pyplot as plt
from calculus import Calculus

def cubic_function(x):
    return x**3

def trigonometric_function(x):
    return np.sin(x)

lower_bound = -2
upper_bound = 2

derivatives_cubic = Calculus.calculate_numerical_derivatives(cubic_function, lower_bound, upper_bound)
derivatives_trig = Calculus.calculate_numerical_derivatives(trigonometric_function, lower_bound, upper_bound)

x = np.linspace(lower_bound, upper_bound, num=100)
cubic_derivative_analytical = 3 * x**2
trig_derivative_analytical = np.cos(x)

plt.figure(figsize=(10, 6))
plt.title("Derivacije kubne i trigonometrijske funkcije")
plt.xlabel("x")
plt.ylabel("f'(x)")

plt.plot(x, cubic_derivative_analytical, label="Kubna funkcija (analiticko rjesenje)")
plt.plot(x, trig_derivative_analytical, label="Trigonometrijska funkcija (analiticko rjesenje)")

x_cubic, y_cubic = zip(*derivatives_cubic)
x_trig, y_trig = zip(*derivatives_trig)
plt.scatter(x_cubic, y_cubic, color="red", label="Kubna funkcija")
plt.scatter(x_trig, y_trig, color="green", label="Trigonometrijska funkcija ")

plt.legend()
plt.grid(True)
plt.show()