#!/usr/bin/python3

inp = [int(x) for x in input().split()]

inp.sort()

ab, ac, bc, abc = inp

a = int(abc) - int(bc)
b = int(abc) - int(ac)
c = int(abc) - int(ab)

print(a, b, c)