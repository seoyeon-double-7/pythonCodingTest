# def solution(sides):
#     maxNum = max(sides)
#     sides.remove(maxNum)
#     if sum(sides) > maxNum:
#         return 1
#     else:
#         return 2


# sort 사용해서 풀기
def solution(sides):
    sides.sort()
    return 1 if sides[2] < sides[0] + sides[1] else 2