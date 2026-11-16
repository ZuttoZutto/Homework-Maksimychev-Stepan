class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._length = 0

    def __len__(self):
        return self._length

    def _get_node(self, index):
        if index < 0:
            index += self._length
        if index < 0 or index >= self._length:
            raise IndexError("Индекс вне диапазона")
        if index < self._length // 2:
            node = self.head
            for _ in range(index):
                node = node.next
        else:
            node = self.tail
            for _ in range(self._length - 1, index, -1):
                node = node.prev
        return node

    def __getitem__(self, index):
        return self._get_node(index).data

    def insert(self, index, data):
        if index < 0:
            index += self._length
        if index < 0:
            index = 0
        if index > self._length:
            index = self._length

        new_node = Node(data)

        if self._length == 0:
            self.head = self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        elif index == self._length:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            prev_node = self._get_node(index - 1)
            next_node = prev_node.next
            new_node.prev = prev_node
            new_node.next = next_node
            prev_node.next = new_node
            next_node.prev = new_node

        self._length += 1

    def append(self, data):
        self.insert(self._length, data)

    def __delitem__(self, index):
        node = self._get_node(index)

        if node.prev:
            node.prev.next = node.next
        else:
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev

        node.prev = node.next = None
        self._length -= 1

    def __repr__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.data))
            current = current.next
        return f"DoublyLinkedList([{', '.join(values)}])"