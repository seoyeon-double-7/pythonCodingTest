# 첫 풀이
# def solution(n):
#     answer = 1

#     for i in range(1,100):
#         answer *= i
#         if(answer * i >= n):
#             return i


#     return answer

# facorial 함수 사용
import math


def solution(n):
    answer = 0
    for i in range(1, 12):
        if n < math.factorial(i):
            return i - 1
    return answer