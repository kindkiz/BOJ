from sys import stdin

n, m = list(map(int, stdin.readline().split()))
table = [list(map(int, stdin.readline().split())) for i in range(n)]


def l():
    MAX = 0
    for i in range(n):
        for j in range(m-3):
            MAX = max(MAX, table[i][j]+table[i][j+1]+table[i][j+2]+table[i][j+3])
    for i in range(n-3):
        for j in range(m):
            MAX = max(MAX, table[i][j] + table[i+1][j] + table[i+2][j] + table[i+3][j])
    return MAX


def O():
    MAX = 0
    for i in range(n-1):
        for j in range(m-1):
            MAX = max(MAX, table[i][j] + table[i+1][j] + table[i][j+1] + table[i+1][j+1])
    return MAX


def T():
    MAX = 0
    for i in range(n-1):
        for j in range(m-2):
            MAX = max(MAX, table[i][j] + table[i][j+1] + table[i+1][j+1] + table[i][j+2])
    for i in range(1, n):
        for j in range(m-2):
            MAX = max(MAX, table[i][j] + table[i][j+1] + table[i][j+2] + table[i-1][j+1])
    for i in range(n-2):
        for j in range(m-1):
            MAX = max(MAX, table[i][j] + table[i+1][j] + table[i+1][j+1] + table[i+2][j])
    for i in range(n-2):
        for j in range(1, m):
            MAX = max(MAX, table[i][j] + table[i+1][j] + table[i+1][j-1] + table[i+2][j])
    return MAX


def L():
    MAX = 0
    for i in range(n-2):
        for j in range(m-1):
            MAX = max(MAX, table[i][j] + table[i+1][j] + table[i+2][j] + table[i+2][j+1])
            MAX = max(MAX, table[i][j] + table[i][j+1] + table[i+1][j] + table[i+2][j])
            MAX = max(MAX, table[i][j] + table[i][j+1] + table[i+1][j+1] + table[i+2][j+1])
            MAX = max(MAX, table[i][j+1] + table[i+1][j+1] + table[i+2][j+1] + table[i+2][j])
    for i in range(n-1):
        for j in range(m-2):
            MAX = max(MAX, table[i][j] + table[i][j+1] + table[i][j+2] + table[i+1][j+2])
            MAX = max(MAX, table[i][j] + table[i+1][j] + table[i][j+1] + table[i][j+2])
            MAX = max(MAX, table[i][j] + table[i+1][j] + table[i+1][j+1] + table[i+1][j+2])
            MAX = max(MAX, table[i+1][j] + table[i+1][j+1] + table[i+1][j+2] + table[i][j+2])
    return MAX


def S():
    MAX = 0
    for i in range(n-2):
        for j in range(m-1):
            MAX = max(MAX, table[i][j] + table[i+1][j] + table[i+1][j+1] + table[i+2][j+1])
            MAX = max(MAX, table[i][j+1] + table[i+1][j] + table[i+1][j+1] + table[i+2][j])
    for i in range(n-1):
        for j in range(m-2):
            MAX = max(MAX, table[i+1][j] + table[i+1][j+1] + table[i][j+1] + table[i][j+2])
            MAX = max(MAX, table[i][j] + table[i+1][j+1] + table[i][j+1] + table[i+1][j+2])
    return MAX


print(max(max(l(), O()), max(max(T(), L()), S())))
