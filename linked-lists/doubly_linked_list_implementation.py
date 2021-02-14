class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def prepend(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node

        self.length += 1

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node

        self.length += 1

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return

        if index >= self.length:
            self.append(value)
            return

        node = Node(value)
        previous = self.traverse_to_node(index)
        follower = previous.next

        node.prev = previous
        node.next = follower
        follower.prev = node
        previous.next = node

        self.length += 1

    def remove(self, index):
        previous = self.traverse_to_node(index)
        previous.next = previous.next.next
        previous.next.next.prev = previous

        self.length -= 1

    def traverse_to_node(self, index):
        i = 0
        node = self.head

        while i != index - 1:
            node = node.next

        return node
