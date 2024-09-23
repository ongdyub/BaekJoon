import copy

N = int(input())

sort = []

target = list(map(int, input().split(' ')))

target_set = set(target)
target_set = sorted(target_set)

dic = {}

for idx, s in enumerate(target_set):
    dic[s] = idx

# print(dic)
# print(target_set)

for t in target:
    print(dic[t], end=' ')