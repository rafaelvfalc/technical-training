def process_statement(stat):
    if('+' in stat):
        return 1
    if('-' in stat):
        return -1

if __name__ == '__main__':
    n = int(input())

    value = 0
    for i in range(n):
        stat = input()
        value += process_statement(stat)
    
    print(value)
