from collections import deque
import heapq

nxt_G = []
V, E = map(int, input().split(' '))

s = int(input())

int_max = 20001 * 1000

graph = [[] for i in range(V+1)]
dist = [int_max]*(V+1)
visit = set()

for _ in range(E):
    u, v, w = map(int, input().split(' '))
    graph[u].append((v,w))
    # graph[u][v] = w
    
    
heapq.heappush(nxt_G, (0, s))
dist[s] = 0

while len(nxt_G) > 0:
    dst, cur = heapq.heappop(nxt_G)
    visit.add(cur)
    # nxt_G = []
    
    for edge in graph[cur]:
        (v, w) = edge
        # print(f'{cur} {v} {w}')
        if dist[v] < w:
            continue
        
        if dist[cur] + w < dist[v]:
            dist[v] = dist[cur] + w
        
            if v not in visit:
                heapq.heappush(nxt_G, (dist[v], v))
    
for i in range(1,V+1):
    if dist[i] == int_max:
        print("INF")
    else:
        print(dist[i])