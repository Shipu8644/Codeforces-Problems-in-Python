n=int(input(""))
f="I hate that"
g="I love that"
h="I hate it"
j="I love it"
for i in range(1,n):
      if i%2!=0:
          print(f,end=" ")
      else:
          print(g,end=" ")

if n%2!=0:
    print(h,end=" ")
else:
    print(j,end=" ")

