#!/usr/bin/python3

n = int(input())

counter = 0
for number in range(1, int((n/2))+1):
    if(n % number == 0 and n != number):
        counter = counter + 1

print(counter)