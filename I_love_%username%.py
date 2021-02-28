t = int(input())
a = list(map(int, input().split()[:t]))
c = 0;
c1 = 0;
temp = a[0];
temp1 = a[0]

for i in range(t - 1):
    if temp > a[i + 1]:
        c = c + 1
        temp = a[i + 1]
    elif temp1 < a[i + 1]:
        c = c + 1
        temp1 = a[i + 1]

print(c)

