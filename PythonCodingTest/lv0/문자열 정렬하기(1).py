# 기본 풀이
# def solution(my_string):
#     answer = []
#     number = '0123456789'
#     answer = list(int(n) for n in my_string if n in number)
#     answer.sort()
#     return answer

# 문자열이 숫자로 이루어졌는지 판별하는 함수 isdigit 사용
# 정렬하고 새 리스트를 만들어서 반환하는 함수 sorted 사용
def solution(my_string):
    return sorted([int(n) for n in my_string if n.isdigit()])


# filter로 숫자만 걸러내기
# def solution(my_string):
#     return sorted(map(int, filter(lambda a: a.isdigit(), my_string)))


# 정규식 사용하기
# import re

# def solution(my_string):
#     return sorted(map(int, (list(re.sub('[^0-9]', '', my_string)))))