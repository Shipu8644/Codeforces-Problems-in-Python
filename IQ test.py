n=int(input())
n1=list(map(int,input().split()[:n]))
c=0
c1=0
for i in range(n):
    if n1[i]%2!=0:
        c=c+1
        l=i+1

    else:
      c1=c1+1
      l1=i+1

if(c<c1):
    print(l)

else:
    print(l1)