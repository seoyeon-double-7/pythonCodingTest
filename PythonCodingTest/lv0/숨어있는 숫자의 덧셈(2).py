# def solution(my_string):
#     for s in my_string:
#         if(s.isalpha()):
# #             알파벳이 있는 곳은 공백으로 구분시켜주기
#             my_string = my_string.replace(s,' ')
#     return sum (int(i) for i in my_string.split())

def solution(my_string):
    s = ''.join(s if s.isdigit() else ' ' for s in my_string )
    return sum(int(n) for n in s.split())