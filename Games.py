a=[input().split()for i in range(int(input()))]
count = 0
for i in a:
    for j in a:
        if i[0]==j[1]:
            count += 1
print(count)