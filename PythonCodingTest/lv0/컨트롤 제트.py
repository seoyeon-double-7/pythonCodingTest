# def solution(s):
#     answer = 0
#     l = s.split(' ')

#     for i in range(0, len(l)):
#         if str(l[i]) == 'Z':
#             continue
#         elif i < len(l) -1:
#             if str(l[i+1]) == 'Z':
#                 continue
#             else:
#                 answer += int(l[i])
#         else:
#                 answer += int(l[i])

#     return answer


def solution(s):
    stack = []

    for a in s.split():
        if a != 'Z':
            stack.append(int(a))
        else:
            if stack:
                #               Z 앞에 있는 마지막 숫자 제거
                stack.pop()

    return sum(stack)