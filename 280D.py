import math

K=int(input())

#素因数分解の関数
def factorization(n):
    arr = []
    temp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr.append([i, cnt])

    if temp!=1:
        arr.append([temp, 1])

    if arr==[]:
        arr.append([n, 1])

    return arr

#素因数分解したリストを得る。
l1=factorization(K)
l_max=0
l2=[] #
l3=[] #

#1+2+...に、乗数を変換→l2
for i in range(len(l1)):
    count=0
    for j in range(10**12):
        count=count+j
        #print(count)
        #print(count)
        if count>=l1[i][1]:
            l2.append([l1[i][0],count])
            l3.append([l1[i][0],j]) #1+2+...の最後の数を代入したver
            break
print(l1)
print(l2)
print(l3)
l2_max=0
index=0

#最大値を求める。
count=0
for i in range(len(l3)):
    if i == 0:
        l2_max=l3[i][0]**l3[i][1]
    if l2_max<l3[i][0]**l3[i][1]:
        l2_max=l3[i][0]**l3[i][1]
        index=i
#print("index",index)
count=0
k=0
#i~(n-1)

print(l3[index][0]**l3[index][1])