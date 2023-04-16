# height보다 큰 값이 있을 때 answer을 증가
# def solution(array, height):
#     answer = 0

#     for i in array:
#         if(i > height):
#             answer +=1
#         else:
#             continue
#     return answer

# 간단하게
# def solution(array, height):
#     return sum(1 for a in array if a > height)


# filter로 큰 개수세기
def solution(array: list, height: int) -> int:
    answer = len(list(filter(lambda x: x > height, array)))
    return answer

