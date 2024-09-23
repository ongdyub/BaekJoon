
N, M, B = map(int, input().split(' '))

graph = [[0]*M for i in range(N)]

ans_time = 500*500*256*2
ans_height = 0

for i in range(N):
    row = list(map(int, input().split(' ')))
    graph[i] = row
    
min_height = 256
max_height = 0

for y in range(N):
	min_height = min(min_height,min(graph[y]))
	max_height = max(max_height,max(graph[y]))

for height in range(min_height, max_height+1):
    cut = 0
    stack = 0
    time = 0
    
    for x in range(N):
        for y in range(M):
            if height > graph[x][y]:
                stack += (height - graph[x][y])
                time += (height - graph[x][y])
            if height < graph[x][y]:
                cut += (graph[x][y] - height)
                time += (2*(graph[x][y] - height))
    
    if B + cut < stack:
        break
    
    if time <= ans_time:
        ans_time = time
        ans_height = height
        
print(f'{ans_time} {ans_height}')
        