"""
list = []
list[0]   index 오류, list에 값이 없으므로

text = 'abc'
number = int(text)   value 오류, 문자와 정수
"""

text = '100%'
try:
    number = int(text) # 트라이 함수가 성립하는지 시도
except ValueError:
    print("{}는 숫자가 아니네요.".format(text)) # 오류가 생긴다면 실행
