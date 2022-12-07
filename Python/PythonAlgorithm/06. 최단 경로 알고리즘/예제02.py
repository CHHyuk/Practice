# 미래 도시
"""
미래 도시에는 1번부터 N번까지의 회사가 있다 특정 회사끼리는 서로 도로를 통해 연결되어 있다
방문 판매원 A는 현재 1번 회사에 위치해 있으며 X번 회사에 방문해 물건을 판매하고자 한다

미래 도시에서 특정 회사에 도착하기 위해서는 회사끼리 연결된 도로를 이용하는 방법이 유일하다

또한 A는 소개팅에도 참석하고자 한다 소개팅의 상대는 K번 회사에 존재한다
따라서 A는 X번 회사에 가서 물건을 판매하기 전에 K회사를 방문할 예정이다

방문 판매원이 회사 사이를 이동하게 되는 최소 시간을 계산하는 프로그램을 작성하시오
"""

# 입출력 예시
"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
----------
3
"""


INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정

# 노드의 개수, 간선의 개수를 입력 받기
n, m = map(int,input().split())
# 2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF] * (n - 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] == 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # A와 B가 서로에게 가는 비용은 1이라고 설정
    a, b = map(int,input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# 거쳐 갈 노드 x와 최종 목적지 노드 k를 입력 받기
x, k = map(int,input().split())

# 점화식에 따라 플로이드 워셜 알고리즘을 수행

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for a in range(1 , n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k], graph[k][b])

# 수행된 결과를 출력 
distance = graph[1][k] + graph[k][x]

# 도달할 수 없는 경우 -1 출력
if distance >= INF:
    print('-1')
# 도달할 수 있다면 최단 거리를 출력
else:
    print(distance)