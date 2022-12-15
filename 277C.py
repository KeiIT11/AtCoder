N=int(input())
l=[]
start=[]
end=[]
top=0
current=10**9
for i in range(N):
    l.append(list(map(int, input().split())))
    start.append(l[i][0])
    end.append(l[i][1])

while True:
    top=max(end)
    current=start(top.index(top))
    if current==1: #end =[]
        break
print(top)
