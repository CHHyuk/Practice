a = 10
if a < 0 and 2**a > 1000 and a % 5 == 2 and round(a) == a:
    print('복잡한 식')

def return_false():
    print('함수return_false')
    return False

def return_true():
    print('함수return_true')
    return True

print('테스트1')
a = return_false()
b = return_true()

if a and b:
    print(True)
else:
    print(False)

print('테스트2')
if return_false() and return_true(): # 파이썬에선 and 연산에서 첫 값이 false면 and 뒤는 아예 안봄, 단락평가
    print(True)
else:
    print(False)