#!/usr/bin/python3

n = int(input())
cities = input()

SF = 0
FS = 0
current_city = cities[0]
for city in cities[1:]:
    if(current_city != city):
        if(current_city == "S"):
            SF = SF + 1
        else:
            FS = FS + 1
    current_city = city

if(SF > FS):
    print("YES")
else:
    print("NO")