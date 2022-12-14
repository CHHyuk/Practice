# 연결 리스트(Linked Lists)
"""
각 원소들을 링크(link)로 연결하여 관리하는 방법이다.
해당 방법을 이용하여 링크를 끊어 원소를 삭제하거나 그 위치에 다른 원소를 삽입할 수 있다.
이 동작은 선형 배열보다 빠른 시간안에 원소의 삽입 / 삭제 동작을 할 수 있어 많이 사용된다.

각 원소는 하나의 Node 단위로 관리되며, Data 와 다음 노드를 가르키는 Link(next)로 이루어져있다.
이 노드들이 모이면 연결리스트가 되며 연결리스트의 첫 Node를 Head, 맨 끝의 Node를 Tail 이라 한다.
Head, Tail, 연결리스트의 총 Node 갯수를 알아두면 연결리스트의 추상적 자료구조를 만들 수 있으며 관리에 용이하다. 
이는 연속한 위치에 존재하는 일반적인 배열과 가장 큰 차이점으로, 각 연결된 Node가 임의의 위치에 존재가 가능하다는 의미로 해석할 수 있다
"""

# 단방향 리스트의 특정 원소 참조 연산

class Node:
    def __init__(self, item):
        self.data = item # 노드에 아이템이라는 데이터가 있음
        self.next = None # 다음 노드는 없다는 뜻

class LinkedList:
    def __init__(self):

        # 연결 리스트의 Node 갯수
        self.nodeCount = 0

        # 만약 Node가 존재한다면 Node 클래스 값이 들어간다.
        # 즉, curr = self.head 와 같은 코드를 사용한 후
        # curr.data / curr.next 등으로 Node를 사용할 수 있다.
        self.head = None
        self.tail = None

    def getNode(LinkedList, want_index):

        # 아래 조건 중 하나라도 만족하면 Node Return
        # 만약 원하는 인덱스 번호가 0이하
        # 연결 리스트의 전체 Node 수 보다 클 때
        if want_index < 1 or want_index > LinkedList.nodeCount:
            return None
    
        # 시작 노드 인덱스를 1로 시작
        curr_index = 1

        # 첫 노드 부터 시작
        curr = LinkedList.head

        # 원하는 인덱스 값에 도달할 때 까지 Node 이동 작업
        while curr_index < want_index:

            # 다음 노드로 넘어감 (원하는 인덱스가 아니기 때문에 데이터 조회 X)
            curr = curr.next

            # 현재 인덱스 값 +1
            curr_index += 1
    
        return curr