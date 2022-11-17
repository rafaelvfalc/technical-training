#!/usr/bin/python3

n = input()
inp = input().split()

out = "EASY"
for i in range(len(inp)):
    if(int(inp[i]) == 1):
        out = "HARD"
        break

print(out)