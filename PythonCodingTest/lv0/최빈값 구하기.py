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

from collections import Counter


def solution(array):
    cnt = Counter(array).items()
    li = sorted(cnt, key=lambda x: -x[1])
    if len(li) == 1:
        return li[0][0]
    return li[0][0] if li[0][1] != li[1][1] else -1
