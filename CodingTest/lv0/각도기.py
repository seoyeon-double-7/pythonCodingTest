# 기본풀이
def solution(angle):
    if angle<=90:
        return 1 if angle<90 else 2
    else:
        return 3 if angle<180 else 4

    return answer


# 람다로
solution = lambda angle : 2 if angle==90 else 1 if angle<90 else 4 if angle==180 else 3


# 간단한 방법
def solution(angle):
    answer = (angle // 90) * 2 + (angle % 90 > 0) * 1
    return answer

# 검색
def solution(angle):
    angles = {180: 4, 91: 3, 90: 2, 0: 1}
    for base, result in angles.items():
        if angle >= base:
            return result