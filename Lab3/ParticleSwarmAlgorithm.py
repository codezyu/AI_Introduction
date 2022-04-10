import numpy as np
import matplotlib.pyplot as plt
#位置数据
data=np.array([])
#维度
n=0
#粒子群规模
ParticleNum=200
#惯性权重
W=0.2
#学习因子
S=0.7
#迭代次数
Circle=100
#群体最好
P=np.arange(n)
#群体适应度
F=0
def init():
    global data,n,P
    data=np.array([[16.4700  , 96.1000],
     [16.4700  , 94.4400],
     [20.0900  , 92.5400],
     [22.3900   ,93.3700],
     [25.2300   ,97.2400],
     [22.0000   ,96.0500],
     [20.4700   ,97.0200],
     [17.2000  , 96.2900],
     [16.3000  , 97.3800],
     [14.0500  , 98.1200],
     [16.5300  , 97.3800],
     [21.5200   ,95.5900],
     [19.4100  , 97.1300],
     [20.0900 ,  92.5500]])
    n=14
    P=np.arange(n)
def GetDistance(position):
    global data
    x=np.size(position)
    distance=0
    for i in range(0,x):
        distance+=pow(pow(data[position[i]][1]-data[position[(i+1)%x]][1],2)+pow(data[position[i]][0]-data[position[(i+1)%x]][0],2),0.5)
    return distance
def GetAdaptity(position):
    return 1./GetDistance(position)
def ShowParticle(Population):
    plt.clf()
    (x,)=np.shape(Population)
    (num,)=np.shape(Population[0].position)
    xais=[np.sum(Population[i].position[0:num//2]) for i in range(0,x) ]
    yais =[np.sum(Population[i].position[num//2+1:num-1]) for i in range(0, x)]
    xbest=np.sum(P[0:num//2])
    ybest=np.sum(P[num//2+1:num-1])
    plt.scatter(xais, yais)
    plt.scatter(xbest,ybest,c='y')
    plt.pause(0.2)
class Particle:
    def __init__(self,n):
        arr=np.arange(n)
        self.position=np.random.permutation(arr)
        self.v=np.random.randint(0,2,n)
        self.bestPosition=self.position
        self.Bestf=GetAdaptity(self.position)
        self.c1=np.random.uniform(0,1)
    def adapt(self):
        global F,P
        self.adaptV()
        self.adaptPosition()
        t=GetAdaptity(self.position)
        if(t>self.Bestf):
            self.Bestf=t
            self.bestPosition=self.position
        #更新群体适应度
        if(t>F):
            F=t
            P=self.position
    def adaptPosition(self):
        (x,)=np.shape(self.position)
        hash=np.zeros(x)
        newPosition=(self.position+self.v)%x;
        for i in range(0,x):
            while hash[newPosition[i]]>0:
                newPosition[i]=(newPosition[i]+1)%x
            hash[newPosition[i]]=1
        self.position=newPosition
    def adaptV(self):
        global W,S,P
        newv=(W*self.v+self.c1*np.random.uniform()*(self.bestPosition-self.position)+S*np.random.uniform()*(P-self.position));
        v=np.rint(newv)
if __name__=="__main__":
     init()
     Population=[Particle(n) for i in range(0,ParticleNum)]
     for i in range(0,Circle):
         for j in range(0,ParticleNum):
             Population[j].adapt()
         ShowParticle(Population)
         print(GetDistance(P))
     plt.show()