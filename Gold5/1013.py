tree = [[1,2],[-1,0],[3,-1],[4,-1],[4,5],[1,6],[7,6],[4,0]]

n = input()

for _ in range(0,int(n)):
    pattern = input()
    state = 0
    flag = True

    for idx in range(0,len(pattern)):
        # print('state : ' + str(state))
        # print('target : ' + pattern[idx])
        state = tree[state][int(pattern[idx])]
        # print('next_state : ' + str(state))
        if(state == -1):
            flag = False
            break
        
    if(flag and state != 0 and state != 5 and state != 6):
        flag = False
        
    if flag:
        print('YES')
    else:
        print('NO')