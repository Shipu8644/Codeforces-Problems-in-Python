c=0
n=int(input())
for i in range(n):
    s1=(input())
    if s1 == "Tetrahedron":
        c=c+4
    elif s1 == "Cube":
        c=c+6
    elif s1 == "Octahedron":
        c=c+8
    elif s1 == "Dodecahedron":
        c=c+12
    elif s1 == "Icosahedron":
        c=c+20

print(c)