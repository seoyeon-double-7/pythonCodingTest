def solution(num_list, n):
    answer = []
    cnt = 0
    temp = []

    for num in num_list:
        #     1차원 배열에 저장될 값
        temp.append(num)
        cnt += 1

        #     n될때마다 2차원 배열안에 1차원 배열 넣어주고, 초기화
        if cnt == n:
            answer.append(temp)
            temp = []
            cnt = 0
    return answer


# list와 range 활용해서!
def solution(num_list, n):
    answer = []
    for i in range(0, len(num_list), n):
        answer.append(num_list[i:i + n])
    return answer


# 간단한 코드!

def solution(num_list, n):
    return [num_list[i:i + n] for i in range(0, len(num_list), n)]