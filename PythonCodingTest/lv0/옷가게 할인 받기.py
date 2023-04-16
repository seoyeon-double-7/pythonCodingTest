# def solution(price):
#     answer = 0

#     cprice = price/100000
#     answer = price * 0.8 if(cprice >=5) else price*0.9 if(cprice>=3) else price*0.95 if(cprice >= 1) else price

#     # if(cprice >= 5):
#     #     answer = price * 0.8
#     # elif(cprice >= 3):
#     #     answer = price * 0.9
#     # elif(cprice >= 1):
#     #     answer = price * 0.95
#     # else:
#     #     answer = price
#     return int(answer)

# 딕셔너리 사용하기
def solution(price):
    discount_rates = {500000: 0.8, 300000: 0.9, 100000: 0.95, 0: 1}
    for discount_price, discount_rate in discount_rates.items():
        if price >= discount_price:
            return int(price * discount_rate)
