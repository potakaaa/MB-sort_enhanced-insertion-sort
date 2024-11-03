import random

def enhanced_insertion(arr):
    p1 = 1
    p2 = 2
    for i in range(1, len(arr) - 1):
        pass
def binary_search(arr, val, start, end):
     
    if start == end:
        if arr[start] > val:
            return start
        else:
            return start+1

    if start > end:
        return start
 
    mid = (start+end)//2
    if arr[mid] < val:
        return binary_search(arr, val, mid+1, end)
    elif arr[mid] > val:
        return binary_search(arr, val, start, mid-1)
    else:
        return mid
    

def enhanced_insertion2(arr):
    n = len(arr) 
    #half = n // 2
    if n <= 1:
        return arr  # If the array has 0 or 1 element, it is already sorted

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        pos = binary_search(arr, key, 0, j)

        # Shift elements and insert
        arr = arr[:pos] + [key] + arr[pos:i] + arr[i+1:]

    return arr
        



# list = [2, 1, 3, 4, 2, 3, 2] 
# binary_search returns 0

# Test the function

arr = list(range(1, 7))
random.shuffle(arr)
print("Unsorted array:", arr)

sorted_arr = enhanced_insertion2(arr.copy())

print("Sorted array:", sorted_arr)

print(sorted_arr == sorted(arr))


#print(binary_search(arr, 3, 0, 4))