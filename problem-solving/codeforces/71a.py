def abrevWord(word):
    if(len(word) > 10):
        return word[0] + str(len(word)-2) + word[-1]
    return word

if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        word = input()
        print(abrevWord(word))
