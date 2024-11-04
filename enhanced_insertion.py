import random
from binary_search import binary_search

def enhanced_insertion3(arr):
    n = len(arr)
    if n <= 1:
        return
    
    i = 1
    min_index = 0
    
    while i < n:
        key = arr[i]
        j = i - 1

        if key <= arr[min_index]:
            #print("im inside here 1")
            arr.insert(min_index, arr.pop(i))
            #arr = [key] + [arr[min_index]] + arr[min_index + 1:i] + arr[i+1:]
            #print(f"I is {i}, arr is {arr}")
        
        elif key < arr[j]:
            #print("im inside here 2")
            pos = binary_search(arr[:i], key)
            # Shift elements and insert
            arr.insert(pos, arr.pop(i))
            #arr = arr[:pos] + [key] + arr[pos:i] + arr[i+1:]
            #print(f"I is {i}, arr is {arr}")

        i += 1

    return arr