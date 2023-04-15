import math

# 기본 풀이
def solution(num1, num2):
    answer = 0
    answer = 1000 * num1//num2
    return answer

# int로 변환
# solution = lambda num1, num2 : (int)(num1/num2 * 1000)

# trunc 함수 사용
# solution = lambda num1, num2 : math.trunc(num1/num2*1000)