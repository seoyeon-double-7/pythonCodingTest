# def solution(s):
#     answer = ''
#     temp = sorted(set(s))
#     count=0

#     for i in temp:
#         if s.count(i) == 1:
#             answer += ''.join(temp[count])
#         count+=1

#     return answer


def solution(s):
    return ''.join(sorted([c for c in s if s.count(c) == 1]))
