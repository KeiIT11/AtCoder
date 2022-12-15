a=int(input())
N=list(input())

n=len(N)
print(n)
count=0

for i in range(2,n):
        if(N[i]=="C"):
            if(N[i-1]=="B"):
                if(N[i-2]=="A"):
                    count+=1
print(count)