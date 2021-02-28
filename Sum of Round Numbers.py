t = int(input())
n1 = 0;
c = 0;
n2 = 0;
n2=[]
for i in range(t):
    n = int(input())
    s=n
    if n <= 10:
        print(n)
    else:
        while n>=10:
          n1=n%10
          if n%10!=0:
              n2.append(n1)
              c=c+1
          n=n//10
          print(n,n1)

