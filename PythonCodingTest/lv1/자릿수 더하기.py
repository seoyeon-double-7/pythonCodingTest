# list comprehension으로 푸는 방법
# def solution(n):
#     return sum([int(a) for a in str(n)])

# map 사용

def solution(n):
    return sum(map(int, str(n)))