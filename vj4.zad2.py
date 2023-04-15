import numpy as np
import matplotlib.pyplot as plt
from particle import Particle

def analiticko_rjesenje(v0, theta):
    g = 9.81
    t = 2 * v0 * np.sin(np.radians(theta)) / g
    domet = v0 ** 2 * np.sin(np.radians(2 * theta)) / g
    return domet

def numericko_rjesenje(v0, theta, dt):
    projektil = Particle(0, 0, v0, theta)
    domet = projektil.range(dt)
    return domet

v0 = 10  
theta = 60 

domet_analiticki = analiticko_rjesenje(v0, theta)

dt_list = np.linspace(0.01,0.1,1000)

domet_numericko_list = []
rel_pogreska_list = []

for dt in dt_list:
    domet_numericko = numericko_rjesenje(v0, theta, dt)
    domet_numericko_list.append(domet_numericko)
    rel_pogreska = abs(domet_numericko - domet_analiticki) / domet_analiticki
    rel_pogreska_list.append(rel_pogreska)

plt.plot(dt_list, rel_pogreska_list)
plt.xscale('log')
plt.xlabel('dt (s)')
plt.ylabel('Relativna pogreska')
plt.title('Ovisnost relativne pogreske o vremenskom koraku')
plt.show()

def analiticko_rjesenje(v0, theta):
    g = 9.81
    t = 2 * v0 * np.sin(np.radians(theta)) / g
    domet = v0 ** 2 * np.sin(np.radians(2 * theta)) / g
    return domet

def numericko_rjesenje(v0, theta, dt):
    projektil = Particle(0, 0, v0, theta)
    domet = projektil.range(dt)
    return domet

v0 = 10  
theta = 60 

domet_analiticki = analiticko_rjesenje(v0, theta)

dt_list = [0.1, 0.05, 0.01, 0.005, 0.001]

domet_numericko_list = []
rel_pogreska_list = []

for dt in dt_list:
    domet_numericko = numericko_rjesenje(v0, theta, dt)
    domet_numericko_list.append(domet_numericko)
    rel_pogreska = abs(domet_numericko - domet_analiticki) / domet_analiticki
    rel_pogreska_list.append(rel_pogreska)

plt.plot(dt_list, rel_pogreska_list)
plt.xscale('log')
plt.xlabel(' dt (s)')
plt.ylabel('Relativna pogreska')
plt.title('Ovisnost relativne pogreske o vremenskom koraku')
plt.show()
