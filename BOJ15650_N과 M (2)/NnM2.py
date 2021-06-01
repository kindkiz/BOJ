from sys import stdin
from itertools import combinations

n, m = list(map(int, stdin.readline().split()))
for line in list(combinations([i for i in range(1, n+1)], m)):
    for num in line:
        print(num, end=" ")
    print()
