import random

def enhanced_insertion(arr):
<<<<<<< HEAD
    for i in range(1, len(arr)):
        first_pointer = arr[i]
        j = i - 1  

        # Move elements that are greater than first_pointer one position ahead
        while j >= 0 and arr[j] > first_pointer:
            arr[j + 1] = arr[j]
            j -= 1

        # Place first_pointer in its correct position
        arr[j + 1] = first_pointer

    return arr
            
=======
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
>>>>>>> a441bb40133133ce2692fd8af95cda708d811fe6
    

def enhanced_insertion2(arr):
    n = len(arr) 
    half = n // 2
    if n <= 1:
        return arr  # If the array has 0 or 1 element, it is already sorted

    # Sort the first half of the array using insertion with binary search
    for p1 in range(1, half + 1):
        val = arr[p1]
        j = binary_search(arr, val, 0, p1 - 1)
        # Shift elements and insert
        arr = arr[:j] + [val] + arr[j:p1] + arr[p1+1:]

    # Sort the second half of the array using insertion with binary search
    for p2 in range(half + 1, n):
        val = arr[p2]
        j = binary_search(arr, val, n // 2, p2 - 1)  # Adjust search to second half
        # Shift elements and insert
        arr = arr[:j] + [val] + arr[j:p2] + arr[p2+1:]


    result = []
    i, j = 0, n // 2
    while i < n // 2 and j < n:
        if arr[i] < arr[j]:
            result.append(arr[i])
            i += 1
        else:
            result.append(arr[j])
            j += 1

    result.extend(arr[i:n // 2])
    result.extend(arr[j:n])

    return result


# Test the function

arr = list(range(1, 101))
random.shuffle(arr)
print("Unsorted array:", arr)

sorted_arr = enhanced_insertion2(arr.copy())

print("Sorted array:", sorted_arr)

print(sorted_arr == sorted(arr))
