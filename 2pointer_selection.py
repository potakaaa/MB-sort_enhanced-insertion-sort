def enhanced_selection(arr):
    # for even number of elements only
    
    for i in range((len(arr) // 2)):
        last = len(arr) - 1 - i
        min_idx = i 
        max_idx = len(arr) - 1 - i
        
        print(arr)

        for j in range(i+1, (len(arr) // 2) + 1):
            p1 = j
            p2 = len(arr) - j
            print("i = ", i, "j = ", j)
            if arr[p1] < arr[min_idx] or arr[p2] < arr[min_idx]:
                if arr[p1] < arr[min_idx]:
                    min_idx = p1
                    print("p1 at ", p1," found Min Index: ", min_idx, " with value ", arr[min_idx])
                if arr[p2] < arr[min_idx]:
                    min_idx = p2
                    print("p2 at ", p2," found Min Index: ", min_idx, " with value ", arr[min_idx])

            if arr[p1] > arr[max_idx] or arr[p2] > arr[max_idx]:
                if arr[p1] > arr[max_idx]:
                    max_idx = p1
                    print("p1 at ", p1, " found Max Index: ", max_idx, " with value ", arr[max_idx])

                if arr[p2] > arr[max_idx]:
                    max_idx = p2
                    print("p2 at ", p2," found Max Index: ", max_idx, " with value ", arr[max_idx])
            print("p1: ", p1, ", p2: ", p2)

            print("Minimum Index: ", min_idx, ", Maximum Index: ", max_idx)
        print(arr)
        if min_idx != i:
            print("swapping index ", min_idx, " = ", arr[min_idx], " with index ", i, " = ", arr[i])
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            if max_idx == i:
                max_idx = min_idx

        if max_idx != last:
            print("swapping index ", max_idx, " = ", arr[max_idx], " with index ", last, " = ", arr[last])
            arr[last], arr[max_idx] = arr[max_idx], arr[last]
        print(arr)

    
    return arr

        
        

        

arr1 = [10, 2, 18, 36, 52, 68, 84, 100, 14, 28, 42, 58, 74, 90, 6, 20, 34, 48, 62, 76, 92, 8, 22, 36, 50, 64, 78, 94, 12, 26, 40, 54, 68, 82, 96, 16, 30, 44, 58, 72, 86, 100, 18, 32, 46, 60, 74]

print(enhanced_selection(arr1))


            