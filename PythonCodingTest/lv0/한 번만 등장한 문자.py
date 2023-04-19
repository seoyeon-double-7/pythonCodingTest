# 첫번째 코드
# def solution(s):
#     answer = ''
#     temp = sorted(set(s))
#     count=0

#     for i in temp:
#         if s.count(i) == 1:
#             answer += ''.join(temp[count])
#         count+=1

#     return answer


# list comprehension으로 간단하게!
def solution(s):
    return ''.join(sorted([c for c in s if s.count(c) == 1]))
