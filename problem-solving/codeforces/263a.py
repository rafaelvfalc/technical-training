#!/usr/bin/python3

matrix = []

row_1 = 0
col_1 = 0
for i in range(1,6):
    row = input()
    if('1' in row):
        row_1 = i
        col_1 = row.find("1")/2 + 1
    matrix.append(row)

swaps = 0
if(row_1 >= 3):
    swaps = swaps + row_1 - 3
else: 
    swaps = swaps + 3 - row_1

if(col_1 >= 3):
    swaps = swaps + col_1 - 3
else:
    swaps = swaps + 3 - col_1

print(int(swaps))
