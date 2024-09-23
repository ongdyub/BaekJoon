
N = int(input())

S = int(input())

cmd = input()

target = ('IO'*N + 'I')
t_len = 2*N + 1

ans = 0

s_pointer = 0
t_pointer = 0

while s_pointer < S:
    if target[t_pointer] == cmd[s_pointer]:
        t_pointer += 1
        s_pointer += 1
    else:
        if cmd[s_pointer] == 'I':
            t_pointer = 0
            continue
        else:
            s_pointer += 1
            t_pointer = 0
            continue
        
    if t_pointer == t_len:
        ans += 1
        t_pointer -= 2
        # s_pointer -= 1
    
    

        
print(ans)