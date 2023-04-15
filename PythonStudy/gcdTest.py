import math

# 최소 공배수(LCM)를 구하는 함수
def lcm(a, b):
    # 두 수를 곱하고 최대 공약수로 나눔
    # //는 소수점 이하 자릿수를 제거한 몫을 구하는 연산자(Floor Division)
    return a * b // math.gcd(a, b)

a=21
b=14

print(math.gcd(21, 14)) # 최대 공약수(GCD) 계산
print(lcm(21, 14))      # 최대 공배수(LCM) 계산