from pointer_selection import enhanced_selection

def enhanced_selection_merge(arr):
    n = len(arr)

    mid = n // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = enhanced_selection(left_half)
    right_sorted = enhanced_selection(right_half)
    sorted_arr = []
    i, j = 0, 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] < right_sorted[j]:
            sorted_arr.append(left_sorted[i])
            i += 1
        else:
            sorted_arr.append(right_sorted[j])
            j += 1

    sorted_arr.extend(left_sorted[i:])
    sorted_arr.extend(right_sorted[j:])

    return sorted_arr

