N=int(input())
S = list(map(int, input().split()))
l=[]
count=0
for i in range(len(S)):
    if i==0:
        l.append(S[0])
        count+=S[0]
    else:
        l.append(S[i]-count)
        count+=l[i]
print(*l)