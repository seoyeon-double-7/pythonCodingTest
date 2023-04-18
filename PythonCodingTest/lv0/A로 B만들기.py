# def solution(before, after):
#     # if(before[::-1] == after):
#     #     return 1
#     # else :
#     #     return 0
#     before.lower()
#     after.lower()
#     before = list(before)
#     before.reverse()
#     return 1 if after == ''.join(before) else 0

def solution(before, after):
#     문자 자체를 정렬해서 비교하는 방법
    return 1 if sorted(before)==sorted(after) else 0