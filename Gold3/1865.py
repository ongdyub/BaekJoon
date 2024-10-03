import math

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split(' '))
    graph = dict()
    dist = [math.inf] * (N+1)
    
    for _ in range(N+1):
        graph[_] = dict()
        graph[_][_] = 0
        
    for _ in range(M):
        s, e, t = map(int, input().split(' '))
        
        if e in graph[s] and graph[s][e] < t:
            continue
        
        graph[s][e] = t
        graph[e][s] = t        
        
    for _ in range(W):
        s, e, t = map(int, input().split(' '))
        
        if e in graph[s] and graph[s][e] < -t:
            continue
        
        graph[s][e] = -t
        
    # start
    for init in range(1,N+1):
        dist = [math.inf] * (N+1)
        dist[0] = 0
        dist[init] = 0
        change = set()
        change.add(init)
        
        ans = 'NO'
        found = False
        for _ in range(N):
            if _ == N-1:
                for s in range(1,N+1):
                    for e in graph[s].keys():
                        w = graph[s][e]
                        
                        if dist[e] > dist[s] + w:
                            ans = 'YES'
                            found = True
                            break
                    if found:
                        break
                            
            else:
                for s in range(1,N+1):
                    if s in change:
                        change.remove(s)
                        
                        for e in graph[s].keys():
                            w = graph[s][e]
                            
                            if dist[e] > dist[s] + w:
                                dist[e] = dist[s] + w
                                change.add(e)
                            
        if ans == 'YES':
            break
    print(ans)
                
                