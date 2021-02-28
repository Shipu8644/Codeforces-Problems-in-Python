t = int(input())
for i in range(t):
    n = int(input())
    j = 0
    i = 1
    c = c1 = 0
    sum = 0;
    sum1 = 0
    a = []
    b = []
    d = []
    j = 2
    if n % 2 == 0:
        while j % 2 == 0:
            c = c + 1
            sum = sum + j
            a.append(j)
            j = j + 2
            if c == n // 2:
                break

        while i % 2 != 0:
            c1 = c1 + 1
            if c1 > n // 2:
                break
            if c1 < n // 2:
                sum1 = sum1 + i
                b.append(i)
                i = i + 2
            while c1 == n // 2:
                sum1 = sum1 + i
                if sum1>sum:
                    break
                if sum1 == sum:
                    b.append(i)

                    break
                else:
                    sum1 = sum1 - i
                    i = i + 2
    if sum == sum1:
        d = a + b
        print("YES")
        print(*d,sep=" ")

    else:
        print("NO")
