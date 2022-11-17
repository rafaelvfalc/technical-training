#!/usr/bin/python3

a,b = input().split()

count = 0
while True:
    if(int(a) > int(b)):
        break
    a = int(a)*3
    b = int(b)*2
    count = count+1

print(count)