class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:  # 링크드리스트가 노드가 하나도 없는 상태면
            self.head = Node(data)  # 새 노드를 head에 연결
            return
        current = self.head
        while current.link:
            current = current.link  # 다음노드로 이동
        current.link = Node(data)


ll = LinkedList()
ll.append(8)
ll.append(10)
ll.append(-9)

