from timeit import timeit
import random

n = 5000

arr1 = random.choices(range(1, 1000), k = n)
arr1_copy = arr1.copy()
arr1_copy2 = arr1.copy()
arr1_copy3 = arr1.copy()
arr1_copy4 = arr1.copy()
arr1_copy5 = arr1.copy()
arr1_copy6 = arr1.copy()
arr1_copy7 = arr1.copy()
arr1_copy8 = arr1.copy()
arr1_copy9 = arr1.copy()
arr1_copy10 = arr1.copy()

t1 = timeit(
    "selectionSort(arr1)",
    setup="from normal_selection import selectionSort",
    number = 10,
    globals={"arr1":arr1},
)

t2 = timeit(
    "enhanced_selection(arr1_copy)",
    setup="from pointer_selection import enhanced_selection",
    number = 10,
    globals={"arr1_copy":arr1_copy},
)

t3 = timeit(
    "enhanced_selection_merge(arr1_copy2)",
    setup="from pointer_selection_merge import enhanced_selection_merge",
    number = 10,
    globals={"arr1_copy2":arr1_copy2},
)

t4 = timeit(
    "enhanced_insertion(arr1_copy3)",
    setup="from enhanced_insertion import enhanced_insertion",
    number = 10,
    globals={"arr1_copy3":arr1_copy3},
)

'''t5 = timeit(
    "enhanced_insertion2(arr1_copy4)",
    setup="from enhanced_insertion_mid import enhanced_insertion2",
    number = 10,
    globals={"arr1_copy4":arr1_copy4},
)'''

t6 = timeit(
    "sorted(arr1_copy5)",
    number = 10,
    globals={"arr1_copy5":arr1_copy5},
)

t7 = timeit(
    "insertionSort(arr1_copy6)",
    setup="from insertion_sort import insertionSort",
    number = 10,
    globals={"arr1_copy6":arr1_copy6},
)

t8 = timeit(
    "fastbit_radix_like_sort(arr1_copy7)",
    setup="from jesreal_sort import fastbit_radix_like_sort",
    number = 10,
    globals={"arr1_copy7":arr1_copy7},
)

t9 = timeit(
    "bubbleSort(arr1_copy8)",
    setup="from bubble_sort import bubbleSort",
    number = 10,
    globals={"arr1_copy8":arr1_copy8},
)

t9 = timeit(
    "radixSort(arr1_copy9)",
    setup="from radix_sort import radixSort",
    number = 10,
    globals={"arr1_copy9":arr1_copy9},
)

t10 = timeit(
    "fastbit_radix_sort(arr1_copy10)",
    setup="from normal_fastbit_radix import fastbit_radix_sort",
    number = 10,
    globals={"arr1_copy10":arr1_copy10},
)






l = {
    t1: "Selection Sort", 
    t2: "Enhanced Selection Sort", 
    t3: "Enhanced Selection Merge Sort", 
    t4: "Enhanced Insertion Sort",
    t6: "Power Sort",
    t7: "Insertion Sort",
    t7: "Jesreal Radix Sort",
    t8: "Bubble Sort",
    t9: "Radix Sort",
    t10: "Normal Fastbit Radix Sort",

    
    }

l_sorted = dict(sorted(l.items()))

print()
print(f"At {n} datas")
i = 1
for key, value in l_sorted.items():
    print(f"{i}. {value} @ {key} seconds")
    i += 1
print()