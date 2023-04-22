# def solution(my_string):
#     result = 0
#     op_data = []
#     temp = []
#     answer = {0:'+', 1:'-'}

#     for s in my_string:
#         if s == '+':
#             op_data.append(0)
#             my_string = my_string.replace('+', '')
#             print('+입니다')
#         elif s == '-':
#             op_data.append(1)
#             my_string = my_string.replace('-', '')
#             print('-입니다')
#         temp = my_string.split()


#         print(op_data)
#     # for n in (0, len(op_data)):
#     #     print(op_data)

#         # if op_data[n] == 0:
#             # result = my_string[n] + my_string[n+1]
#         # elif op_data[n] == 1 : ng[n+1]


#     return answer


# 문자열을 식으로 변환하여 실행하는 함수
# def solution(my_string):
#     return eval(my_string)


# split 함수 사용하기
def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))