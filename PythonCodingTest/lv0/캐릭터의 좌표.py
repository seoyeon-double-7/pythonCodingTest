# if, else문으로 비교
def solution(keyinput, board):
    answer = [0, 0]
    for k in keyinput:
        if (k == 'left' and answer[0] - 1 >= -(board[0] // 2)):
            answer[0] -= 1
        elif (k == 'right' and answer[0] + 1 <= board[0] // 2):
            answer[0] += 1
        elif (k == 'up' and answer[1] + 1 <= board[1] // 2):
            answer[1] += 1
        elif (k == 'down' and answer[1] - 1 >= -(board[1] // 2)):
            answer[1] -= 1

    return answer


# abs로 비교

def solution(keyinput, board):
    x_lim, y_lim = board[0] // 2, board[1] // 2
    move = {'left': (-1, 0), 'right': (1, 0), 'up': (0, 1), 'down': (0, -1)}
    x, y = 0, 0
    for k in keyinput:
        dx, dy = move[k]
        if abs(x + dx) > x_lim or abs(y + dy) > y_lim:
            continue
        else:
            x, y = x + dx, y + dy

    return [x, y]