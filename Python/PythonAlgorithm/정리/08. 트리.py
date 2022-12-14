# 트리(Trees)
"""
root 노드에서 간선(edge)들이 뿌리처럼 뻗어나가는 구조를 가진 형태이다.
"""

# 트리 관련 용어
"""
Node의 수준(Level)
    root 노드에서 간선을 하나씩 거칠 수록 레벨이 하나씩 증가한다. 
    root 노드가 0 일 경우 간선을 거칠 수록 Level 1, Level 2 ... 로 증가
Node의 높이(Height) or Node의 깊이(depth)
    Node의 높이 = Node의 최대 수준(Level) + 1
부분 트리(서브 트리)
    트리에서 특정 노드를 기준으로 가장 아래쪽 자식 노드까지를 묶어 부분 트리라고 한다.
Node의 차수(Degree)
    자식 Node 수를 나타내며, 이때 자식 트리가 없는  Node들을 leaf Node라고 한다.
"""