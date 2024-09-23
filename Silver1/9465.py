T = int(input())

for _ in range(T):
    n = int(input())
    up = list(map(int, input().split(' ')))
    down = list(map(int, input().split(' ')))
    
    state_0 = 0
    state_1 = up[0]
    state_2 = down[0]
    # print(f'{state_0} {state_1} {state_2}')
    for idx in range(1,n):
        nxt_0 = (max(state_1, state_2))
        nxt_1 = (max(state_0, state_2) + up[idx])
        nxt_2 = (max(state_1, state_0) + down[idx])
        state_0 = nxt_0
        state_1 = nxt_1
        state_2 = nxt_2
        # print(f'{state_0} {state_1} {state_2}')
    
    print(max(state_0, state_1, state_2))