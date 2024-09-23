from collections import deque

N, M = map(int, input().split(' '))

graph = [[0]*(N+1) for i in range(N+1)]
score = [[0]*(N+1) for i in range(N+1)]

Q = deque()
cnt = 0

for _ in range(M):
    s,e = map(int, input().split(' '))
    graph[s][e] = 1
    graph[e][s] = 1


for people in range(1, N+1):
    Q = deque([(people, 0)])
    visit = [False]*(N+1)
    # print("PP")
    # print(people)
    while len(Q) > 0:
        cur, step = Q.popleft()
        
        if visit[cur]:
            continue
        
        visit[cur] = True
        # print("Q")
        # print(f'{cur} {step}')
        score[people][cur] = step
        
        for i in range(1, N+1):
            if graph[cur][i] and not visit[i]:
                Q.append((i, step+1))
                # score[people][cur] = step+1
                # score[i][people] = step+1
                # visit[i] = True

score_sum = []

for idx, _ in enumerate(score):
    if idx == 0:
        continue
    score_sum.append(sum(_))
    
# print(score_sum)
print(score_sum.index(min(score_sum))+1)
