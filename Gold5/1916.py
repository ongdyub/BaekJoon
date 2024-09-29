import math
import heapq
from collections import deque

N = int(input())
M = int(input())

graph = [[]*(N+1) for _ in range(N+1)]
dist = [math.inf]*(N+1)
visit = set()

for _ in range(M):
    u, v, w = map(int, input().split(' '))
    graph[u].append((v,w))

S, E = map(int, input().split(' '))

travel = [(0,S)]
dist[S] = 0

while len(travel) > 0:
    dst, cur = heapq.heappop(travel)
    if cur in visit:
        continue
    visit.add(cur)

    for edge in graph[cur]:
        (end, weight) = edge

        if dist[end] < weight:
            continue

        if dist[cur] + weight < dist[end]:
            dist[end] = dist[cur] + weight

            if end not in visit:
                heapq.heappush(travel, (dist[end], end))
    
    

print(dist[E])