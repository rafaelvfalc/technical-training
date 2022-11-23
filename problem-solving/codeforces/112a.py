def lexicographical_order(word_1, word_2):
    word_1 = word_1.lower()
    word_2 = word_2.lower()

    if(word_1 == word_2):
        return 0
    
    for index in range(len(word_1)):
        if(ord(word_1[index]) == ord(word_2[index])):
            continue
        if(ord(word_1[index]) > ord(word_2[index])):
            return 1
        else:
            return -1

if __name__ == '__main__':
    word_1 = input()
    word_2 = input()

    print(lexicographical_order(word_1, word_2))
