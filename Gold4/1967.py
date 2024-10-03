from collections import deque

N = int(input())

Tree = dict()
C_Tree = dict()

# parent = [0] * (N+1)

first = [0] * (N+1)

for _ in range(N-1):
    root, child, value = map(int, input().split(' '))
    
    if root not in Tree:
        Tree[root] = []
    Tree[root].append((child, root, value))
    
    if child not in C_Tree:
        C_Tree[child] = []
    C_Tree[child].append((root, child, value))
    
Q = deque()

Q.append(1)

while Q:
    root = Q.popleft()
    if root not in Tree:
        continue
    for edge in Tree[root]:
        child, root, value = edge
        
        first[child] = first[root] + value
        Q.append(child)

first_max_idx = first.index(max(first))

second = [0] * (N+1)
visit = [False] * (N+1)
Q = deque()

Q.append(first_max_idx)

while Q:
    cur = Q.popleft()
    # print(cur)
    visit[cur] = True
    
    # 애매
    if cur in C_Tree:
        for edge in C_Tree[cur]:
            root, child, value = edge
        
            if not visit[root]:
                # print("IN")
                # print(root)
                Q.append(root)
                visit[root] = True
                second[root] = second[child] + value
    
    
    if cur in Tree:
        for edge in Tree[cur]:
            child, root, value = edge
            
            if not visit[child]:
                # print("IIIIn")
                # print(child)
                visit[child] = True
                second[child] = second[root] + value
                Q.append(child)

print(max(second))