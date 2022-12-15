import copy

S=list(input())
T=list(input())

flag=False
for i in range(2 ** len(S)):
    M=S.copy()
    for j in range(len(S)):
        if ((i >> j) & 1):
            if(M==[]):
                break
            elif(M==T):
                flag=True
            else:
                M.pop(0)
            #print("M",M)
            #print("S",S)
        else:
            if(M==[]):
                break
            elif(M==T):
                flag=True
            else:
                M.pop(-1)
            #print("M",M)
            #print("S",S)
        if flag==True:
            break
if flag==True:
    print("Yes")
else:
    print("No")