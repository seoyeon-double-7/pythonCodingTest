def dfs(x,y):
#     범위체크
    if x<= -1 or x>= n or y<= -1 or y >= m:
        return False

    if graph[x][y] == 0:
    #     인접처리
        graph[x][y] = 1
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True

    return False

# N, M을 공백 기준으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []

for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0

for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result+=1

print(result)