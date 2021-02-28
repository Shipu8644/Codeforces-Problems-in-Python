n=int(input())
c=0
s=0
for i in range(0,n):
    n1,n2=input().split()
    n1=int(n1)
    n2=int(n2)

    s=s-n1
    s=s+n2
    c=max(c,s)

print(c)