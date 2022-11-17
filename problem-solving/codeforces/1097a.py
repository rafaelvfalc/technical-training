#!/usr/bin/python3

card_table = input()
cards = input().split()

answer = "NO"
for card in cards:
    sets, suits = card[0], card[1]
    if(sets in card_table or suits in card_table):
        answer = "YES"
        break

print(answer)