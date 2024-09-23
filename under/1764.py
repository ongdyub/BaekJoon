N, M = map(int, input().split(' '))

n = []
m = []

for _ in range(N):
    n.append(input())
for _ in range(M):
    m.append(input())
    
n = set(n)
m = set(m)

out = n & m
out = sorted(out)
print(len(out))

for o in out:
    print(o)