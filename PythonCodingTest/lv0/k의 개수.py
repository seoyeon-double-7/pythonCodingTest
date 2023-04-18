# 처음에 짠 🐶같은 코드 ㅎㅎ
# def solution(i, j, k):
#     answer = 0
#     find = str(k)

# #     i부터 j까지
#     for i in range (i, j+1):
#         # 숫자를 리스트로 만들어줌
#         n1 = list(str(i))

# #        리스트 안에 있는 숫자 중 찾는 값과 같으면 1 더하기
#         for j in n1:
#             if j == find:
#                 answer += 1
#     return answer

# count 함수 활용
def solution(i, j, k):
    answer = 0
    for n in range(i, j + 1):
        answer += str(n).count(str(k))
    return answer

# sum, lambda 함수 활용
# return sum([ str(i).count(str(k)) for i in range(i,j+1)])
# sum(map(lambda v: str(v).count(str(k)), range(i, j+1)))