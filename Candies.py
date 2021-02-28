t = int(input())
while (t):
    t = t - 1
    n = int(input())
    a = 3
    while (n % a != 0):
        a = (a << 1) + 1
    print(int(n / a))
