t = int(input())

for i in range(t):
    a = list(map(int, input().split()))
    if a[0]*(a[1] - a[2])<=a[3] + a[4] and a[0]*(a[1] + a[2])>=a[3] - a[4]:
        print("YES")
    else:
        print("NO")
