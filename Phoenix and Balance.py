t= int(input())
sum = 0
for i in range(t):
    n = int(input())
    sum = 0
    sum1 = []
    if n == 2:
        print(2)
    else:
     for i in range(1,n+1):
        sum = 2**i
        sum1.append(sum)

     l = len(sum1)
     l2 = int(l/2)

     sum2 = 0
     for i in range(l2):
         sum2 = sum2 + sum1[i]
     print(sum2)
