def solution(n):
    subak = ['수', '박']
    answer = []

    for i in range(n):
        answer.append(subak[i % 2])

    return ''.join(answer)


def solution(n):
    str = '수박' * n
    return str[:n]