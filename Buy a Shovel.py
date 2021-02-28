k,r=map(int,input().split())
i=0
while True:
    i=i+1
    if k*i%10==0 or k*i%10==r:
        print(i)
        break
