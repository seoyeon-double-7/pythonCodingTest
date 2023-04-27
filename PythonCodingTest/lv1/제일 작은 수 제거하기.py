def solution(arr):
    min_num = arr.index(min(arr))
    if len(arr) > 1:
        arr.remove(arr[min_num])
        return arr
    else:
        return [-1]

# def solution(mylist):
#     return [i for i in mylist if i > min(mylist)] or [-1]    