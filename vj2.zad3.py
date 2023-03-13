
import kinematika
import numpy as np

v0 = 10.0 
t = np.linspace(0, 10, 1000)
kinematika.jednoliko_gibanje(v0, t)


v0 = 20.0  
theta = 45.0  
m = 1.0  
t = np.linspace(0, 10, 1000)
kinematika.kosi_hitac(v0, theta, m, t)
