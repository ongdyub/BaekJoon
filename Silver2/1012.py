from collections import deque

def assign_matrix(mat, K):
    for _ in range(K):
        X, Y = map(int, input().split(' '))
        mat[Y][X] = 1
        
    return mat

def DFS(visit, mat, n, m, Q, N, M):
    while len(Q) > 0:
        # 현재꺼 방문
        (cur_x, cur_y) = Q.pop()
        visit[cur_x][cur_y] = True
        
        # 다음꺼 생성 위
        up_x = cur_x-1 if cur_x > 0 else 0
        down_x = cur_x+1 if cur_x < N-1 else N-1
        left_y = cur_y-1 if cur_y > 0 else 0
        right_y = cur_y+1 if cur_y < M-1 else M-1
        
        if visit[cur_x][left_y] == False and mat[cur_x][left_y] == 1:
            Q.append((cur_x, left_y))
        if visit[cur_x][right_y] == False and mat[cur_x][right_y] == 1:
            Q.append((cur_x, right_y))
        if visit[up_x][cur_y] == False and mat[up_x][cur_y] == 1:
            Q.append((up_x, cur_y))
        if visit[down_x][cur_y] == False and mat[down_x][cur_y] == 1:
            Q.append((down_x, cur_y))
            
    return visit, mat

__ = int(input())

for _ in range(__):
    M, N, K = map(int, input().split(' '))
    
    visit = [[False]*M for i in range(N)]
    matrix = [[0]*M for i in range(N)]
    matrix = assign_matrix(matrix, K)
    # print("MAT")
    # print(matrix)
    
    ans = 0
    
    for m in range(M):
        for n in range(N):

            # DFS 시작점
            if visit[n][m] == False and matrix[n][m] == 1:
                ans += 1
                Q = deque([(n,m)])
                visit, matrix = DFS(visit, matrix, n, m, Q, N, M)
            else:
                continue
    print(ans)