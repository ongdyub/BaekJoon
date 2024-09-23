import heapq

T = int(input())

for _ in range(T):
    n_cmd = int(input())
    max_Q = []
    min_Q = []
    n_id = dict()
    add_cnt = 0
    
    for __ in range(n_cmd):
        cmd = input().split(' ')
        op, num = cmd[0], int(cmd[1])
        
        if op == 'I':
            heapq.heappush(max_Q, -num)
            heapq.heappush(min_Q, num)
            add_cnt += 1
            if num in n_id:
                n_id[num] += 1
            else:
                n_id[num] = 1
        elif num == 1:
            if add_cnt <= 0:
                continue
            
            max_num = heapq.heappop(max_Q)
            
            while not n_id[-max_num]:
                max_num = heapq.heappop(max_Q)
                
            n_id[-max_num] -= 1
            add_cnt -= 1
            
        else:
            if add_cnt <= 0:
                continue
            
            min_num = heapq.heappop(min_Q)
            
            while not n_id[min_num]:
                min_num = heapq.heappop(min_Q)
                
            n_id[min_num] -= 1
            add_cnt -= 1
        
        
        
    if add_cnt == 0:
        print("EMPTY")
    else:
        max_num = heapq.heappop(max_Q)
        
        while not n_id[-max_num]:
            max_num = heapq.heappop(max_Q)
            
        min_num = heapq.heappop(min_Q)
        
        while not n_id[min_num]:
            min_num = heapq.heappop(min_Q)
                
        print(f'{-max_num} {min_num}')
            
        
        