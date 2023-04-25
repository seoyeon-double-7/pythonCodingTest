# def solution(bin1, bin2):
#     a1, a2 = (int(bin1,2), int(bin2,2))
#     return format((a1+a2),'b')


# 2진수 문자열 bin1, bin2를 10진수 int로 바꿔서 더해주고
# 10진수를 2진수로 바꿔조는 함수 bin을 사용해서 2진수 문자열로 저장
# bin함수를 사용하면 앞에 접두어 2개가 붙기때문에 [2:]를 사용해서 2글자 빼줌
def solution(bin1, bin2):
<<<<<<< HEAD
    answer = bin(int(bin1,2) + int(bin2,2))[2:]
    return answer
=======
    answer = int(bin1, 2) + int(bin2, 2)
    return bin(answer)[2::]
>>>>>>> 53a4140aecfda61ad355354b26a5cffc099a6bbf
