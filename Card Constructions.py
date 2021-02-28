t=int(input())

for i in range(t):
    c = 0
    sum = 0
    i=0
    n=int(input())

    while(n>1):
            sum=0
            i=0
            while(True):
              sum=2+3*i
              i=i+1
              if sum>n:
                break
              else:
                n=n-sum

            c=c+1

    print(c)