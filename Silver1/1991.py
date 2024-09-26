from collections import deque

N = int(input())

Tree = dict()
front = ''
mid = ''
back = ''
for _ in range(N):
    root, left, right = input().split(' ')
    Tree[root] = [left, right]
    
# 전위

Q = deque()
Q.append("A")
visit = set()

while len(Q) > 0:
    cur = Q.popleft()
    visit.add(cur)
    front += cur
    left = Tree[cur][0]
    right = Tree[cur][1]
    
    if right not in visit and right != '.':
        Q.appendleft(right)
        visit.add(right)
    
    if left not in visit and left != '.':
        Q.appendleft(left)
        visit.add(left)

print(front)

def mid_order(cur):
    global mid
    
    left = Tree[cur][0]
    right = Tree[cur][1]
    
    if left == '.' and right == '.':
        mid += cur
        return
    
    if left != '.':
        mid_order(left)
    mid += cur
    
    if right != '.':
        mid_order(right)
    return

mid_order("A")
print(mid)

# 후위
def back_order(cur):
    global back
    
    left = Tree[cur][0]
    right = Tree[cur][1]
    
    if left == '.' and right == '.':
        back += cur
        return
    
    if left != '.':
        back_order(left)
    
    if right != '.':
        back_order(right)
        
    back += cur
    return

back_order("A")
print(back)

