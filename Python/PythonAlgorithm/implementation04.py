# 문자열 재정렬
"""
알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어진다
모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에,
그 뒤에 모든 숫자를 더한 값을 이어서 출력한다
예) K1KA5CB7 = ABCKK13
"""

s = input()
result = []
value = 0

# 문자를 하나씩 확인
for x in s:
    # 알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    # 숫자는 따로 더하기
    else:
        value += int(x)

# 알파벳 오름차순 정리
result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
if value != 0:
    result.append(str(value))

print(''.join(result))