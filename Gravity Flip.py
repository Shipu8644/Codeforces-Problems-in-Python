n=int(input())
n1=list(map(int,input().split()[:n]))
for i in range(0,n):
    n1.sort()
    print(n1[i],end=" ")
