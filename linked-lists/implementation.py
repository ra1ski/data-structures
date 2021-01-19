from typing import Any


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    head = None
    tail = None
    length = 0

    def get(self):
        pass

    def append(self, value: Any):
        node = Node(value)

        if self.head is None:
            self.head = node
            self.tail = self.head
        else:
            self.tail.next = node
            self.tail = node

        self.length += 1

    def prepend(self, value: Any):
        node = Node(value)
        node.next = self.head
        self.head = node

        self.length += 1

    def insert(self, index: int, value: Any):
        if index == 0:
            return self.prepend(value)

        if index >= self.length:
            return self.append(value)

        node = Node(value)
        current_node = self.traverse_to_index(index - 1)
        node.next = current_node.next
        current_node.next = node

        self.length += 1

    def delete(self, index):
        current_node = self.traverse_to_index(index - 1)
        current_node.next = current_node.next.next
        self.length -= 1

    def traverse_to_index(self, index: int):
        i = 0
        current_node = self.head

        while i != index - 1:
            current_node = current_node.next
            i += 1

        return current_node

    def print_list(self):
        values = []
        head = self.head

        while head:
            values.append(head.value)
            head = head.next

        print(values)

        return values


linked_list = LinkedList()
linked_list.print_list()
linked_list.append(10)
linked_list.print_list()
linked_list.append(20)
linked_list.print_list()
linked_list.append(30)
linked_list.print_list()
linked_list.prepend(90)
linked_list.prepend(100)
linked_list.insert(0, 110)
linked_list.insert(6, 40)
linked_list.print_list()
linked_list.insert(2, 95)
linked_list.print_list()
linked_list.delete(2)
linked_list.print_list()
