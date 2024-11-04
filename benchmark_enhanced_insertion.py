from timeit import timeit
import random

n = 5000

arr1 = random.choices(range(1, 1000), k = n)

t1 = timeit(
    "insertionSort(arr1)",
    setup="from insertion_sort import insertionSort",
    number = 10,
    globals={"arr1":arr1},
)

t2 = timeit(
    "enhanced_insertion3(arr1)",
    setup="from enhanced_insertion import enhanced_insertion3",
    number = 10,
    globals={"arr1":arr1},
)

l = {t1: "Normal Insertion Sort", t2: "Enhanced Insertion Sort"}

print(f"At {n} datas")
print(f"Fastest: {l.get(min(l))} @ {min(l)}")
print(f"Slowest: {l.get(max(l))} @ {max(l)}")
print()