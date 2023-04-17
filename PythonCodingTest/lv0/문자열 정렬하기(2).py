# def solution(my_string):
#     answer = []
#     # my_string = my_string.lower()
#     for s in my_string.lower():
#         answer.append(s)
#     answer.sort()
#     return ''.join(answer)


def solution(my_string):
    return ''.join(sorted(my_string.lower()))