from collections import deque

N = int(input())

# graph = [[0]*(N+1) for _ in range(N+1)]
graph = [[] for _ in range(N+1)]
visit = [False] * (N+1)
root = [0]*(N+1)

for _ in range(N-1):
    s, e = map(int, input().split(' '))
    # graph[s][e] = 1
    # graph[e][s] = 1
    graph[s].append(e)
    graph[e].append(s)
    

Q = deque()
Q.append(1)

root[1] = 1

while len(Q) > 0:
    cur_root = Q.popleft()
    
    for v in graph[cur_root]:
        if not root[v]:
            Q.append(v)
            root[v] = cur_root
            
for i in range(2,N+1):
    print(root[i])