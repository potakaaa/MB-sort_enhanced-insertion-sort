import bisect

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        
        # Find the position to insert the key using binary search
        pos = bisect.bisect_left(arr, key, 0, i)
        
        # Shift elements to the right to make room for key
        arr.insert(pos, arr.pop(i))
    
    return arr