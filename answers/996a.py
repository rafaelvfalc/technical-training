#!/usr/bin/python3

n = int(input())

count = 0
while(n != 0):
    if(n >= 100):
        bills = int(n / 100)
        n = n - (bills * 100)
        count = count + bills
    elif(n >= 20):
        bills = int(n / 20)
        n = n - (bills * 20)
        count = count + bills
    elif(n >= 10):
        bills = int(n / 10)
        n = n - (bills * 10)
        count = count + bills
    elif(n >= 5):
        bills = int(n / 5)
        n = n - (bills * 5)
        count = count + bills
    elif(n >= 1):
        bills = int(n / 1)
        n = n - (bills * 1)
        count = count + bills

print(count)