import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
matrix=[1,2]
Pc=0.4
Pv=0.2
Pt=0.5
Pk=0.1
bestcount=1.0
colors=list(mcolors.TABLEAU_COLORS.keys())
maxsize=100
size=0
def GetRandomGene(n):
    flag=np.zeros((1,n+1),int)
    gene=np.zeros((1,n+1),int)
    i=1
    while i<=n:
        t=random.randint(1,n)
        while flag[0][t]==1:
            t=t%n+1;
        if flag[0][t]==0:
            gene[0][i]=t
            flag[0][t]=1
            i+=1
    return gene
#获取适应度
def GetAdaptability(gene,matrix):
    global bestcount
    count=GetDistance(gene,matrix)
    return 1.0/count
def GetDistance(gene,matrix):
    (y,) = np.shape(gene)
    y -= 1
    i = 1
    count = 0
    while i <= y:
        count += matrix[gene[i]][gene[i % y + 1]]
        i += 1
    return count
def AddToStock(array,gene):
    array=np.append(array,np.array(gene),axis=0)
    return array
# todo
def SelectGene(array,n):
    global bestcount
    (x,y)=np.shape(array)
    count=0
    ada=np.array([0])
    i=0
    maxcount=GetAdaptability(array[0], matrix)
    while i<x:
        now=GetAdaptability(array[i], matrix)
        ada=np.append(ada,now)
        count+=now
        if(now>maxcount):
            maxcount=now
        i+=1
    newarray=np.zeros((0,y),int)
    t1=random.random()*0.5
    t2=random.random()*0.75
    l=np.mean(ada)
    global Pc
    global Pv
    global Pt
    global Pk
    if(np.median(ada)==np.max(ada)):
        Pc=1
        Pv=1
        Pt=1
        Pk=0
    else:
        Pc=0.4
        Pv=0.2
        Pt=0.5
        Pk=0.1
    i=0
    j=0
    while i<x:
        if j>=n:
            break
        t = random.random()
        if(l>ada[i] and t>Pt):
            i+=1
            continue
        else:
            newarray = AddToStock(newarray, convert(array[i]))
            s=random.random()
            if(s<Pk):
                newarray = AddToStock(newarray, convert(array[i]))
                j+=1
            j+=1
        i+=1
    bestcount=1.0/maxcount
    return newarray
#交叉
def GenerateSon(father,mother):
    #获取父代基因片段
    (x,y)=np.shape(father)
    y=y-1
    begin=random.randint(1,y)
    end=random.randint(1,y)
    if(begin>end):
        begin,end=end,begin
    slice=father[0][begin:end]
    t=1
    newgene=np.zeros((1,y+1),int)
    newgene[0][begin:end]=slice
    while t<=y:
        if t>=begin and t<end:
            t+=1
            continue
        for i in mother[0]:
            if i in slice or i in newgene[0]:
                continue
            else:
                newgene[0][t]=i
                t+=1
                break;
    return newgene
#变异
def Variation(gene):
    (x,y)=np.shape(gene)
    y-=1
    t1=random.randint(1,y)
    t2=random.randint(1,y)
    temp=gene[0][t1]
    gene[0][t1]=gene[0][t2]
    gene[0][t2]=temp
    return gene
def convert(a):
    return np.array(np.atleast_2d(a))
def Read():
    global matrix
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
     [20.0900 ,  92.5500]]);
    (x,y)=np.shape(data)
    matrix=np.zeros((x+1,x+1),float)
    i=1
    while i<=x:
        j=1
        while j<=x:
            matrix[i][j]=np.sqrt(np.square(data[i-1][1]-data[j-1][1])+np.square(data[i-1][0]-data[j-1][0]))
            j+=1
        i+=1
    (size,size1)=np.shape(matrix)
    t=0
    # 新建种群
    array = np.zeros((0, size), int)
    while t<200:
        x=GetRandomGene(size-1)
        array=AddToStock(array,x)
        t+=1
    #每代生成
    ma=200
    g=0
    while g<500:
        (mb,mb1)=np.shape(np.array(array))
        #杂交
        i=0
        t1=0
        while t1<200:
            i=random.randint(0,mb-1)
            j=random.randint(0,mb-1)
            t=random.random()
            if(t>Pc):
                continue
            else:
                if(np.array_equal(array[i],array[j])):
                    another = Variation(convert(array[i]))
                else:
                    another=array[i]
                son=GenerateSon(convert(another),convert(array[j]))
                array=AddToStock(array,son)
                t1+=1
        (x,y)=np.shape(array)
        i=0
        #突变
        t1=0
        while t1<200:
            t = random.random()
            if (t >Pv):
                continue
            else:
                i=random.randint(0,x-1)
                another=Variation(convert(array[i]))
                array=AddToStock(array,another)
                t1+=1
        g+=1
        #加入其它种族
        while t < 200:
            x = GetRandomGene(size - 1)
            array = AddToStock(array, x)
            t += 1
        # 自然选择
        array = SelectGene(array, ma)
        print("第" + str(g) + "代")
        print(array)
        print("距离为："+str(GetDistance(array[0], matrix)))
        for i in array[0]:
            print(i,end="->")

    i=0
    while i<100:
        print(str(GetDistance(array[i], matrix)),end=",")
        i+=1
if __name__=="__main__":
    Read()
