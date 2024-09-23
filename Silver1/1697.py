from collections import deque

N, K = map(int, input().split(' '))

Q = deque([(0, N)])
step = 1

visit = [False] * 200002

while N != K:
    
    (step, N) = Q.popleft()
    # print(N)
    if visit[N] == True:
        continue
    else:
        visit[N] = True
        step += 1
        if 0 <= N-1 and N-1 < 100001:
            Q.append((step, N-1))
        if 0 <= N+1 and N+1 < 100001:
            Q.append((step, N+1))
        if 0 <= N*2 and N*2 < 100001:
            Q.append((step, N*2))
        # print("NExT")
        # print(N)
    

print(step-1)