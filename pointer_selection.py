import time


def enhanced_selection(arr):
    start_time = time.time()
    n = len(arr)
    
    for i in range(n//2):
        last = n - 1 - i
        min_idx = i 
        max_idx = i
        
        #print(arr)

        for j in range(i+1, n//2 + 1):
            p1 = j
            p2 = n - j
            #print("i = ", i, "j = ", j)
            if arr[p1] < arr[min_idx] or arr[p2] < arr[min_idx]:
                if arr[p1] < arr[min_idx]:
                    min_idx = p1
                    #print("p1 at ", p1," found Min Index: ", min_idx, " with value ", arr[min_idx])
                    #print("p1 at ", p1," found Min Index: ", min_idx, " with value ", arr[min_idx])
                if arr[p2] < arr[min_idx]:
                    min_idx = p2
                    #print("p2 at ", p2," found Min Index: ", min_idx, " with value ", arr[min_idx])

            if arr[p1] > arr[max_idx] or arr[p2] > arr[max_idx]:
                if arr[p1] > arr[max_idx]:
                    max_idx = p1
                    #print("p1 at ", p1, " found Max Index: ", max_idx, " with value ", arr[max_idx])

                if arr[p2] > arr[max_idx]:
                    max_idx = p2
                    #print("p2 at ", p2," found Max Index: ", max_idx, " with value ", arr[max_idx])
            #print("p1: ", p1, ", p2: ", p2)

            #print("Minimum Index: ", min_idx, ", Maximum Index: ", max_idx)
        if min_idx != i:
            #print("swapping index ", min_idx, " = ", arr[min_idx], " with index ", i, " = ", arr[i])
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            if max_idx == i:
                max_idx = min_idx

        if max_idx != last:
            #print("swapping index ", max_idx, " = ", arr[max_idx], " with index ", last, " = ", arr[last])
            arr[last], arr[max_idx] = arr[max_idx], arr[last]
        #print(arr)

    runtime = time.time() - start_time
    print(f"--- Enhanced Selection runtime: {runtime} seconds ---")

    return arr, runtime

