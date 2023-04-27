# def solution(phone_number):
#     len_phone =len(phone_number)
#     for i in range(len_phone):
#         if(i < len_phone-4):
#             answer.append('*')
#         else:
#             answer.append(phone_number[i])

#     return ''.join(answer)


# def solution(phone_number):
#     len_phone = len(phone_number)
#     return ''.join(['*' if i < (len_phone-4) else phone_number[i] for i in range(len_phone)])

def solution(p_number):
    return '*' * (len(p_number)-4) + p_number[-4::]