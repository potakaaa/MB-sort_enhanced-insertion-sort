import random
from binary_search import binary_search

def enhanced_insertion(arr):
    p1 = 1
    p2 = 2
    for i in range(1, len(arr) - 1):
        pass

def enhanced_insertion2(arr):
    n = len(arr) 
    if n <= 1:
        return # If the array has 0 or 1 element, it is already sorted

    min_index = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        if arr[i] <= arr[min_index]:
            arr = [arr[i]] + [arr[min_index]] + arr[min_index:i] + arr[i+1:]
            min_index = i
            print(f"I is {i}, arr is {arr}")

        else:
            pos = binary_search(arr[:i], key)
            # Shift elements and insert
            arr = arr[:pos] + [key] + arr[pos:i] + arr[i+1:]
            print(f"I is {i}, arr is {arr}")

    return arr
        



# list = [2, 2, 3, 1, 4, 2, 3, 2] 
# newlist = [1, 2, ]
# binary_search returns 0

# Test the function

arr = list(range(1, 8))
random.shuffle(arr)
print("Unsorted array:", arr)

sorted_arr = enhanced_insertion2(arr.copy())

print("Sorted array:", sorted_arr)

print(sorted_arr == sorted(arr))


#print(binary_search(arr, 3, 0, 4))