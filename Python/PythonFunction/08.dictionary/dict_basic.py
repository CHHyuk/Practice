
wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
}
print(wintable['가위'])

def rsp(mine,yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else:
        return 'lose'

result = rsp('가위','바위')


messages = {   # Dictionary, 여러 값을 저장해두고 필요한 값을 꺼내 쓰는 기능
    'win' : '이겼다!',
    'draw' : '비겼다',
    'lose' : '졌다'
}

print(messages[result])


"""
words = ['a','b','c']
print(words[1])
"""