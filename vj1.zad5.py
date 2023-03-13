import matplotlib.pyplot as plt
import numpy as np

x1=float(input("unesi tocku x1 "))
y1=float(input("unesi tocku y1 "))
x2=float(input("unesi tocku x2 "))
y2=float(input("unesi tocku y2 "))

k=(y2-y1)/(x2-x1)
l=y1-k*x1
 
x=np.linspace(0,50,200)

y=k*x+l
plt.plot(x,y)
plt.plot([x1,x2],[y1,y2],"o")
osnes=input("unesi osnes")
if osnes=="s":
    osfile=input("filenemameda")
    plt.savefig(osfile+".pdf")
if osnes=="p":
    plt.show()

