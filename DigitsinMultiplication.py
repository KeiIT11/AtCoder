N=int(input())
a=[]
for i in range(1,N+1):
    if(N%i==0):
        a.append(max(len(str(abs(i))),len(str(abs(N//i)))))
print(min(a))
