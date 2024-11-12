import random

def nearly_sorted(size, disorder_factor=0.1):
    """
    Generates a nearly sorted array with a given level of disorder.

    Parameters:
    - size (int): The number of elements in the array.
    - disorder_factor (float): The fraction of elements to swap, controlling the disorder level. 
                               (0.1 = 10% of elements swapped)

    Returns:
    - list: A nearly sorted array.
    """
    # Create a sorted array of the specified size
    arr = list(range(1, size + 1))
    
    # Calculate the number of swaps based on the disorder factor
    num_swaps = int(size * disorder_factor)
    
    # Perform the swaps to introduce disorder
    for _ in range(num_swaps):
        i, j = random.sample(range(size), 2)
        arr[i], arr[j] = arr[j], arr[i]
    
    return arr