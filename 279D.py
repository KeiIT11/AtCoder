import math

A,B = map(int,input().split())
g=1
t=A/(math.sqrt(g))
x=1
while True:
    if(-1/(x**2)+B<0):
        x+=1
    else:
        if x==1:
            print(t)
        else:
            x-=1
            #print(float(A/(g+x)+B*x))
            print('{:16.5f}'.format(A/(g+x)+B*x))
        break