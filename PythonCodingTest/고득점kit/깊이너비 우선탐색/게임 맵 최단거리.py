from collections import deque


def bfs(map, x, y, n, m):
    queue = deque()
    queue.append((x, y))

    #     큐가 빌때까지 수행하기
    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로 찾기 공간을 벗어난 경우 무시
            if (nx < 0 or nx >= n or ny < 0 or ny >= m):
                continue
            #     벽인 경우 무시
            if map[nx][ny] == 0:
                continue
            #     해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if map[nx][ny] == 1:
                map[nx][ny] = map[x][y] + 1
                queue.append((nx, ny))
                print(nx, ny)

    #      가장 오른쪽 아래까지의 최단 거리 반환
    return map[n - 1][m - 1]


def solution(maps):
    answer = 0

    map_n = len(maps)
    map_m = len(maps[0])

    answer = bfs(maps, 0, 0, map_n, map_m)
    print(answer)

    return answer if not answer == 1 else -1


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]