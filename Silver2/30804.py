N = int(input())

fruits = list(map(int, input().split(' ')))

cur_set = set()

if N == 1:
    print(1)
elif N == 2:
    print(2)
else:
    start_idx = 0
    end_idx = 1
    ans = 2
    cnt = 2
    cur_set.add(fruits[start_idx])
    cur_set.add(fruits[end_idx])
    
    while end_idx < N-1:
        end_idx += 1
        
        if len(cur_set) == 2:
            if fruits[end_idx] in cur_set:
                cnt += 1
            else:
                if cnt > ans:
                    ans = cnt

                cur_set.add(fruits[end_idx])
                target_idx = fruits[end_idx-1]
                start_idx = end_idx - 1
                
                while fruits[start_idx] == target_idx:
                    start_idx -= 1
                    
                cur_set.remove(fruits[start_idx])
                start_idx += 1
                
                cnt = (end_idx - start_idx + 1)
                
        else:
            cnt += 1
            
            cur_set.add(fruits[end_idx])
            
    if cnt > ans:
        print(cnt)
    else:
        print(ans)
    