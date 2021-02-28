t=int(input())
c=0;c1=0
while(t):

    t=t-1
    a,b=map(int,input().split())
    if a>b:
        c=c+1
    elif b>a:
        c1=c1+1

if c>c1:
     print("Mishka")
elif c1>c:
     print("Chris")

elif c==c1:
    print("Friendship is magic!^^")