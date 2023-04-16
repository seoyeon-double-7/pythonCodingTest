import math

# def solution(n, k):
#     answer = 0
#     answer = 12000*n + k*2000 - math.floor(n/10) * 2000
#     return answer


solution = lambda n, k : 12000 * n + 2000 * (k - n // 10)