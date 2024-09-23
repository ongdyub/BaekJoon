
N, M = map(int, input().split(' '))

graph = []

for i in range(N):
    col = list(map(int, input().split(' ')))
    graph.append(col)
    
sum_graph = [[0]*N for i in range(N)]

sum_graph[0][0] = graph[0][0]

for y in range(1,N):
    sum_graph[0][y] = sum_graph[0][y-1] + graph[0][y]
for x in range(1,N):
    sum_graph[x][0] = sum_graph[x-1][0] + graph[x][0]
    
for x in range(1,N):
    for y in range(1,N):
        sum_graph[x][y] = sum_graph[x-1][y] + sum_graph[x][y-1] + graph[x][y] - sum_graph[x-1][y-1]
        
# print(sum_graph)
        
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split(' '))
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1
    
    lx, ly = x2, y1-1
    ux, uy = x1-1, y2
    cx, cy = x1-1, y1-1
    
    lsum = sum_graph[lx][ly] if ly >= 0 else 0
    usum = sum_graph[ux][uy] if ux >= 0 else 0
    csum = sum_graph[cx][cy] if cx >= 0 and cy >= 0 else 0
    # print(f'{lsum} {usum} {csum}')
    print(sum_graph[x2][y2]-lsum-usum+csum)