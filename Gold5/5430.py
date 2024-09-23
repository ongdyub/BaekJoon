import ast

T = int(input())

for _ in range(T):
    cmd = input()
    length = int(input())
    list_output = ast.literal_eval(input())
    
    reverse = False
    left = 0
    right = 0
    
    for c in cmd:
        if c == 'D':
            if reverse:
                right += 1
            else:
                left += 1
        elif c == 'R':
            reverse = not reverse
    # print(reverse)
    # print(left)
    # print(right)
    if left + right > length:
        print('error')
    else:
        if reverse:
            if not right:
                ans = list_output[left:]
            else:
                ans = list_output[left:-right]
            
            ans.reverse()
            string_output = '[' + ','.join(map(str, ans)) + ']'
            print(string_output)
        else:
            if not right:
                ans = list_output[left:]
            else:
                ans = list_output[left:-right]
            string_output = '[' + ','.join(map(str, ans)) + ']'
            print(string_output)
        