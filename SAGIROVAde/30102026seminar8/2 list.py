class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = DNode(data)
        if self.tail is None:
            self.head = self.tail = new_node
            return
        new_node.prev = self.tail
        self.tail.next = new_node
        self.tail = new_node

    def print_reverse(self):
        result = []
        cur = self.tail
        while cur is not None:
            result.append(cur.data)
            cur = cur.prev
        print(result)


def main():
    dll = DoublyLinkedList()
    for x in [1, 2, 3, 4]:
        dll.append(x)
    dll.print_reverse()


main()