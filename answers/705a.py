n = int(input())

feeling = "I hate"
for num in range(2,n+1):
    if num % 2 == 0:
        feeling = feeling + " that I love"
    else:
        feeling = feeling + " that I hate"

feeling = feeling + " it"
print(feeling)
