t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    l=0
    l1=0
    i=0
    a=[]
    while True:
        l=l+1
        if l%n != 0:
            a.append(l)
            i=i+1
            if i==k:
                break

    l1=len(a)
    print(a[l1-1])
