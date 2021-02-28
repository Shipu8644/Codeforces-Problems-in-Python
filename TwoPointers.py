t = int(input())
a = list(map(int, input().split()[:t]))
a = sorted(a)
i = 0
j = len(a) - 1
x = 30

while i < j:
    if a[i] + a[j] == x:
        print(a[i], a[j])
        break

    elif a[i] + a[j] < x:
        i = i + 1

    else :
        j = j - 1

if a[i] + a[j] != x:
    print("doesnot found")
