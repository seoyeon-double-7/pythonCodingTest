import math
def solution(n, t):
#   마리수에 2씩 증가하는 수를 곱함
    return n * math.pow(2, t)

# 비트 연산자 사용
# def solution(n, t):
#     return n << t