t=int(input())
for i in range(t):
    n,a,b=map(int,input().split())
    print(('abcdefghijklmnopqrstuvwxyz'[:b]* n) [:n])

