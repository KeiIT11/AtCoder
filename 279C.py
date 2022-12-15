import itertools
import copy

H,W=map(int,input().split())
S=[]
T=[]
a= [i for i in range(W)]
arr = list(itertools.permutations(a))
#print(arr)
flag=False
for i in range(H):
    S.append(list(input()))
for i in range(H):
    T.append(list(input()))

for i in range(len(arr)):
    S2=[]
    for j in range(H):
        W2=[]
        for k in range(W):
            W2.append(S[j][arr[i][k]])
        S2.append(W2)
    if S2==T:
        flag=True
        break
if flag==True:
    print("Yes")
else:
    print("No")