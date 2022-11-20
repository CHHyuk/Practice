# 괄호 회전하기 XXXXXXXXXXXX

def check(s):
    b = 0
    if s[0] == '}' or  s[0] == ')' or  s[0] == ']':
        b += 1
    for i in range(1,len(s)):
        if s[i-1] == '[' and s[i] != ']':
            b += 1
        if s[i-1] == '{' and s[i] != '}':
            b += 1
        if s[i-1] == '(' and s[i] != ')':
            b += 1
    if b == 0:
        return True
    else:
        return False

def solution(s):
    result = 0
    a = 0
    while len(s) != a:
        if check(s):
            result += 1
        list_s = list(s)
        x = list_s.pop()
        list_s.insert(0,x)
        s = ''.join(list_s)
        a += 1
    
    return result


solution("[](){}")
