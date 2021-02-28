n, m, a, b = map(int, input().split())

if b // m >= a:
    print(n * a)

elif b // m < a:
    r = (n%m) * a
    if r>b:
        print (n // m * b + b)
    else:
        print (n // m * b + r)