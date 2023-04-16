# 기본 풀이

# def solution(n):
#     for i in range(1,n):
#         if n == i * i:
#             return 1
#     return 2

# 0.5제곱 활용 => 루트
def solution(n):
    return 1 if not (n ** 0.5) % 1 else 2


# import math

# def solution(n):
#     return 1 if int(math.sqrt(n)) ** 2 == n else 2


