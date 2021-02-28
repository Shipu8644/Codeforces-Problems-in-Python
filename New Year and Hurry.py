n,k=map(int,input().split())
mul = 0;c=0
for i in range(1,n+1):
   mul = mul + 5*i
   if 240 - mul >= k:
       c = c + 1

   else:
       break

print(c)