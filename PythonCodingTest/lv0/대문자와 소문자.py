# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i.isupper():
#             answer += i.lower()
#         else:
#             answer += i.upper()


#     return answer

# 대소문자 전환 함수 swapcase 사용
# def solution(my_string):
#     return my_string.swapcase()


def solution(my_string):
    return ''.join(s.lower() if s.isupper() else s.upper() for s in my_string)