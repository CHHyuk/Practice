# 예외(에러)의 이름을 모를 경우

try:
    list = []
    print(list[0])

    text = 'abc'
    number = int(text)
except Exception as ex:
    print('에러가 발생했습니다.',ex)