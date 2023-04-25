# 리스트로 주어지는 네 좌표를 x 기준으로 먼저 정렬하고, x 가 같으면 y 기준으로 정렬
# 왼쪽 아래에 위치한 x, y 값에서 오른쪽 위에 위치한 x, y값을 통해 직사각형의 가로길이와 세로길이를 구하기
def solution(dots):
    answer = 0

    dots.sort(key=lambda x: (x[0], x[1]))
    print(dots[1])

    answer = abs(dots[0][0] - dots[3][0]) * abs(dots[0][1] - dots[3][1])

    return answer


# 사각형이 축에 평행하니까 max(dots) 좌표가 1시방향 끝점, min(dots) 좌표가 5시 방향 끝점
def solution(dots):
    return (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])