num = input() #input
x = [int(a) for a in str(num)] #ABCD

op=['-','-','-']
n = len(op)

for i in range(2 ** n):
    op=['-','-','-']
    for j in range(n):
        if ((i >> j) & 1):
            op[j]='+'
    if(eval(str(x[0])+op[0]+str(x[1])+op[1]+str(x[2])+op[2]+str(x[3])) == 7):
        print(str(x[0])+op[0]+str(x[1])+op[1]+str(x[2])+op[2]+str(x[3])+"=7")
        break