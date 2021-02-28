t=int(input())

while(t):
    t=t-1
    n,k=map(int,input().split())

    if(n==1 or k==1 or (n==2 and k==2)):
        print("YES")
    else:
        print("NO")