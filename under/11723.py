import copy
import sys

input = sys.stdin.readline

_ = int(input())

al = set([i for i in range(1,21)])
empth = set([])

target = set([])

for __ in range(_):
    command = input().split(' ')
    # print(command)
    if len(command) == 2:
        x = int(command[1])
        if command[0] == 'add':
            target.add(x)
        elif command[0] == 'remove':
            try:
                target.remove(x)
            except:
                pass
        elif command[0] == 'toggle':
            if x in target:
                target.remove(x)
            else:
                target.add(x)
        elif command[0] == 'check':
            if x in target:
                print(1)
            else:
                print(0)
    else:
        if command[0] == 'all\n' or command[0] == 'all':
            target = target | al
        elif command[0] == 'empty\n' or command[0] == 'empty':
            target = target & empth
    # print(target)