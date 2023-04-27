# def solution(left, right):
#     dvs_num = []
#     dvs = 0
# #     left~right 약수의 개수 구하기
#     for i in range(left, right+1):
#         dvs=0
#         for j in range(1, i+1):
#             if i%j == 0:
#                 dvs+=1
#         dvs_num.append(dvs)

# #     약수의 개수가 짝수인 수 더하기
# #     약수의 개수가 홀수인 수 빼기

#     return sum(left+n if not dvs_num[n]%2 else -(left+n) for n in range(len(dvs_num)))

# 제곱수의 약수는 홀수라는 개념을 이용한 풀이
def solution(left, right):
    return sum(-i if int(i ** 0.5) == i ** 0.5 else i for i in range(left, right + 1))