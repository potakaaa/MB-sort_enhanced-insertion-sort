from binary_search import binary_search

def enhanced_insertion(arr):
    n = len(arr)
    if n <= 1:
        return
    
    i = 1
    
    while i < n:
        key, j = arr[i], i - 1

        if key <= arr[0]:
            arr.insert(0, arr.pop(i))
            #arr = [key] + arr[:i] + arr[i+1:] 
        
        elif key < arr[j]:
            pos = binary_search(arr[:i], key)
            arr.insert(pos, arr.pop(i))
            #arr = arr[:pos] + [key] + arr[pos+1:i] + arr[i+1:]

        i += 1

    return arr