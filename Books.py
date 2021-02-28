n, t = map(int, input().split())
sum = 0
a = list(map(int, input().split()[:n]))


for i in range(n):
    sum = sum + a[i]
    if  sum > t:
        a = i
        print(a)
        break
    elif sum==t:
        print(i)

    elif sum < t and i==n-1:
        print(i+2)


