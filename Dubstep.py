s = input()
c=1
i=0
for i in range(0,len(s)):
        if s[i] == 'W' and s[i + 1] == 'U' and s[i + 2] == 'B':
            i=i+3
            if (c!=1):
               print(" ",end="")

            continue
        else:
            c=0
            print(s[i],end="")



