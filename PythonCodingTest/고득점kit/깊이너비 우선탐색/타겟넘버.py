# 참고 : https://daeun-computer-uneasy.tistory.com/69?category=1053494

# ------- BFS --------

def solution(numbers, target):
    leaves = [0]  # 모든 계산 결과를 탐지
    count = 0

    for num in numbers:
        #         temp 초기화
        temp = []

        #       leaf는 부모 노드의 합
        for leaf in leaves:
            #         자손노드
            temp.append(leaf + num)
            temp.append(leaf - num)
        #       해당 노드까지 합해준 값 넣기
        leaves = temp

    #   모든 경우의 수 계산 후 target과 같은지 확인
    for leaf in leaves:
        if leaf == target:
            count += 1

    return count


# ------- DFS ----------

def dfs(numbers, target, idx, values):
    global cnt
    cnt = 0

    #     깊이가 끝까지 닿았으면
    if idx == len(numbers) & values == target:
        cnt += 1
        return
    #     끝까지 탐색했는데 sum이 target과 다르면 넘어가기
    elif idx == len(numbers):
        return

    #     재귀함수
    #     새로운 idx, values 값 세팅
    dfs(numbers, target, idx+1, values + numbers[idx])
    dfs(numbers, target, idx+1, values - numbers[idx]

    )

    def solution(numbers, target):
        global cnt
        dfs(numbers, target, 0, 0)

        return cnt