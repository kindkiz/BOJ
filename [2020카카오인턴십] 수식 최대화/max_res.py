from collections import deque
from itertools import permutations
import copy


def cal(num, op, order):
    temp_num = []
    a = 0
    for i in range(3):
        j = 0
        flag = False
        while order[i] in op and num:
            if len(num) != 1:
                temp_num.append(num.popleft())
            if op[j] == order[i]:
                if op[j] == '*':
                    num.appendleft((temp_num.pop() * num.popleft()))
                elif op[j] == '+':
                    num.appendleft((temp_num.pop() + num.popleft()))
                elif op[j] == '-':
                    num.appendleft((temp_num.pop() - num.popleft()))
                del op[j]
            else:
                j += 1
        while temp_num:
            num.appendleft(temp_num.pop())
        if len(num) == 1:
            break
    return num[0]


def solution(expression):
    numbers = deque([])
    oper = deque([])
    tmp = ''
    for i in expression:
        if i in ['*', '+', '-']:
            numbers.append(int(tmp))
            tmp = ''
            oper.append(i)
        else:
            tmp += i
    if tmp != '':
        numbers.append(int(tmp))
    answer = 0
    for i in list(permutations(['*', '+', '-'])):
        num = copy.deepcopy(numbers)
        op = copy.deepcopy(oper)
        answer = max(answer, abs(cal(num, op, i)))
    return answer
