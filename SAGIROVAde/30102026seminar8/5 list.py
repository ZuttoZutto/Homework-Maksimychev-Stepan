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

    def to_list(self):
        result = []
        cur = self.head
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return result

    def paired_diffs_from_ends(self):
        values = self.to_list()
        n = len(values)
        result = []
        for i in range(n // 2):
            result.append(values[i] - values[n - 1 - i])
        if n % 2 == 1:
            result.append(0)
        return result


def main():
    dll = DoublyLinkedList()
    for x in [1, 2, 3, 4, 5, 6]:
        dll.append(x)

    print("Список:", dll.to_list())
    print("a1-an, a2-a_{n-1}, ...:", dll.paired_diffs_from_ends())


main()