class SNode:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):
        new_node = SNode(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new_node
        self.size += 1

    def insert_at(self, index, data):
        new_node = SNode(data)
        if index <= 0 or self.head is None:
            new_node.next = self.head
            self.head = new_node
            self.size += 1
            return
        cur = self.head
        i = 0
        while cur.next is not None and i < index - 1:
            cur = cur.next
            i += 1
        new_node.next = cur.next
        cur.next = new_node
        self.size += 1

    def delete_by_value(self, value):
        prev = None
        cur = self.head
        while cur is not None:
            if cur.data == value:
                if prev is None:
                    self.head = cur.next
                else:
                    prev.next = cur.next
                self.size -= 1
                return True
            prev = cur
            cur = cur.next
        return False

    def to_list(self):
        result = []
        cur = self.head
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return result

    def print_list(self):
        print(self.to_list())

    def ai_minus_last(self, include_last=True):
        values = self.to_list()
        if not values:
            return []
        last = values[-1]
        if include_last:
            return [x - last for x in values]
        return [x - last for x in values[:-1]]


def main():
    sll = SinglyLinkedList()
    for x in [10, 20, 30, 40, 50]:
        sll.append(x)

    sll.insert_at(2, 25)
    print("После вставки 25 в позицию 2:")
    sll.print_list()

    sll.delete_by_value(20)
    print("После удаления 20:")
    sll.print_list()

    print("Последовательность ai - an:")
    print(sll.ai_minus_last())


main()