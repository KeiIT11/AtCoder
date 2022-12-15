N, K, M = map(int, input().split())
A = list(map(int, input().split()))
a = 0

sum = 0
for i in range(N-1):
    sum += A[i]

if((sum + K)/N < M):
    print(-1)
elif((sum)/N >= M):
    print(0)
else:
    print(M*N-sum)


#(sum + a)/N >=M