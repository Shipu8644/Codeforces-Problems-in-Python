a, b = map(int, input().split())
i = 0
c = 0
c1 = min(a, b)
c2 = max(a,b)
# print(c1)
for i in range(min(a, b)):
    while a != 0 and b != 0:
        a = a - 1
        b = b - 1
        c = c + 1

d = (c2-c)/2
d = int(d)

print(c,d,end="")
