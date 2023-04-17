# 첫번째 코드
# def solution(numbers):
#     numbers.sort(reverse=True)

#     answer = numbers[0] * numbers[1]
#     mnumbers = []


#     for i in numbers:
#         if i < 0:
#             mnumbers.append(abs(i))

#     if len(mnumbers) >= 2:
#         mnumbers.sort(reverse=True)
#         manswer = mnumbers[0]*mnumbers[1]
#         if manswer > answer:
#             answer = manswer

#     return answer


# 정리한 코드

def solution(numbers):
    #    양수 최댓값
    numbers.sort(reverse=True)
    answer = numbers[0] * numbers[1]

    #   음수 리스트
    mnumbers = sorted([-i for i in numbers if i < 0], reverse=True)

    if len(mnumbers) >= 2:
        manswer = mnumbers[0] * mnumbers[1]
        if manswer > answer:
            return manswer

    return answer

# 간단한;; 코드
# def solution(numbers):
#     numbers = sorted(numbers)
# #     음수, 양수 비교
#     return max(numbers[0] * numbers[1], numbers[-1]*numbers[-2]) 