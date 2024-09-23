# from collections import deque

# prompt = input()

# num_Q = deque()
# cal_Q = deque()

# s2n = ''

# for p in prompt:
#     try:
#         num = int(p)
#         if num == 0 and len(s2n) == 0:
#             pass
#         else:
#             s2n += p
#     except:
#         num_Q.append(int(s2n))
#         s2n = ''
#         cal_Q.append(p)
# num_Q.append(int(s2n))

# ans = num_Q.popleft()
# seg = 0
# seg_mode = False

# while len(cal_Q) > 0:
#     cal = cal_Q.popleft()
    
#     if cal == '-':
#         if seg_mode:
#             ans -= seg
            
#         else:
#             seg_mode = True
#             seg += num_Q.popleft()
#     else:
#         if seg_mode:
#             seg += num_Q.popleft()
#         else:
#             ans += num_Q.popleft()
        
# print(num_Q)
# print(cal_Q)
# print(ans-seg_mode)


from collections import deque

prompt = input()

num_Q = deque()
cal_Q = deque()

s2n = ''

for p in prompt:
    try:
        num = int(p)
        if num == 0 and len(s2n) == 0:
            pass
        else:
            s2n += p
    except:
        num_Q.append(int(s2n))
        s2n = ''
        cal_Q.append(p)
num_Q.append(int(s2n))

ans = num_Q.popleft()
minus = False


while len(cal_Q) > 0:
    cal = cal_Q.popleft()
    
    if minus == False and cal == '-':
        minus = True
        
    if minus:
        ans -= num_Q.popleft()
    else:
        ans += num_Q.popleft()
print(ans)