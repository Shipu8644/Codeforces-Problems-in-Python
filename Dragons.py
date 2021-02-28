s,t = map(int,input().split())
c = 0
s1 = t
a= []
b= []
i=0

for i in range(t):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
for i in range(t):
  for j in range(t-i-1):
       if a[j]>a[j + 1]:
           a[j],a[j+1]= a[j+1],a[j]
           b[j], b[j + 1] = b[j + 1], b[j]

for l in range(t):
    if s>a[l]:
        c= c + 1
        s = s + b[l]


if(c == s1):
    print("YES")

else:
    print("NO")
