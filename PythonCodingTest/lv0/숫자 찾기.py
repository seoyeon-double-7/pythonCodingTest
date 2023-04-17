# def solution(num, k):
#     n_list = list(map(int, str(num)))
#     return n_list.index(k)+1 if k in n_list else -1

# find 함수 사용하기
def solution(num, k):
    return -1 if str(k) not in str(num) else str(num).find(str(k)) + 1