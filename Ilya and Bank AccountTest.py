n1 = int(input())
a = 0;
b = 0
if n1 >= 0:
    print(n1)

else:
    a = (n1 // 10)
    b = n1 // 100 * 10 + n1 % 10
    print(a, b)
    # print(max(a, b))
