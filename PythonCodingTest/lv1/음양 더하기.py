# def solution(absolutes, signs):
#     answer = 0

#     for s in range(len(signs)):
#         if signs[s]:
#             answer += absolutes[s]
#         else:
#             answer -= absolutes[s]

#     return answer

# zip 함수 이용하기
def solution(absolutes, signs):
    return sum(a if s else -a for a, s in zip(absolutes, signs))