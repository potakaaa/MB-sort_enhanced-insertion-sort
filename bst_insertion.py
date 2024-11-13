from sortedcontainers import SortedList  # An alternative to a manual BST implementation

def enhanced_insertion_bst(arr):
    n = len(arr)
    if n <= 1:
        return arr
    
    sorted_list = SortedList(arr[:1])  # Initialize with the first element

    for i in range(1, n):
        key = arr[i]
        
        # Find the insertion position and insert
        pos = sorted_list.bisect_left(key)
        sorted_list.add(key)
        
        # Update arr to match sorted_list order
        arr[i] = sorted_list[i]

    return list(sorted_list)