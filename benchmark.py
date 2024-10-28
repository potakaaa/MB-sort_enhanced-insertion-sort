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
print()
print("Normal Selection runtime: ", t1)

t2 = timeit(
    "enhanced_selection(arr1)",
    setup="from pointer_selection import enhanced_selection",
    number = 10,
    globals={"arr1":arr1},
)
print("Enhanced Selection runtime: ", t1)
print()

t1 = timeit(
    "enhanced_selection_merge(arr1)",
    setup="from pointer_selection_merge import enhanced_selection_merge",
    number = 10,
    globals={"arr1":arr1},
)
print("Enhanced Selection with Merge runtime: ", t1)
print("Enhanced Selection runtime: ", t2)
print(f"Difference in runtime: {t2 - t1}" if t2 > t1 else f"Difference in runtime: {t1 - t2}")
print()