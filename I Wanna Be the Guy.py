n = int(input())
n1 = list(map(int, input().split()[:n]))
n2=int(input())
n3 = list(map(int, input().split()[:n2]))

s = 0
s1=0
c = 0
c1 = 0

for i in range(1, n):
    s = s + n1[i]
    if s % n1[0] == 0:
         c =1

for i in range(1, n2):
    s1 = s1 + n3[i]
    if s1 % n3[0] == 0:
        c1 = 1


if c==c1:
     print("I become the guy.")

else:
     print("Oh, my keyboard!")