N,Q=map(int,input().split())
l=[] #input
m=[[0]*N for _ in range(N)] #user follow

for i in range(Q):
    l.append(list(map(int, input().split())))

for i in range(Q):
    if l[i][0]==1:
        m[l[i][1]-1][l[i][2]-1]=1 #l[i][1]-1:A, l[i][2]-1:B
    elif l[i][0]==2:
        m[l[i][1]-1][l[i][2]-1]=0
    else:
        if m[l[i][1]-1][l[i][2]-1]==1 and m[l[i][2]-1][l[i][1]-1]==1:
            print("Yes")
        else:
            print("No")
