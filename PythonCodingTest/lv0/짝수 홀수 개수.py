# 기본 코드
# def solution(num_list):
#     answer = []
#     even=0
#     odd= 0
#     for i in num_list:
#         if(i%2):
#             odd+=1
#         else:
#             even+=1
#     answer.append(even)
#     answer.append(odd)

#     return answer


# map을 활용해서 풀기
def solution(num_list):
    # 홀수는 1, 짝수는 0
    answer = list(map(lambda n: n % 2, num_list))
    return [answer.count(0), answer.count(1)]

# 인덱싱을 활용한 풀이
# def solution(num_list):
#     answer=[0,0]

# #   0방은 짝수 1방은 홀수
#     for i in num_list:
#         answer[i%2] += 1
#     return answer
