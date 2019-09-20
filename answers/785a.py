n = int(input())

faces = 0
for i in range(n):
    poly = input()
    if(poly == "Tetrahedron"):
        faces = faces + 4
    elif(poly == "Cube"):
        faces = faces + 6
    elif(poly == "Octahedron"):
        faces = faces + 8
    elif(poly == "Dodecahedron"):
        faces = faces + 12
    elif(poly == "Icosahedron"):
        faces = faces + 20

print(faces)   