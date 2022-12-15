import itertools
import math

N = int(input())
x=[0 for x in range(N)]
y=[0 for x in range(N)]
l = []
ave_l=0
for i in range(N):
    x[i], y[i] = map(int, input().split())
arr = [0, 1, 2]
a = [x for x in range(N)]
p = list(itertools.permutations(a))

for i in range(len(p)): #順列の回数
    all = 0
    for j in range(1,len(p[0])): #経路を求めるのに必要な回数
        all+=math.sqrt((x[p[i][j-1]]-x[p[i][j]])**2+(y[p[i][j-1]]-y[p[i][j]])**2)
    l.append(all)
print(sum(l)/len(l))