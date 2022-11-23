def placed_dominos(m, n):
    return (m*n)//2

if __name__ == '__main__':
    m, n = map(int, input().split())

    print(placed_dominos(m, n))
