def enhanced_selection(arr):
    # for even number of elements only
    for i in range((len(arr) // 2)):
        print("i = ", i)
        last = len(arr) - 1 - i
        min_idx = i
        max_idx = len(arr) - 1 - i
        p1 = 1
        p2 = last - 1
        print(arr)

        for j in range(i+1, len(arr) // 2):
            print("j = ", j)
            if arr[p1] < arr[min_idx] or arr[p2] < arr[min_idx]:
                if arr[p1] < arr[min_idx]:
                    min_idx = p1
                    print("p1 at ", p1," p1 found Min Index: ", min_idx, " with value ", arr[min_idx])
                if arr[p2] < arr[min_idx]:
                    min_idx = p2
                    print("p2 at ", p2," p2 found Min Index: ", min_idx, " with value ", arr[min_idx])

            if arr[p1] > arr[max_idx] or arr[p2] > arr[max_idx]:
                if arr[p1] > arr[max_idx]:
                    max_idx = p1
                    print("p1 at ", p1, " found Max Index: ", max_idx, " with value ", arr[max_idx])

                if arr[p2] > arr[max_idx]:
                    max_idx = p2
                    print("p2 at ", p2," p2 found Max Index: ", max_idx, " with value ", arr[max_idx])
            print("p1: ", p1, ", p2: ", p2)
            p1 += 1
            p2 -= 1
        
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            if max_idx == i:
                max_idx = min_idx
        if max_idx != last:
            arr[last], arr[max_idx] = arr[max_idx], arr[last]
        print(arr)
    
    return arr

        
        

        

arr1 = [2, 3, 1, 2, 4, 3, 0, 0]

print(enhanced_selection(arr1))


            