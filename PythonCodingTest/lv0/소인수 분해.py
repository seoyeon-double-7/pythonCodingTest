def solution(n):
    answer = []
    #     2부터 n까지 나누기
    for i in range(2, n + 1):
        if (n % i == 0):
            answer.append(i)
            while (n % i == 0):
                n = n // i

    return answer