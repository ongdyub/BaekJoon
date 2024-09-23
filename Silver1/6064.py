
T = int(input())

for _ in range(T):
    M, N, x, y = map(int, input().split(' '))
    ans = -1
    
    if x > M or y > N:
        print(-1)
        continue
    
    while x <= M*N or y <= M*N:
        if x > y:
            y += N
        elif x < y:
            x += M
        else:
            ans = x
            break
    
    print(ans)