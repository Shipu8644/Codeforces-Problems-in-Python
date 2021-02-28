import math
t=int(input())

for i in range(t):
    a1,b1=map(int,input().split())
    a2,b2=map(int,input().split())
    if a1<b1:
        a1,b1=b1,a1
    if a2<b2:
        a2,b2=b2,a2

    if (a1==a2 and b1+b2==a2):
        print("YES")
    else:
        print("NO")
