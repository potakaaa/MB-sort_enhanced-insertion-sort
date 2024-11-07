import random, time
from algo_testcases import test_algo
from normal_selection import selectionSort

n = 10000

arr1 = random.sample(range(1, 10001), n)
arr1_copy = arr1.copy()
arr2 = random.sample(range(1, 10001), n)
arr2_copy = arr2.copy()
arr3 = random.sample(range(1, 10001), n)
arr3_copy = arr3.copy()
arr4 = random.sample(range(1, 10001), n)
arr4_copy = arr4.copy()
arr5 = random.sample(range(1, 10001), n)
arr5_copy = arr5.copy()

def enhancedSelectionSort(arr):
    start_time = time.time()
    n = len(arr) // 2
    for i in range(n):
        min_idx = i
        max_idx = i
        last_elm = len(arr) - 1 - i

        for j in range(i+1, last_elm+1):
            if arr[j] < arr[min_idx]:
                min_idx = j
            if arr[j] > arr[max_idx]:
                max_idx = j


        arr[last_elm], arr[max_idx] = arr[max_idx], arr[last_elm]
        if min_idx == last_elm:
            min_idx = max_idx
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    print("--- %s seconds ---" % (time.time() - start_time))
    runtime = time.time() - start_time

    return arr, runtime

print("Enhanced Selection is faster" if enhancedSelectionSort(arr1_copy)[1] < selectionSort(arr1)[1] else "Enhanced Selection is not faster", end="\n\n")
print("Enhanced Selection is faster" if enhancedSelectionSort(arr2_copy)[1] < selectionSort(arr2)[1] else "Enhanced Selection is not faster", end="\n\n")
print("Enhanced Selection is faster" if enhancedSelectionSort(arr3_copy)[1] < selectionSort(arr3)[1] else "Enhanced Selection is not faster", end="\n\n")
print("Enhanced Selection is faster" if enhancedSelectionSort(arr4_copy)[1] < selectionSort(arr4)[1] else "Enhanced Selection is not faster", end="\n\n")
print("Enhanced Selection is faster" if enhancedSelectionSort(arr5_copy)[1] < selectionSort(arr5)[1] else "Enhanced Selection is not faster", end="\n\n")

'''
test_algo(selectionSort, "NORMAL SELECTION", arr1)
test_algo(enhancedSelectionSort, "ENHANCED SELECTION", arr1_copy)

test_algo(selectionSort, "NORMAL SELECTION", arr2)
test_algo(enhancedSelectionSort, "ENHANCED SELECTION", arr2_copy)

test_algo(selectionSort, "NORMAL SELECTION", arr3)
test_algo(enhancedSelectionSort, "ENHANCED SELECTION", arr3_copy)

test_algo(selectionSort, "NORMAL SELECTION", arr4)
test_algo(enhancedSelectionSort, "ENHANCED SELECTION", arr4_copy)

test_algo(selectionSort, "NORMAL SELECTION", arr5)
test_algo(enhancedSelectionSort, "ENHANCED SELECTION", arr5_copy)

'''