def fastbit_radix_like_sort(arr):
    max_num = max(arr)
    max_nibbles = (max_num.bit_length() + 3) // 4  

    buckets = {i: [] for i in range(16)}
    sorted_arr = arr[:]
    
    for nibble_pos in range(max_nibbles):
       
        for i in range(16):
            buckets[i] = []

        for num in sorted_arr:
            nibble = (num >> (4 * nibble_pos)) & 0xF  
            buckets[nibble].append(num)

        index = 0
        for i in range(16):
            for num in buckets[i]:
                sorted_arr[index] = num
                index += 1

    return sorted_arr