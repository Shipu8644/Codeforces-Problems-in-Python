t = int(input())
c=c1=0
n1 = list(map(int, input().split()[:t]))
for i in range(t):
   c=c+n1[i]
   if c<0:
       c=0
       c1=c1+1
print(c1)

