from collections import deque

N = int(input())

visit = [[False]*N for i in range(N)]

graph = [[0]*N for i in range(N)]

for x in range(N):
    l = input()
    for y in range(N):
        graph[x][y] = l[y]
        
Q = deque()

cnt_no = 0
for x in range(N):
    for y in range(N):
        if visit[x][y]:
            continue
        else:
            Q.append((x,y,graph[x][y]))
            while len(Q) > 0:
                (cur_x, cur_y, color) = Q.popleft()

                if visit[cur_x][cur_y]:
                    continue
                else:
                    visit[cur_x][cur_y] = True
                    
                    ad_x = cur_x+1 if cur_x < N-1 else N-1
                    mi_x = cur_x-1 if cur_x > 0 else 0
                    ad_y = cur_y+1 if cur_y < N-1 else N-1
                    mi_y = cur_y-1 if cur_y > 0 else 0
                    # print(f'{cur_x} {cur_y} {cur_x} {ad_y} {step}')
                    if not visit[cur_x][ad_y] and graph[cur_x][ad_y] == color:
                        Q.append((cur_x, ad_y, graph[cur_x][ad_y]))
                    if not visit[cur_x][mi_y] and graph[cur_x][mi_y] == color:
                        Q.append((cur_x, mi_y, graph[cur_x][mi_y]))
                    if not visit[ad_x][cur_y] and graph[ad_x][cur_y] == color:
                        Q.append((ad_x, cur_y, graph[ad_x][cur_y]))
                    if not visit[mi_x][cur_y] and graph[mi_x][cur_y] == color:
                        Q.append((mi_x, cur_y, graph[mi_x][cur_y]))
            
            cnt_no += 1
            
            
visit = [[False]*N for i in range(N)] 
for x in range(N):
    for y in range(N):
        if graph[x][y] == 'R':
            graph[x][y] = 'G'
                   
Q = deque()
cnt_yes = 0

for x in range(N):
    for y in range(N):
        if visit[x][y]:
            continue
        else:
            Q.append((x,y,graph[x][y]))
            while len(Q) > 0:
                (cur_x, cur_y, color) = Q.popleft()

                if visit[cur_x][cur_y]:
                    continue
                else:
                    visit[cur_x][cur_y] = True
                    
                    ad_x = cur_x+1 if cur_x < N-1 else N-1
                    mi_x = cur_x-1 if cur_x > 0 else 0
                    ad_y = cur_y+1 if cur_y < N-1 else N-1
                    mi_y = cur_y-1 if cur_y > 0 else 0
                    # print(f'{cur_x} {cur_y} {cur_x} {ad_y} {step}')
                    if not visit[cur_x][ad_y] and graph[cur_x][ad_y] == color:
                        Q.append((cur_x, ad_y, graph[cur_x][ad_y]))
                    if not visit[cur_x][mi_y] and graph[cur_x][mi_y] == color:
                        Q.append((cur_x, mi_y, graph[cur_x][mi_y]))
                    if not visit[ad_x][cur_y] and graph[ad_x][cur_y] == color:
                        Q.append((ad_x, cur_y, graph[ad_x][cur_y]))
                    if not visit[mi_x][cur_y] and graph[mi_x][cur_y] == color:
                        Q.append((mi_x, cur_y, graph[mi_x][cur_y]))
            
            cnt_yes += 1
            
            



# print(len(visit_Q))
# print(visit_cnt)
# print(check)

print(f'{cnt_no} {cnt_yes}')