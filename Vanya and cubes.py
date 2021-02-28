n=int(input())
sum = 0
s1 = 0
c = 0
for i in range(1,n+1):
    sum = sum + i
    s1 = s1 + sum

    if (s1>n):
        break

    c+=1

print(c)