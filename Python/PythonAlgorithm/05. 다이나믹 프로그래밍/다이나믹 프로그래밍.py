# 다이나믹 프로그래밍(동적 계획법)
"""
메모리를 적절히 사용하여 수행 시간 효율성을 비약적으로 향상시키는 방법
이미 계산된 결과(작은 문제)는 별도로 메모리 영역에 저장하여 다시 계산하지 않도록 한다
일반적으로 탑다운 방식과 바텀업 방식으로 구성됨
"""
"""
일반적인 프로그래밍 분야에서 동적(Dynamic)이란
    - 자료 구조에서 동적 할당(Dynamic Allocation)은 '프로그램이 실행되는 도중에 실행에 필요한 메모리를 할당하는 기법'을 의미
    - 다이나믹 프로그래밍에서의 '다이나믹'은 별다른 의미 없이 사용된 단어
"""
"""
다이나믹 프로그래밍은 문제가 다음 조건을 만족할 때 사용 가능
    1. 최적 부분 구조 (Optimal Substructure)
        큰 문제를 작은 문제로 나눌 수 있으며 작은 문제의 답을 모아 큰 문제 해결 가능
    2. 중복되는 부분 문제 (Overlapping Subproblem)
        동일한 작은 문제를 반복적으로 해결해야 함
"""