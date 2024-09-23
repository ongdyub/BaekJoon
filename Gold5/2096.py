N = int(input())
score = []
for i in range(N):
    score.append(list(map(int, input().split(' '))))
    
left = score[0][0]
cent = score[0][1]
rigt = score[0][2]

mleft = score[0][0]
mcent = score[0][1]
mrigt = score[0][2]

for i in range(1,N):
    nxt_left = max(left, cent) + score[i][0]
    nxt_cent = max(left, cent, rigt) + score[i][1]
    nxt_rigt = max(cent, rigt) + score[i][2]
    
    left = nxt_left
    cent = nxt_cent
    rigt = nxt_rigt
    
    nxt_mleft = min(mleft, mcent) + score[i][0]
    nxt_mcent = min(mleft, mcent, mrigt) + score[i][1]
    nxt_mrigt = min(mcent, mrigt) + score[i][2]
    
    mleft = nxt_mleft
    mcent = nxt_mcent
    mrigt = nxt_mrigt
    
print(f'{max(left, cent, rigt)} {min(mleft, mcent, mrigt)}')