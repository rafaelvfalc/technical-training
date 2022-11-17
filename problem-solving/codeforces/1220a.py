#!/usr/bin/python3

n = int(input())

cards = input()

binary = ""
while(len(cards) != 0):
    if("o" in cards and "n" in cards and "e" in cards):
        cards = cards.replace('o', '', 1)
        cards = cards.replace('n', '', 1)
        cards = cards.replace('e', '', 1)
        binary = binary + "1 "
    else:
        cards = cards.replace('z', '', 1)
        cards = cards.replace('e', '', 1)
        cards = cards.replace('r', '', 1)
        cards = cards.replace('o', '', 1)
        binary = binary + "0 "

print(binary)

