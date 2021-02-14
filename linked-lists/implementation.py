class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.value)
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def append(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def prepend(self, value):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            node.next = self.head
            self.head = node

        self.length += 1

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
            return

        if index >= self.length:
            self.append(value)
            return

        node = Node(value)

        current_node = self.head
        i = 0

        while current_node is not None:
            if i == index - 1:
                node.next = current_node.next
                current_node.next = node
                self.length += 1
                return

            current_node = current_node.next

            i += 1

    def remove(self, index):
        # check parameters
        current_node = self.head
        i = 0

        while current_node is not None:
            if i == index - 1:
                print(current_node.value, i)
                current_node.next = current_node.next.next
                self.length -= 1
                return

            i += 1

            current_node = current_node.next

    def reverse(self):
        if not self.head.next:
            return self.head

        left = self.head
        self.tail = left
        right = self.head.next

        while right:
            temp = right.next
            right.next = left
            left = right
            right = temp

        self.head.next = None
        self.head = left


llist = LinkedList()

llist.append(1)
llist.append(2)
llist.append(3)
llist.insert(0, 10)
llist.insert(5, 20)
llist.insert(3, 2.5)
llist.insert(4, 111)
llist.remove(3)
llist.prepend(100)
llist.prepend(101)
llist.reverse()
a = 1
