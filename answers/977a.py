n,k = input().split()

count = 0
while count < int(k):
    if(int(n)%10 == 0):
        n = int(n)/10
    else:
        n = int(n)-1
    count = count+1

print(int(n))