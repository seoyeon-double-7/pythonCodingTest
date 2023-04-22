# 첫번째 풀이
# def solution(sides):
#     answer=0
#     a= min(sides)
#     b= max(sides)

#     if(b-a == 1):
#         return 1

# #     가장 긴변이 sides(a,b) => b일 경우
# #     b-a < answer <= b
#     answer += sum(1 for i in range(b-a+1, b+1))
# #     나머지 한 변이 가장 긴변인 경우
# #     b < answer <a+b
#     answer += sum(1 for i in range(b+1, a+b))
#     return answer


# range와 len을 사용(푸는 방식은 위와 동일)
# def solution(sides):
#     return len(range(max(sides) + 1, sum(sides))) + len(range(max(sides) - min(sides) + 1, max(sides) + 1))


# 수학적으로 풀기 ^^
# 가장 긴변이 sides에 있을 때 => c< a < a+b 따라서 a => b-1개
# 나머지 한변이 가장 긴변일때 => c < a < b+c 따라서 a=> b-1개
# 같을 때 1가지
# 다 합하면 2*b-1
def solution(sides):
    return 2 * min(sides) - 1
