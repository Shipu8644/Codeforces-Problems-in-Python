n1=list(map(int,input().split()[:4]))
c=0
n1.sort()

for i in range(0,3):
    if n1[i]==n1[i+1]:
        c=c+1

print(c)

