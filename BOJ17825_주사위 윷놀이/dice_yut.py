from sys import stdin
dice = list(map(int, stdin.readline().split()))

board = [i * 2 for i in range(0, 20)]
board += [13, 16, 19] + [22, 24] + [28, 27, 26] + [25, 30, 35, 40, 0]
piece_pos = [0, 0, 0, 0]
max_score = 0


def move(start, value):
    if start == 5:
        start = 20
        value -= 1
    if start == 10:
        start = 23
        value -= 1
    if start == 15:
        start = 25
        value -= 1
    if start < 20:
        if start + value >= 20:
            value -= (20 - start)
            start = 31
    if 20 <= start <= 22:
        if start + value > 22:
            value -= (23 - start)
            start = 28
    if 23 <= start <= 24:
        if start + value > 24:
            value -= (25 - start)
            start = 28
    if start + value > 32:
        return 32
    else:
        return start + value


def dfs(count, score):
    global max_score
    if count == 10:
        if max_score < score:
            max_score = score
        return
    for i in range(4):
        if piece_pos[i] == 32:
            continue
        pre_pos = piece_pos[i]
        next_pos = move(piece_pos[i], dice[count])
        if next_pos in piece_pos and next_pos != 32:
            continue
        piece_pos[i] = next_pos
        dfs(count+1, score + board[next_pos])
        piece_pos[i] = pre_pos


dfs(0, 0)
print(max_score)
