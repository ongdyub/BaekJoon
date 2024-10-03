import math
import heapq
from collections import deque

N, M, X = map(int, input().split(' '))

origin_g = dict()
reverse_g = dict()
for _ in range(N+1):
    origin_g[_] = []
    reverse_g[_] = []
    
for _ in range(M):
    s, e, w = map(int, input().split(' '))
    # heapq.heappush(origin_g[s], (w, e))
    # heapq.heappush(reverse_g[e], (w, s))
    origin_g[s].append((e,w))
    reverse_g[e].append((s,w))
    
dist2X = [math.inf] * (N+1)
X2dist = [math.inf] * (N+1)
dist2X[0] = 0
dist2X[X] = 0
X2dist[0] = 0
X2dist[X] = 0


# V_set = set([i for i in range(1,N+1)])
# start = X
# V_set.remove(X)
E = [(0, X)]
while E:
    _, start = heapq.heappop(E)
    
    for edge in origin_g[start]:
        u, w = edge
        
        if w > dist2X[u]:
            continue
        
        if dist2X[u] > w + dist2X[start]:
            dist2X[u] = w + dist2X[start]
            heapq.heappush(E, (dist2X[u], u))

E = [(0, X)]
while E:
    _, start = heapq.heappop(E)
    
    for edge in reverse_g[start]:
        u, w = edge
        
        if w > X2dist[u]:
            continue
        
        if X2dist[u] > w + X2dist[start]:
            X2dist[u] = w + X2dist[start]
            heapq.heappush(E, (X2dist[u], u))     

result = [a + b for a, b in zip(dist2X, X2dist)]
print(max(result))