from queue import PriorityQueue

#代价函数采用当前状态和目标状态的曼哈顿距离进行估量
def JudgeTheDistance(Now,End):
    sum=0
    for i in range(0,9):
        if Now[i]=='0':
            continue
        for j in range(0,9):
            if End[j]==Now[i]:
                value=abs(j%3-i%3)+abs(int(j/3)-int(i/3))
                sum+=value
    return sum
#显示
def show(Now):
    for i in range(0,9):
        if i%3==2:
            print(Now[i])
        else:
            print(Now[i],end = ' ')
#生成子代
def GenerateSon(Begin):
    index=0
    for i in range(0,9):
        if Begin[i]=='0':
            index=i
            break
    son=[]
    if i+3<9:
        son.append(swap(Begin,i,i+3))
    if i-3>=0:
        son.append(swap(Begin,i,i-3))
    if i-1>=0:
        son.append(swap(Begin,i,i-1))
    if i+1<9:
        son.append(swap(Begin,i,i+1))
    return son

def swap(Begin,i1,i2):
    son = list(Begin)
    son[i1], son[i2] = son[i2], son[i1]
    son = ''.join(son)
    return son
#A*搜索算法
def Astar(Begin,End):
    open =[]
    d=JudgeTheDistance(Begin,End)
    open.append((Begin,d,0))
    closed=[]
    maxcount=1
    while open:
        open.sort(key=lambda item:(-item[2],item[1]))
        maxcount=open[0][2]
        print("step: ", maxcount)
        show(open[0][0])
        if(open[0][0]==End):
            return maxcount
        else:
            son=GenerateSon(open[0][0])
            for i in son:
                status=False
                for j in open:
                    if i==j[0]:
                        status=True
                        break
                if i in closed:
                    status=True
                if status:
                    continue
                else:
                    soncoup=(i,JudgeTheDistance(i,End),open[0][2]+1)
                    open.append(soncoup)
            closed.append(open[0])
            del open[0]


if  __name__ == "__main__":
#    Begin=input("输入begin:")
 #   End=input("输入end:")
    Begin='283164705'
    End='123804765'
    print(Astar(Begin,End))


