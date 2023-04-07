import numpy as np
N=int(input("broj tocaka: "))
xi=int(input("broj xi: "))
for i in range(1,N):
    xi+=xi+1
x_sr=xi/N
print(x_sr)

znj=0.0
for i in range(1,N):
    znj+=znj+(xi-x_sr)**2

ro=np.sqrt(znj)
donji=np.sqrt(N(N-1))
oho=ro/donji
print(oho)