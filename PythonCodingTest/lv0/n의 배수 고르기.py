# def solution(n, numlist):
#     answer = []
#     for i in numlist:
#         if i%n == 0:
#             answer.append(i)

#     return answer


#     list comprehension 활용
# def solution(n, numlist):
#     return [i for i in numlist if not i%n]

# filter 활용
def solution(n, numlist):
    return list(filter(lambda i: not i % n, numlist))