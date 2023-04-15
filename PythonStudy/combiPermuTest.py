# 중복 순열
from itertools import product

data = ['A', 'B', 'C']

# 2개를 뽑는 모든 순열 구하기 (중복 허용)
result = list(product(data, repeat=2))
print(result)


# 중복 조합
from itertools import combinations_with_replacement

data = ['A', 'B', 'C']

# 2개를 뽑는 모든 조합 구하기 (중복 허용)
result = list(combinations_with_replacement(data, 2))
print(result)