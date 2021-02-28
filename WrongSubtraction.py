n,k= input().split()
n=int(n)
k=int(k)

for i in range(0,k):
    if n%10>0:
        n=n-1
    else:
        n=n/10

n=int(n)
print(n)