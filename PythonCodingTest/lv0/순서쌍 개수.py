# 약수 구하기

def solution(n):
    return len([s for s in range(1, n+1) if n%s == 0])