n=int(input())
k=0
for i in range(1,n):
    if i%4 == 0 or i%9==0:
        k = n-i
        if k%2==0:
            print(i,k,end="")
            break