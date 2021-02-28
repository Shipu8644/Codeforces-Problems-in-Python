n, t = map(int, input().split())
ls = list(map(int, input().split()))
s = j = 0
for i in range(n):
    s += ls[i]
    if s > t:
        s -= ls[j]
        j += 1
print(n-j)