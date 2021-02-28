n=int(input())
n1=list(map(int,input().split()[:n]))
print(n1)

sum=0
for i in n1:
    sum=sum+i

print(sum/n)