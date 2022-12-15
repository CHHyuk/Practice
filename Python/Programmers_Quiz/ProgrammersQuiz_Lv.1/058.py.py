# 문자열 나누기

def solution(s):
    temp = ''
    check = ''
    check_count = 0
    other_count = 0
    result = 0
    for i in range(len(s)):
        if temp == '':
            temp += s[i]
            check = s[i]
            check_count += 1
        elif temp[i] == check:
            check_count += 1
        elif temp[i] != check:
            other_count += 1
        if check_count == other_count:
            result += 1
            temp = ''
            check = ''
            check_count = 0
            other_count = 0
        if i == len(s) -1 and temp != '':
            result += 1
    return result
