N = int(input())
A = list(map(int, input().split()))
flag = True
for i in range(N):
    if(A[i]%2==0):
        if(A[i]%3!=0):
            if(A[i]%5!=0): #３で割り切れて、５で割り切れなかったら
                flag = False
                break
if(flag):
    print("APPROVED")
else:
    print("DENIED")