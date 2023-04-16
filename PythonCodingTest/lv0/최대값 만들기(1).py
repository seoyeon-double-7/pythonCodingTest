# 가장 큰숫자를 삭제한 배열에서 큰숫자를 찾고 곱하는 방식
# def solution(numbers):
#     m1 =max(numbers)
#     index=0
#     for i in numbers:
#         if i == m1:
#             del(numbers[index])
#         index += 1
#     m2 = max(numbers)
#     answer = m1*m2
#     return answer

# 내림차순 정렬 후 첫번째, 두번째 값을 곱해주기
def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0]*numbers[1]