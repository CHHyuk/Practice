
def add_10(value):
    if value < 10:
        return 10 # return 나오면 함수를 바로 끝내버림
    
    result = value + 10
    return result

n = add_10(3)
print(n)
n = add_10(42)
print(n)

n = round(1.5)
print(n)