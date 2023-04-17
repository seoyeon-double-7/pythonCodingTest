# def solution(cipher, code):
#     answer = ''

# #     16/2 = 8
# #     0~16 => 2 4 6 8 16
#     for i in range(code, len(cipher)+1, code):
#         answer += cipher[(i-1)]

#     return answer

def solution(cipher, code):
    #     code-1부터 마지막 index까지 code 간격에 있는 값을 answer에 넣어줌
    answer = cipher[code - 1::code]
    return answer


# list comprehension 활용
def solution(cipher, code):
    return ''.join(cipher[i] for i in range(code - 1, len(cipher), code))