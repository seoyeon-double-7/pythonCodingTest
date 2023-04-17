# list comprehension 사용
def solution(order):
    return sum(1 for i in str(order) if i in ('369'))

# sum, count 함수 사용
# def solution(order):
#     return sum(map(lambda x: str(order).count(str(x)), [3, 6, 9]))

# def solution(order):
#     answer =0
#     num = 0

#     while(order):
#         num = order % 10
#         if(num % 3 == 0):
#             answer += 1
#         order = order // 10
#     return answer