from binary_search import binary_search
from linked_list import LinkedList

def enhanced_insertion2(linked_list):
    n = linked_list.sizeOfLL()
    if n <= 1:
        return

    i = 1
    while i < n:
        key = linked_list.get(i)
        j = i - 1

        if key <= linked_list.get(0):
            linked_list.insertAtIndex(key, 0)
            linked_list.remove_at_index(i + 1)  # Remove the original position of `key`

        elif key < linked_list.get(j):
            pos = linked_list.find_insertion_index(key)
            linked_list.insertAtIndex(key, pos)
            linked_list.remove_at_index(i + 1)  # Remove the original position of `key`

        i += 1

    return linked_list


'''# Example usage:
ll = LinkedList()
ll.generate_random_list(1, 10, 10)

print(f"Original List: {ll.to_list()}")

enhanced_insertion2(ll)


print(f"Sorted List: {ll.to_list()}")'''

