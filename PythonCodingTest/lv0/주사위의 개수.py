# 기본 풀이
# def solution(box, n):
#     answer=1
#     # answer = (box[0]//n) * (box[1] //n) * (box[2]//n)

#     for i in box:
#         answer *= (i//n)

#     return answer


# 모든 요소의 곱을 계산하는 함수 math.prod
import math


def solution(box, n):
    return math.prod(map(lambda v: v // n, box))