def enhanced_insertion(arr):
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
            
    

def enhanced_insertion2(arr):
    pass