def rearrange_numbers(n, k):
    count = -1
    if(k <= n//2):
        count = -1
        for value in range(1,n+1,2):
            count += 1
            if(count == k):
                return value
    else:
        count = n//2
        for value in range(2,n+1,2):
            count += 1
            if(count == k):
                return value


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(rearrange_numbers(n, k-1))
