input()
r = 0
for i in list(map(int, input().split()))[::-1]:
    r = min(0, r + i)

print(-r)
