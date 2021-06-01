from sys import stdin
from itertools import permutations

n, m = list(map(int, stdin.readline().split()))
arr = list(map(int, stdin.readline().split()))
arr = sorted(list(permutations(arr, m)))
for line in arr:
    for num in line:
        print(num, end=" ")
    print()
