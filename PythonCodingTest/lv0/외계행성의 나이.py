# 리스트에 알파벳 값 넣고, => 인덱스를 사용하여 나이 계산하기
# def solution(age):
#     answer = ''
#     alpha = ["a", "b", "c", "d", "e", "f","g", "h", "i", "j"]

#     for i in str(age):
#         answer += alpha[int(i)]

#     return answer

# 아스키코드 활용하기
# a => 97

def solution(age):
    return ''.join([chr(int(i) + 97) for i in str(age)])
