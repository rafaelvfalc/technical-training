def countWinners(n, k, scores):
    k_th = int(scores[k-1])
    count = 0

    for score in scores:
        score = int(score)
        if score and score >= k_th:
            count += 1;

    return count

if __name__ == '__main__':
    n,k = map(int, input().split(' '))
    scores = input().split(' ')

    print(countWinners(n, k, scores))
