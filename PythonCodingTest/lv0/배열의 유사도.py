# def solution(s1, s2):
#     answer = 0
#     if(len(s1) < len(s2)):
#        # answer = sum(1 for i in s2 if i in s1)
#         answer = sum(1 for i in s2 if i in s1)
#     else:
#         answer = sum(1 for i in s1 if i in s2)
#     return answer

# 집합 형식으로 바꿔주는 set함수 이용
def solution(s1, s2):
    print(set(s1)&set(s1))
    return len(set(s1)&set(s2));