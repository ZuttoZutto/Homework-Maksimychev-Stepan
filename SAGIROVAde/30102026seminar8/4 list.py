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

    def delete_value(self, value):
        cur = self.head
        while cur is not None:
            if cur.data == value:
                if cur.prev is None:
                    self.head = cur.next
                else:
                    cur.prev.next = cur.next
                if cur.next is None:
                    self.tail = cur.prev
                else:
                    cur.next.prev = cur.prev
                return True
            cur = cur.next
        return False

    def to_list(self):
        result = []
        cur = self.head
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return result


def main():
    dll = DoublyLinkedList()
    for x in [5, 10, 15, 20, 25]:
        dll.append(x)

    print("Список до удаления:", dll.to_list())
    try:
        value = int(input("Удаление: "))
    except EOFError:
        value = 15

    dll.delete_value(value)
    print("Список после удаления:", dll.to_list())


main()