# def solution(quiz):
#     answer = []

#     for q in quiz:
#         ex = q[:q.find('=')-1]

#         if eval(ex) == int(q[q.find('=')+1:]):
#             answer.append('O')
#         else:
#             answer.append('X')
#     return answer


# 간단하게
def solution(quiz):
    return ['O' if eval(q[:q.find('=') - 1]) == int(q[q.find('=') + 1:]) else 'X' for q in quiz]