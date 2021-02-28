n,k=map(int,input().split())
n1=list(map(int,input().split()[:n]))
c=0
for i in range(n):
    if n1[i]+k<=5:
        c=c+1

print(c//3)
