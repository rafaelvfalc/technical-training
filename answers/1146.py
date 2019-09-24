#!/usr/bin/python3

s = input() 

if(s.count("a") > (len(s)-s.count("a"))):
    print(len(s))
else:
    print(s.count("a")*2 - 1)