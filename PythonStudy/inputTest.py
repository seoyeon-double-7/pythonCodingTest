# 데이터의 개수 입력
n = int(input())

# 각 데이터를 공백을 기준으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

# 65 90 75 34 99 => 입력
# [99, 90, 75, 65, 34] => 출력