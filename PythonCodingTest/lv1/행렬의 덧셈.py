def solution(arr1, arr2):
    temp = []
    answer = []

    for i in range(len(arr1)):
        temp = []
        for n1, n2 in zip(arr1[i], arr2[i]):
            temp.append(n1 + n2)
        answer.append(temp)
    return answer


# 짧게
def solution(arr1, arr2):
    return [[n1 + n2 for n1, n2 in zip(arr1[i], arr2[i])] for i in range(len(arr1))]

    # return [[c + d for c, d in zip(a,b)] for a, b in zip(A,B)]


#    map 사용
def solution(A, B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]