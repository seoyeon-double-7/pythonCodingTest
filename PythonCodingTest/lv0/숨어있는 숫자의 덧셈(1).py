# def solution(my_string):
# #     숫자면 number_list에 문자열 형태로 넣어주기
#     number_list = ''.join(s for s in my_string if s in '0123456789')
# #     숫자 문자열이 있는 number_list를 int로 변경
#     answer = sum(int(i) for i in number_list)
#     return answer

# 문자열에 숫자 있는지 체크하는 isdigit 함수 활용
def solution(my_string):
    return sum(int(i) for i in my_string if i.isdigit())

# re 라이브러리 sub 함수활용
# import re

# def solution(my_string):
#     return sum(int(n) for n in re.sub('[^1-9]', '', my_string))