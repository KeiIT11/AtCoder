S=input()
T=input()

for i in range(len(S)):
    if S[i]!=T[i]:
        print(i+1)
        break
    if i==(len(S)-1):
        print(i+2)