
N = int(input())

room = []

for _ in range(N):
    s, e = map(int, input().split(' '))
    room.append((s,e))
    
room = sorted(room, key=lambda x :(x[1], x[0]))

# print(room)
cnt = 0
s_l = -1
e_l = -1

for _ in range(N):
    if room[_][0] >= e_l:
        cnt += 1
        e_l = room[_][1]
        
print(cnt)