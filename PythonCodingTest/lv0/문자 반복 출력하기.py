# lambda
# def solution(my_string, n):
#     return ''.join(map(lambda s: s*n, my_string))

def solution(my_string, n):
    return ''.join(i*n for i in my_string)