import numpy as np
import matplotlib.pyplot as plt
from numpy import linalg as LA

class gravitacija:
    def __init__(self,Mz,v_obodna,x,Ms,V,x2):
        self.m=Mz
        self.v=v_obodna
        self.x=x
        self.M=Ms
        self.V=V
        self.x2=x2
        self.pocetni=self.m,self.v,self.x
        self.pocetni2=self.M,self.V,self.x2

    def __move(self,dt,G=6.67408*10**(-11)):

        self.a=-G*self.M/((LA.norm(np.array(self.x)-np.array(self.x2)))**3)*(np.array(self.x)-np.array(self.x2))
        self.v+=self.a*dt
        self.x+=self.v*dt
        self.a2=-G*self.m/((LA.norm(np.array(self.x2)-np.array(self.x)))**3)*(np.array(self.x2)-np.array(self.x))
        self.V+=self.a2*dt
        self.x2+=self.V*dt

    def reset(self):
        self.m,self.v,self.x=self.pocetni
        self.M,self.V,self.x2=self.pocetni2


    def plot_trajectory(self,dt,T,G=6.67408*10**(-11)):
        lista_x=[self.x[0]]
        lista_y=[self.x[1]]
        lista_xs=[]
        lista_ys=[]
        t=0

        while t<T:
            self.__move(dt,G=6.67408*10**(-11))
            lista_x.append(self.x[0])
            lista_y.append(self.x[1])
            lista_xs.append(self.x2[0])
            lista_ys.append(self.x2[1])
            t+=dt

        plt.scatter(0,0,c='yellow')
        plt.plot(lista_x,lista_y,'brown')
        plt.plot(lista_xs,lista_ys,'red')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.show()

zemlja=gravitacija(5.9742*10**24,(0,29783),(1.486*10**11,0),1.989*10**30,(0,0),(0,0))

zemlja.plot_trajectory(24*3600,365.242*24*3600)