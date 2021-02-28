n, t = map(int, input().split())
c = 0
sum = 0
a = list(map(int, input().split()))
for i in range(t - 1):
    while sum < t:
        sum = sum + a[i]
    if sum == t:
        c = c + 1
        break

if c == 1:
    print("YES")
else:
    print("NO")
