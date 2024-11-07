import numpy as np

def fastbit_radix_sort(arr):

    max_num = max(arr)
    num_bits = int(max_num).bit_length()  

    output = np.zeros(len(arr), dtype=int)

    for i in range(0, num_bits, 8):  

        mask = (1 << 8) - 1  

        count = [0] * 256  

        for num in arr:
            count[(num >> i) & mask] += 1
        
        for j in range(1, 256):
            count[j] += count[j - 1]

        for num in reversed(arr): 
            output[count[(num >> i) & mask] - 1] = num
            count[(num >> i) & mask] -= 1

        arr[:] = output

    return arr