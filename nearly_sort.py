import random

def nearly_sort(arr, disorder_factor=0.1):
    """
    Takes an existing array and nearly sorts it by introducing a small amount of disorder.

    Parameters:
    - arr (list): The array to be nearly sorted.
    - disorder_factor (float): The fraction of elements to swap, controlling the disorder level.

    Returns:
    - list: A nearly sorted version of the original array.
    """
    # Copy the original array to avoid modifying it in-place
    arr = sorted(arr)
    
    # Calculate the number of swaps based on the disorder factor
    size = len(arr)
    num_swaps = int(size * disorder_factor)
    
    # Perform the swaps to introduce disorder
    for _ in range(num_swaps):
        i, j = random.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr
