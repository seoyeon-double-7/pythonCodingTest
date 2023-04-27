def solution(n):
    answer = []
    for num in str(n):
        answer.append(num)
    return int(''.join(sorted(answer, reverse=True)))
