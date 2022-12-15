import sys
N=int(input())
S=[input() for _ in range(N)]
s1=["H" , "D" , "C" , "S"]
s2=["A" , "2" , "3" , "4" , "5" , "6" , "7" , "8" , "9" , "T" , "J" , "Q" , "K" ]
for i in range(N):
    for k in range(len(s1)):
        if not S[i][0] in s1:
            print("No1")
            sys.exit()
    for k in range(len(s2)):
        if not S[i][1] in s2:
            print("No2")
            sys.exit()
    for j in range(N):
        if i==j:
            pass
        elif S[i]==S[j]:
            print("No3")
            sys.exit()
print("Yes")