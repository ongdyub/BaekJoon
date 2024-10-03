from collections import deque

S = input()
T = input()
words = set()
# init
Q = deque()
Q.append(T)
words.add(T)

while True:
    new = Q.popleft()
    
    if len(new) <= len(S):
        print(0)
        break
    
    if new[-1] == 'A':
        new_A = new[:-1]
        if new_A == S:
            print(1)
            break
        else:
            if new_A not in words:
                Q.append(new_A)
                words.add(new_A)
    
    if new[-1] == 'B':
        new_B = new[:-1]
        new_B = new_B[::-1]
        if new_B == S:
            print(1)
            break
        else:
            if new_B not in words:
                Q.append(new_B)
                words.add(new_B)
