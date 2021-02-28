t1= int(input())
c = 0
for i in range(t1):
    c=0
    x,y= map(int,input().split())

    if x%y == 0:
        print(0)

    else:
        print((y - x % y) % y)







