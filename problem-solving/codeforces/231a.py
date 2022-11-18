def doQuestion(team_info):
    total = sum(int(char) for char in team_info if char.isdigit())
    return True if total > 1 else False


if __name__ == '__main__':
    n = int(input())

    count = 0
    for i in range(n):
        team_info = str(input())
        if(doQuestion(team_info)):
            count += 1
    print(count)
