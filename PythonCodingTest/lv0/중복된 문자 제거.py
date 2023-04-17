# def solution(my_string):
#     answer = ''
#     my_string = ''.join(list(set(my_string)))
#     return my_string


# not in 써서 풀이
# def solution(my_string):
#     answer = ''
#     for i in my_string:
#         if i not in answer:
#             answer += i
#     return answer

# dictionary를 이용하여 중복제거
# 딕셔너리는 key 값이 중복 불가!
# dict.fromkeys(iterable) => 인자로 들어온 iterable 데이터를 key 값으로 해서 딕셔너리 자료형을 만들어줌
def solution(my_string):
    return ''.join(dict.fromkeys(my_string))