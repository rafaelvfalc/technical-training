def print_something(code):
    for instruction in ['H', 'Q', '9']:
        if(instruction in code):
            return "YES"

    return "NO"

if __name__ == '__main__':
    code = input()
    print(print_something(code))
