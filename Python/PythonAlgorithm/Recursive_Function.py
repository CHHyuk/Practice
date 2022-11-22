# 재귀함수(Recursive Function)
"""
자기 자신을 다시 호출하는 함수
"""
def recursive_Function():
    print('재귀함수를 호출합니다')
    recursive_Function()

recursive_Function() # '재귀함수를 호출합니다' 가 계속 출력되다가 최대 재귀 깊이 초과 메시지 출력 (RecursionError)
