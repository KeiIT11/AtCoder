#Nはスイッチの数、Mは電球の数
N, M = map(int, input().split())
#aは、電球が点灯しているかどうか。0 and 1
a=[0]*M
#nは、スイッチがoff(false)かON(true)か。
n=[False]*N

#k,xを一旦格納する
li=[[0] * 100 for i in range(M)]

"""
#kは繋がってるスイッチの数字
k=[0]*M
#スイッチの数字
s=[[0] * 100 for i in range(M)]
"""


#付いている電球の数
count1=0
#条件を満たした電球の数
count2=0
#条件を満たした組み合わせの数
count3=0

for i in range(M):
    li[i]=(list(map(int, input().split())))
#電球iが、式＝＝pのとき、点灯する
p = list(map(int, input().split()))

for i in range(2 ** N):
    n=[False]*N
    count1=0
    for j in range(N):#このループが一番のポイント
        if ((i >> j) & 1):#順に右にシフトさせ最下位bitのチェックを行う
            n[j]=True
            print(n)
        for l in range(M): #電球の数だけ回す
            for m in range(1,li[l][0]+1): #１個の電球がついているか確認
                if(n[li[l][m]-1]==True):
                    count1+=1
            if(count1%2==p[l]):
                count2+=1
            count1=0
    if(count2==M):
        count3+=1
print(count3)
