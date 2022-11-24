def is_dangerous(players):
    if(len(players) < 7):
        return 'NO'
    for players_seq in players.split('1'):
        if(len(players_seq) > 6):
            return 'YES'
    for players_seq in players.split('0'):
        if(len(players_seq) > 6):
            return 'YES'
    return 'NO'

if __name__ == '__main__':
    players = str(input())
    print(is_dangerous(players))
