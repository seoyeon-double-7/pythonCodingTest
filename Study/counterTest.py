from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

# 'blue'가 등장한 횟수 출력
# 3
print(counter['blue'])

# 1
# 'green'이 등장한 횟수 출력
print(counter['green'])

# {'red': 2, 'blue': 3, 'green': 1}
# 사전 자료형으로 반환
print(dict(counter))