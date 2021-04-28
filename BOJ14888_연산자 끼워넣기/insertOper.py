from sys import stdin
from itertools import permutations
n = int(stdin.readline())
arr = list(map(int, stdin.readline().split()))
a, b, c, d = list(map(int, stdin.readline().split()))
oper = ['+'] * a + ['-'] * b + ['*'] * c + ['/'] * d
MAX = (-1) * float('inf')
MIN = float('inf')
for operators in list(permutations(oper)):
    result = arr[0]
    for i in range(n-1):
        if operators[i] == '+':
            result += arr[i+1]
        elif operators[i] == '-':
            result -= arr[i+1]
        elif operators[i] == '*':
            result *= arr[i+1]
        else:
            result = int(result / arr[i+1])
    if result > MAX:
        MAX = result
    if result < MIN:
        MIN = result

print(int(MAX))
print(int(MIN))
