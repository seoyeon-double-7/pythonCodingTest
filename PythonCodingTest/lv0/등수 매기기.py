# 1. 첫 풀이
def solution(score):
    answer = []
    avg_score = []

    for i in score:
        #       평균으로 등수를 구하므로 소수점까지 계산해줘야됨 => // No No!!
        avg_score.append(sum(i) / 2)

    sort_score = sorted(avg_score, reverse=True)

    for n in avg_score:
        answer.append(sort_score.index(n) + 1)

    # return answer


# 2. 위의 풀이를 짧게 줄인 버전

def solution(score):
    avg_score = []
    for i in score:
        #       평균으로 등수를 구하므로 소수점까지 계산해줘야됨 => // No No!!
        avg_score.append(sum(i) / 2)
    return [sorted(avg_score, reverse=True).index(n) + 1 for n in avg_score]


# 3. 평균을 구하지 않고, 더해준 값을 정렬한 a배열과 score을 비교하여 등수 index값 넣어주기
# 여기서 index는 매개변수로 들어온 값과 동일한 가장 먼저 있는 값을 리턴
def solution(score):
    a = sorted([sum(i) for i in score], reverse=True)
    return [a.index(sum(i)) + 1 for i in score]