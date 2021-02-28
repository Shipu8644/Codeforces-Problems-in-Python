def printDivisors(n):
    i = 1
    c=0
    while i <= n:
        if (n % i == 0):
            c=c+1
            print(i,end=" ")
        i = i + 1
    print(c)


n1=2
printDivisors(n1)