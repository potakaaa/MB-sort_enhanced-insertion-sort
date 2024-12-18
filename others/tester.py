import random, time
from algo_testcases import test_algo_works
from normal_selection import selectionSort
from pointer_selection import enhanced_selection
from pointer_selection_merge import enhanced_selection_merge

arrn = [10, 2, 18, 36, 52, 68, 84, 100, 14, 28, 
        42, 58, 74, 90, 6, 20, 34, 48, 62, 76, 
        92, 8, 22, 36, 50, 64, 78, 94, 12, 26, 
        40, 54, 68, 82, 96, 16, 30, 44, 58, 72, 
        86, 100, 18, 32, 46, 60, 74]

n = 13

arr1 = random.choices(range(1, 1000), k = n)
arr1_copy = arr1.copy()
'''arr2 = random.sample(range(1, 102), n)
arr2_copy = arr2.copy()
arr3 = random.sample(range(1, 102), n)
arr3_copy = arr3.copy()
arr4 = random.sample(range(1, 102), n)
arr4_copy = arr4.copy()
arr5 = random.sample(range(1, 102), n)
arr5_copy = arr5.copy()'''

print("\n\n\n")

test_algo_works(enhanced_selection_merge, "Selection", arr1)
'''test_algo_works(enhanced_selection, "Selection", arr2)
test_algo_works(enhanced_selection, "Selection", arr3)
test_algo_works(enhanced_selection, "Selection", arr4)
test_algo_works(enhanced_selection, "Selection", arr5)'''

#test_algo_works(enhanced_selection, "Selection", [90, 71, 26, 34, 50, 78, 3, 29, 60, 57])

#normal_runtime = selectionSort(arr1)
#enhanced_runtime = enhanced_selection(arr1_copy)

#print(f"Enhanced Selection is faster" if enhanced_runtime < normal_runtime else "Enhanced Selection is not faster", end="\n\n")

#test_algo_works(enhanced_selection, "Selection", arr1)     