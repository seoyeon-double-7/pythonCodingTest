def solution(slice, n):
    answer = (n - 1) // slice + 1

    return answer# def solution(my_string):
#     answer = ''
#     remove_string = ('a,e,i,o,u')
#     for i in remove_string:
#         my_string = my_string.replace(i,'')

#     return my_string

# join 함수 사용하기
def solution(my_string):
    return ''.join([i for i in my_string if not i in ('aeiou')])