A, B, C = map(int, input().split(' '))
ans = 1

def mul(num, exp, C):
    global ans
    etc = exp % 2
    div = exp // 2
    # print(f'{exp} {div} {etc}')
    # if exp <= 2:
    #     # if etc:
    #     #     ans *= ((num**(exp+1))%C)
    #     #     return
    #     # else:
    #     #     ans *= (num**exp)%C
    #     #     return
    #     ans = (num**(div+etc))%C
    #     return
    if exp <= 1:
        # if etc:
        #     ans *= ((num**(exp+1))%C)
        #     return
        # else:
        #     ans *= (num**exp)%C
        #     return
        ans = num%C
        return
        
    else:
        mul(num, div, C)
        ans = ((ans**2) * (num**etc))%C
        return

mul(A,B,C)
print(ans)