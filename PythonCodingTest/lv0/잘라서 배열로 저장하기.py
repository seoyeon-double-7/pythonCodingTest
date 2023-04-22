# 슬라이싱 사용
def solution(my_str, n):
    answer = []

    #     0~5 6~11 12~15
    #     0~2 3~5 6~8

    for i in range(0, len(my_str), n):
        answer.append(my_str[i:i + n:])
    return answer


# list comprehension 사용하여 간단하게 표현
def soulution(my_str, n):
    return [my_str[i:i + n:] for i in range(0, len(my_str), n)]
