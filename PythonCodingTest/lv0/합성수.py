# 기본풀이
def solution(n):
    answer = 0

    for i in range(n + 1):
        #       count 초기화
        count = 0
        for n in range(1, i + 1):
            if i % n == 0:
                count += 1

        if count >= 3:
            answer += 1

    return answer

# filter 사용
# def get_divisors(n):
#     return list(filter(lambda v: n % v ==0, range(1, n+1)))

# def solution(n):
#     return len(list(filter(lambda v: len(get_divisors(v)) >= 3, range(1, n+1))))