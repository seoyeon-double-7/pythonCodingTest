# index 함수 활용하기
# def solution(numbers):
#     temp = ''
#     answer = ''
#     alpha = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

#     for s in numbers:
#         temp += s
# #       문자열이 영어이면 index값을 넘겨주고 temp 초기화 후 다시 비교
#         if(temp in alpha):
#             answer = answer + str(alpha.index(temp))
#             temp = ''
#     return int(answer)

# 딕셔너리 활용하기
def solution(numbers):
    for num, word in enumerate(["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]):
        numbers = numbers.replace(word, str(num))
    return int(numbers)