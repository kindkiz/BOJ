from sys import stdin
adj = {
    10:[1, 3, 4, 5, 2, 3, 4, 1, 2, 3],
    11:[1, 5, 4, 3, 4, 3, 2, 3, 2, 1],
    1:[4, 0, 1, 2, 1, 2, 3, 2, 3, 4],
    2:[3, 1, 0, 1, 2, 1, 2, 3, 2, 3],
    3:[4, 2, 1, 0, 3, 2, 1, 4, 3, 2],
    4:[3, 1, 2, 3, 0, 1, 2, 1, 2, 3],
    5:[2, 2, 1, 2, 1, 0, 1, 2, 1, 2],
    6:[3, 3, 2, 1, 2, 1, 0, 3, 2, 1],
    7:[2, 2, 3, 4, 1, 2, 3, 0, 1, 2],
    8:[1, 3, 2, 3, 2, 1, 2, 1, 0, 1],
    9:[2, 4, 3, 2, 3, 2, 1, 2, 1, 0],
    0:[0, 4, 3, 4, 3, 2, 3, 2, 1, 2],
}


def solution(numbers, hand):
    answer = []
    right = 11
    left = 10
    for i in numbers:
        if i in [1, 4, 7]:
            answer.append('L')
            left = i
        elif i in [3, 6, 9]:
            answer.append('R')
            right = i
        else:
            if adj[right][i] < adj[left][i]:
                answer.append('R')
                right = i
            elif adj[left][i] < adj[right][i]:
                answer.append('L')
                left = i
            else:
                if hand == 'right':
                    answer.append('R')
                    right = i
                else:
                    answer.append('L')
                    left = i
    return ''.join(answer)
