# def solution(id_pw, db):
#     for i in db:
#         if id_pw[0] in i:
# #             아이디 맞고, 비번도 맞으면 => login
# #             아이디 맞았는데, 비번 틀리면 => wrong pw
#             if id_pw[1] in i:
#                 return 'login'
#             else:
#                 return 'wrong pw'
#     return 'fail'


def solution(id_pw, db):
    db_dict = {i[0]: i[1] for i in db}

    ID, PW = id_pw[0], id_pw[1]

    #     id 확인하기
    if ID in db_dict:
        #     id가 맞고, 다른 배열에서 비번이 같을 수 있으므로
        #     맞는 id가 들어있는 배열의 비번 값이 회원 비번과 같으면 login 리턴 => PW == db_dict[ID]
        #     in 연산자는 포함만 되어있으면 true를 리턴하기 때문에 ==연산자를 써야됨
        return 'login' if PW == db_dict[ID] else 'wrong pw'
    else:
        return 'fail'
