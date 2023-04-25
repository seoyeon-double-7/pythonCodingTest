# def solution(spell, dic):
#     answer = sorted(spell)
#     for s in dic:
#         if sorted(s) == answer:
#             return 1
#     return 2

# 집합의 특성 (차집합)을 활용하기
def solution(spell, dic):
    alpha = set(spell)
    for s in dic:
#       차집합 결과 값이 없을때 0이 아닌 set()을 반환
#       따라서 == 0이 아닌 not연산자를 이용
        if not alpha-set(s):
            print(alpha-set(s))
            return 1
    return 2