n=int(input())
c1=0
c2=0
n1=list(map(int,input().split()[:n]))
for i in range(n):
    if n1[i]==0:
        c1=c1+1

    elif n1[i]==1:
        c2=c2+1

if(c2==0):
    print("EASY")
else:
    print("HARD")

