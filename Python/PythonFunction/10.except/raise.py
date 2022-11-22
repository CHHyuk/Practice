# 에러를 직접 일으키는 방법

def rsp(mine,yours):
    allowed = ['가위','바위','보']
    if mine not in allowed:
        raise ValueError
    if yours not in allowed:
        raise ValueError
    # 가위바위보 승패를 판단하는 코드
try:
    rsp('가위','바')
except ValueError:
    print('잘못된 값을 넣은것 같습니다')
