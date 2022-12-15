import sys
h,m=input().split()
#13:40の場合34が入れ替わる。
#01:22
def swap(H,M):
    if len(H)==1:
        #01:23
        if len(M)==2:
            H,M=M[0],H[0]+M[1]

        else:
            M=H+M
            H="00"
        #01:02→00:12
    #11:12
    else:
        #11:22
        if len(M)==2:
            H,M=H[0]+M[0],H[1]+M[1]
        #11:02→10:12
        else:
            M=H[1]+M
            H=H[0]+"0"
    #print("swap",H,M)
    if 0<=int(H) and int(H)<=23 and 0<=int(M) and int(M)<=59:
        return True
    else:
        return False

flag=False
#for i in range(int(h),24):
i=int(h)
while True:
    if flag: #もし初回じゃないなら
        for j in range(0,60):
            #print(i,j)
            if swap(str(i),str(j)):
                print(i,j)
                sys.exit()
    else: #２回め以降なら
        for j in range(int(m),60):
            if j==59:
                flag=True
            #print(i,j)
            if swap(str(i),str(j)):
                print(i,j)
                sys.exit()
    if i==23:
        i=0
    else:
        i+=1