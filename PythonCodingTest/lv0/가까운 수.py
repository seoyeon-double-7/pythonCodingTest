# def solution(array, n):
#     indexNum = 0
#     array.append(n)
#     array.sort()
#     indexNum = array.index(n)


# #     시작과 끝에 있는 경우
#     if(max(array) == n):
#         return array[indexNum-1]
#     if(min(array) == n):
#         return array[indexNum+1]

# #     같거나 왼쪽에 있는 수가 더 가까울 경우
#     if n - array[indexNum-1] < array[indexNum+1]-n or n - array[indexNum-1] == array[indexNum+1]-n:
#         return array[indexNum-1]
# #     오른쪽 수가 더 가까울 경우
#     else:
#         return array[indexNum+1]


# def solution(array, n):
#     sort key 값에 2개 항목을 넣을 수 있어요. 첫번째 정렬, 두번째 정렬인데 x-n을 넣어주는 이유는 abs(x-n)이 똑같은 경우 값 작은게 앞에 있게 하려고(거리가 같으면 작은값을 리턴)
# array.sort(key = lambda x : (abs(x-n), x-n))
#   answer = array[0]
#   return answer


def solution(array, n):
    return sorted(array, key=lambda x: (abs(x - n), x))[0]

# 람다식 활용
# solution=lambda a,n:sorted(a,key=lambda x:(abs(x-n),x))[0]