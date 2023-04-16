def solution(n):
    answer = []

    for i in range(n + 1):
        if i % 2:
            answer.append(i)
    answer.sort()
    return answer

#  range 사용
# def solution(n):
#     return list(range(1, n+1, 2))