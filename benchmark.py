from timeit import timeit
import random

n = 5000

arr1 = random.choices(range(1, 1000), k = n)

t1 = timeit(
    "selectionSort(arr1)",
    setup="from normal_selection import selectionSort",
    number = 10,
    globals={"arr1":arr1},
)
'''print()
print("Normal Selection runtime: ", t1)'''

t2 = timeit(
    "enhanced_selection(arr1)",
    setup="from pointer_selection import enhanced_selection",
    number = 10,
    globals={"arr1":arr1},
)
'''print("Enhanced Selection runtime: ", t1)
print()'''

t3 = timeit(
    "enhanced_selection_merge(arr1)",
    setup="from pointer_selection_merge import enhanced_selection_merge",
    number = 10,
    globals={"arr1":arr1},
)
'''print("Enhanced Selection with Merge runtime: ", t3)
print("Enhanced Selection runtime: ", t2)
print(f"Difference in runtime: {t3 - t2}" if t3 > t2 else f"Difference in runtime: {t2 - t3}")
print()'''

t4 = timeit(
    "enhanced_insertion(arr1)",
    setup="from enhanced_insertion import enhanced_insertion",
    number = 10,
    globals={"arr1":arr1},
)
print("Enhanced Insertion runtime: ", t4)

l = {t1: "Normal Selection Sort", t2: "Enhanced Selection Sort", t3: "Enhanced Selection Merge Sort", t4: "Enhanced Insertion Sort"}

print(f"At {n} datas")
print(f"Fastest: {l.get(min(l))} @ {min(l)}")
print(f"Slowest: {l.get(max(l))} @ {max(l)}")
print()