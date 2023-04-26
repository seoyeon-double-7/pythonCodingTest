def solution(array):
    while len(array) != 0:
        #       set을 이용하여 배열의 모든 원소를 한 개씩 모두 소거
        #       최종적으로 값의 종류가 1개가 남을 경우(최빈값) i=0이므로 해당 값을 반환하고, 값의 종류가 두 개 이상이 남을 경우 i가 1이상이 되므로 -1을 반환합니다. [3, 3, 3, 1, 2]일때 한 번 반복을 돌면 원소의 종류[1, 2, 3]을 한 번씩 제거하고 [3, 3]이 됩니다. set([3, 3])은 (3)이 되므로 그럼 i는 0에서 끝납니다.

        for i, a in enumerate(set(array)):
            array.remove(a)
            print(i)
        if i == 0:
            return a
    return -1

# def solution(array):
#     answer = []
#     key = list(set(array))
#     count_num = []


#     key.sort(key=lambda x:array.count(x), reverse=True)

#     for key in array:
#         count_num.append(array.count(key))

#     return -1 if len(list(set(answer))) == 1 and len(answer)>=2 else key[0]


# def solution(array):
# 	count = [0] * (max(array)+1) # 숫자 출연 횟수를 셀 리스트

# 	for i in array:
# 		count[i] += 1

# 	m = 0 # 최빈값의 개수
# 	for c in count:
# 		if c == max(count):
# 			m += 1

# 	if m > 1: # 최빈값이 2개 이상이면 -1을 리턴
# 		return -1
# 	else: # 최빈값이 1개이면 해당 숫자를 리턴
# 		return count.index(max(count))

# from collections import Counter

# def solution(array):
#     cnt = Counter(array).items()
#     li = sorted(cnt,key=lambda x: -x[1])
#     if len(li)==1:
#         return li[0][0]
#     return li[0][0] if li[0][1]!=li[1][1] else -1
