class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def prepend(self, data):
        new_node = DNode(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.size += 1

    def pop_left(self):
        if self.head is None:
            raise IndexError("pop from empty list")
        data = self.head.data
        if self.head.next is None:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        self.size -= 1
        return data

    def to_list(self):
        result = []
        cur = self.head
        while cur is not None:
            result.append(cur.data)
            cur = cur.next
        return result


class StackDLL:
    def __init__(self):
        self.dll = DoublyLinkedList()

    def push(self, item):
        self.dll.prepend(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError("pop from empty stack")
        return self.dll.pop_left()

    def top(self):
        if self.isEmpty():
            raise IndexError("top from empty stack")
        return self.dll.head.data

    def size(self):
        return self.dll.size

    def isEmpty(self):
        return self.dll.size == 0

    def printstack(self):
        print(self.dll.to_list())


def main():
    st = StackDLL()
    for x in [10, 20, 30]:
        st.push(x)

    print("Стек:")
    st.printstack()
    print("top():", st.top())
    print("size():", st.size())
    print("pop():", st.pop())
    print("После pop:")
    st.printstack()
    print("isEmpty():", st.isEmpty())


main()