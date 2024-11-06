from binary_search import binary_search



def enhanced_insertion2(arr):
    n = len(arr)
    if n <= 1:
        return
    
    min_index, i = 0, 1
    
    while i < n:
        key, j = arr[i], i - 1

        if key <= arr[min_index]:
            arr.insert(min_index, arr.pop(i))

        elif key >= arr[j]:
            arr.insert(j + 1, arr.pop(i))
        
        elif key < arr[j]:
            pos = binary_search(arr[:i], key)
            arr.insert(pos, arr.pop(i))

        i += 1

    return arr
    