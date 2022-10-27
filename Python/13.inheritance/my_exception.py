from unexpectedRSPValue import UnexpectedRSPValue

value = '가'
try:
    if value not in ['가위','바위','보']:
        raise UnexpectedRSPValue
except UnexpectedRSPValue:
    print('에러가 발생했습니다')