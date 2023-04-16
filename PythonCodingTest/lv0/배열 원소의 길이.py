def solution(strlist):
    answer = []
    for i in strlist:
        answer.append(len(i))
    return answer

# map 사용하기
# def solution(strlist):
#     answer = list(map(len, strlist))
#     return answer