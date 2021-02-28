l,r,x,y,k= map(int,input().split())

for i in range(x, y+1):
    if r >= i*k >= l:
        print('YES')
        break
else:
    print('NO')