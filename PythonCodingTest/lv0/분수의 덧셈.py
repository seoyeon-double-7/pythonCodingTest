# 최대공약수 함수 사용

import math


def solution(numer1, denom1, numer2, denom2):
    numer = denom1 * numer2 + denom2 * numer1  # 분자
    denom = denom1 * denom2  # 분모
    gcd = math.gcd(denom, numer)  # 최대공약수 구하기
    return [numer // gcd, denom // gcd]


# 유클리드 호제법 사용
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(numer1, denom1, numer2, denom2):
    numer = denom1 * numer2 + denom2 * numer1  # 분자
    denom = denom1 * denom2  # 분모
    g = gcd(denom, numer)  # 최대공약수 구하기
    return [numer // g, denom // g]