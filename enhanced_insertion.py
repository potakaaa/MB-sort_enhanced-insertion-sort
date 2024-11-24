from binary_search import binary_search

def enhanced_insertion(arr):
    n = len(arr)
    if n <= 1:
        return
    
    for i in range(1, n):
        key, j = arr[i], i - 1

        while key < arr[j]:
            if key <= arr[0]:
                arr.insert(0, arr.pop(i))
                break
        
            elif key < arr[j]:
                pos = binary_search(arr[:i], key)
                arr.insert(pos, arr.pop(i))
                break

    return arr