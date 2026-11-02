class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = SNode(data)
        if self.head is None:
            self.head = new_node
            return
        cur = self.head
        while cur.next is not None:
            cur = cur.next
        cur.next = new_node

    def search(self, value):
        cur = self.head
        while cur is not None:
            if cur.data == value:
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
    sll = SinglyLinkedList()
    for x in [10, 20, 30, 40]:
        sll.append(x)

    print("Список:", sll.to_list())
    try:
        value = int(input("поиск: "))
    except EOFError:
        value = 20

    print(sll.search(value))


main()