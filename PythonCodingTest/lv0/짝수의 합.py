# 기본 풀이
def solution(n):
    answer = 0
    for i in range(2, n+1, 2):
        answer += i
    return answer


# n까지 수 중 짝수만 리스트에 넣어준 후 더해주기
solution = lambda n: sum([i for i in range(2, n + 1, 2)])

# 위의 방법과 비슷함
solution = lambda n: sum(range(0, n+1, 2))

# 등차수열 2n의 합 공식 이용하기
def solution(n):
    return 2*(n//2)*((n//2)+1)/2