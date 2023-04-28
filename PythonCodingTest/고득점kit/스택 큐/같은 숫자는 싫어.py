def solution(arr):
    return [arr[i] for i in range(len(arr)) if i == 0 or arr[i - 1] != arr[i]]


def solution(arr):
    temp = []

    for i in arr:
        #       연속적으로 나타난 숫자와 arr안에 들어있는 숫자가 같으면 temp에 값을 넣어주지 않음
        if temp[-1:] == [i]:
            continue
        #       새로운 숫자이면 temp에 넣어주기
        temp.append(i)
    return temp