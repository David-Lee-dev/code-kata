# 1918
# https://www.acmicpc.net/problem/1918

tc = list(input())[::-1]

operator_stk = []

result = [''] * len(tc)
idx = 0
while tc:
    word = tc.pop()

    if word == '(':
        operator_stk.append('(')
    elif word == ')':
        while operator_stk[-1] != '(':
            result[idx] = operator_stk.pop()
            idx += 1
        operator_stk.pop()
    elif word in ['+', '-']:
        while operator_stk and operator_stk[-1] != '(':
            result[idx] = operator_stk.pop()
            idx += 1
        operator_stk.append(word)
    elif word in ['*', '/']:
        while operator_stk and operator_stk[-1] in ['*', '/']:
            result[idx] = operator_stk.pop()
            idx += 1
        operator_stk.append(word)
    else:
        result[idx] = word
        idx +=1
else:
    for operator in operator_stk[::-1]:
        result[idx] = operator
        idx += 1


print(''.join(result))