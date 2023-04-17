# 딕셔너리 사용
# def solution(rsp):
#     answer = ''
#     win = {'2':'0', '0':'5', '5':'2'}
#     for i in rsp:
#         answer += win[i]

#     return answer


# join, 딕셔너리 사용
def solution(rsp):
    win = {'2': '0', '0': '5', '5': '2'}

    return ''.join(win[i] for i in rsp)

# replace 이용
# def solution(rsp):
#     rsp =rsp.replace('2','s')
#     rsp =rsp.replace('5','p')
#     rsp =rsp.replace('0','r')
#     rsp =rsp.replace('r','5')
#     rsp =rsp.replace('s','0')
#     rsp =rsp.replace('p','2')
#     return rsp