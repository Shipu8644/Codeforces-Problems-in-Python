j = 0
i = 1
c = c1 = 0
sum =0; sum1 = 0
a = []
b = []
j=2
while j % 2 == 0:
    c = c + 1
    sum = sum + j
    a.append(j)
    j = j + 2
    if c == 4:
        break


while i % 2 != 0:
    c1 = c1 + 1
    if c1>4:
        break
    if c1 < 4:
        sum1 = sum1 + i
        b.append(i)
        i = i + 2
    while c1 == 4:
        sum1 = sum1 + i
        if sum1 == sum:
            b.append(i)

            break
        else:
            sum1 = sum1 - i
            i = i + 2

if sum1==sum:
  for y in a:
    print(y, end=" ")
  for x in b:
    print(x, end=" ")

else:
 print("NO")