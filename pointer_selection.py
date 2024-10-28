import time


def enhanced_selection(arr):
    start_time = time.time()
    n = len(arr)
    swapped = False
    
    for i in range(n//2):
        last = n - 1 - i
        min_idx = i 
        max_idx = i
        
        #print(arr)

        for j in range(i+1, n//2 + 1):
            p1 = j
            p2 = n - j

            if arr[p1] < arr[min_idx]:
                min_idx = p1

            if arr[p2] < arr[min_idx]:
                min_idx = p2

            if arr[p1] > arr[max_idx]:
                max_idx = p1


            if arr[p2] > arr[max_idx]:
                max_idx = p2

        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swapped = True
            if max_idx == i:
                max_idx = min_idx

        if max_idx != last:
            arr[last], arr[max_idx] = arr[max_idx], arr[last]
            swapped = True
        
        if not swapped:
            runtime = time.time() - start_time
            print(f"--- Enhanced Selection runtime: {runtime} seconds ---")
            return arr, runtime

    runtime = time.time() - start_time
    print(f"--- Enhanced Selection runtime: {runtime} seconds ---")

    return arr, runtime

