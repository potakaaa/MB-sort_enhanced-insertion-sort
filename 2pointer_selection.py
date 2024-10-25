def enhanced_selection(arr):
    
    p1 = 1
    p2 = len(arr) - 1

    temp_first = 1
    temp_last = len(arr) - 1
    # for even number of elements only
    for i in range(len(arr) // 2):
        min_idx = i
        max_idx = i
        minChange = False
        maxChange = False
        print(arr)

        for j in range(1, len(arr) // 2):
            print(p1)
            print(p2)
            if arr[p1] < arr[min_idx] or arr[p2] < arr[min_idx]:
                if arr[p1] < arr[min_idx]:
                    min_idx = p1
                    print("Min Index: ", min_idx)
                if arr[p2] < arr[min_idx]:
                    min_idx = p2
                    print("Min Index: ", min_idx)
                minChange = True
            if arr[p1] > arr[max_idx] or arr[p2] > arr[max_idx]:
                if arr[p1] > arr[max_idx]:
                    max_idx = p1
                    print("Max Index: ", max_idx)
                if arr[p2] > arr[max_idx]:
                    max_idx = p2
                    print("Max Index: ", max_idx)
                maxChange = True

            p1 += 1
            p2 -= 1
        

        if minChange:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if maxChange:
            arr[temp_last], arr[max_idx] = arr[max_idx], arr[temp_last]
        print(arr)
        
        temp_first += 1
        temp_last -= 1

        minChange = False
        maxChange = False

        p1 = 1
        p2 = len(arr) - 1
    
    return arr

        
        

        

arr1 = [2, 3, 1, 2, 4, 3]

print(enhanced_selection(arr1))


            