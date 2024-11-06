def binary_search(arr, target):
    """
    Finds the index where `target` should be inserted in the sorted array `arr`
    to maintain sorted order.

    :param arr: List of elements in sorted order.
    :param target: The element for which we need the insertion index.
    :return: The index where `target` should be inserted.
    """
    left, right = 0, len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        # Check if target should be on the left or right of mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left  # This is the correct insertion index for `target`

# Example usage:
'''sorted_arr = [1, 3, 5, 7, 9]
target = 6
index = binary_search(sorted_arr, target)
print(f"The insertion index for {target} is {index}.")  # Output: The insertion index for 6 is 3.
'''