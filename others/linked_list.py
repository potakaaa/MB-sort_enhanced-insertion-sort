import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def sizeOfLL(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def generate_random_list(self, range_start, range_end, num_elements):
        if num_elements <= 0:
            self.head = None
            return

        self.head = Node(random.randint(range_start, range_end))
        current = self.head

        for _ in range(1, num_elements):
            new_node = Node(random.randint(range_start, range_end))
            current.next = new_node
            current = new_node

    def get(self, index):
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            current = current.next
            count += 1
        raise IndexError("Index not present")

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1

        if current is None:
            raise IndexError("Index not present")

        new_node.next = current.next
        current.next = new_node

    def remove_at_index(self, index):
        if index == 0:
            if self.head:
                self.head = self.head.next
            return

        current = self.head
        count = 0
        while current and count < index - 1:
            current = current.next
            count += 1

        if current is None or current.next is None:
            raise IndexError("Index not present")

        current.next = current.next.next

    def find_insertion_index(self, target):
        current = self.head
        index = 0
        while current:
            if current.data >= target:
                return index
            current = current.next
            index += 1
        return index

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def to_list(self):
        """
        Converts the linked list to a regular Python list.
        """
        current = self.head
        result = []
        while current:
            result.append(current.data)
            current = current.next
        return result
    
    def generate_from_list(self, regular_list):
        self.head = None  # Clear the current linked list
        for value in reversed(regular_list):  # Reverse the list to maintain order
            self.insertAtIndex(value, 0)  # Insert at the beginning

def list_to_linked_list(arr):
    ll = LinkedList()
    ll.generate_from_list(arr)
    return ll



