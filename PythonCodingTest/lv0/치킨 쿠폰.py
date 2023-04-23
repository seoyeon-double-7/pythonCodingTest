# 쿠폰 개수 => 치킨수를 10으로 나눈 목과 나머지의 합
# 치킨 개수 => 쿠폰개수를 10으로 나눈 목
def solution(chicken):
    cupon = chicken
    answer = 0

    while (cupon >= 10):
        n = cupon // 10
        answer += n
        cupon = n + cupon % 10

    return answer

# 간단한 풀이
# def solution(chicken):
#     answer = (max(chicken,1)-1)//9
#     return answer