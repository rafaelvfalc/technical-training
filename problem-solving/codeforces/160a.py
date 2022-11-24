def get_coins(coins):
    coins = sorted(coins, reverse=True)

    num_coins = 0
    coin_value = 0

    while(coins):
        num_coins += 1
        coin_value += coins.pop(0)
        if(coin_value > sum(coins)):
            return num_coins

    return num_coins

if __name__ == '__main__':
    n = int(input())
    coins = map(int, input().split())
    print(get_coins(coins))
