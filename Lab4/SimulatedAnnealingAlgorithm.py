import numpy as np
import matplotlib.pyplot as plt
import sys
import math
T=10
K=0.9
Circle=5
i=math.pi
x=[0,2*math.pi]
#存储最优结果
besti=i
def generate():
    global x,T,i
    for k in range(0,Circle):
        j = np.random.uniform(-0.5,0.5) *T + i
        j=j%(x[1]-x[0])+x[0]
        Metropolis(j)
    T=T*K
def Func(x):
    return 11*np.sin(6*x)+7*np.cos(5*x)
def Metropolis(j):
    global T,i,besti
    jy=Func(j)
    iy=Func(i)
    if(jy<=iy):
        i=j
    if(jy<=Func(besti)):
        besti=j
    else:
        print(math.exp(-((jy-iy)/T)))
        if(np.random.uniform()>math.exp(-((jy-iy)/T))):
            i=j
    plt.scatter(i,Func(i))
if __name__=="__main__":
    x1=np.arange(x[0],x[1],0.01)
    y1=Func(x1)
    plt.plot(x1,y1)
    while T>1:
        print(T)
        generate()
    print("结果为:")
    print("x="+str(besti))
    print("y="+str(Func(besti)))
    plt.show()