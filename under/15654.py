N, M = map(int, input().split(' '))

seq = list(map(int, input().split(' ')))
seq.sort()

ocur = set()
cnt_dict = dict()

for s in seq:
    if str(s) in cnt_dict:
        cnt_dict[str(s)] += 1
    else:
        cnt_dict[str(s)] = 1

# print(cnt_dict)

def recur(depth, ans, end):
    global ocur, cnt_dict
    
    if depth == end:
        if ' '.join(ans) not in ocur:
            print(' '.join(ans))
            ocur.add(' '.join(ans))            
        return
    
    for i in range(N):
        if cnt_dict[str(seq[i])]:
            ans.append(str(seq[i]))
            cnt_dict[str(seq[i])] -= 1
            result = recur(depth+1, ans, end)
            ans.pop()
            cnt_dict[str(seq[i])] += 1
        else:
            continue
        
        
_ = recur(1, [], M+1)