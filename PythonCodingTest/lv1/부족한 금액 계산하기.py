def solution(price, money, count):
#     돈이 부족하지 않은 경우에는 남는 돈이 아닌 0을 출력
    return sum(price*i for i in range(1, count+1)) - money if rq_money > money else 0

def solution(price, money, count):
    return abs(min(money-sum(price*i for i in range(1, count+1)), 0))

# 등차수열의 합
def solution(price, money, count):
    return max(0,price*(count+1)*count//2-money)