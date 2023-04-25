from math import gcd


def solution(a, b):
    #     b를 a,b의 최소공약수로 나눠주기
    b //= gcd(a, b)

    while (b % 2 == 0):
        b //= 2  # 2로 나눠떨어질때까지 나눠주기
    while (b % 5 == 0):
        b //= 5  # 5로 나눠떨어질때까지 나눠주기

    return 1 if b == 1 else 2