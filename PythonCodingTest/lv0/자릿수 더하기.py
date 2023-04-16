# def solution(n):
#     answer = 0
#     while(n):
#         answer += n%10
#         n //= 10
#     return answer

# n을 문자열로 만들어주고 순회, list comprehension활용
def solution(n):
    return sum(int(i) for i in str(n))

# 정수를 문자열로 변환한 후 각 문자열을 int로 바꾸어 list에 삽입하고, list 원소를 더해줌
# def solution(n):
#     return sum(list(map(int, str(n))))