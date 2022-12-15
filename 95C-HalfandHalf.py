A,B,C,X,Y = map(int, input().split())
a=0
b=0
cost=[]
if(X<Y):
    A,B=B,A
    X,Y=Y,X

for i in range(X+1):
    if(Y-i>=0):

        cost.append(A*(X-i)+B*(Y-i)+2*C*i)

    else:

        cost.append(A*(X-i)+B*(0)+2*C*i)
print(min(cost))