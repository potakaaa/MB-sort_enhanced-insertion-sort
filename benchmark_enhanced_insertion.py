from timeit import timeit
import random
import numpy as np
import perfplot
from insertion_sort import insertionSort
from enhanced_insertion import enhanced_insertion

n = 5000

arr1 = random.choices(range(1, 1000), k = n)
arr1_copy = arr1.copy()
arr1_copy2 = arr1.copy()
arr1_copy3 = arr1.copy()

t1 = timeit(
    "insertionSort(arr1)",
    setup="from insertion_sort import insertionSort",
    number = 10,
    globals={"arr1":arr1},
)

t2 = timeit(
    "enhanced_insertion(arr1_copy)",
    setup="from enhanced_insertion import enhanced_insertion",
    number = 10,
    globals={"arr1_copy":arr1_copy},
)

t3 = timeit(
    "enhanced_insertion2(arr1_copy2)",
    setup="from enhanced_insertion_mid import enhanced_insertion2",
    number = 10,
    globals={"arr1_copy2":arr1_copy2},
)

t4 = timeit(
    "sorted(arr1_copy3)",
    number = 10,
    globals={"arr1_copy3":arr1_copy3},
)

l = {t1: "Normal Insertion Sort", t2: "Enhanced Insertion Sort", t3: "Enhanced Insertion Sort Mid", t4: "Power Sort"}
l_sorted = dict(sorted(l.items()))
'''print(f"At {n} datas")
print(f"Fastest: {l.get(min(l))} @ {min(l)}")
print(f"Slowest: {l.get(max(l))} @ {max(l)}")
print()'''

print()
i = 1
print(f"At {n} datas")
for key, value in l_sorted.items():
    print(f"{i}. {value} @ {key} seconds")
    i += 1
print()

'''perfplot.live(
    setup = lambda n: np.random.rand(n).tolist(),
    kernels=[
        insertionSort,
        enhanced_insertion,

    ],
    labels=["Insertion Sort",
            "Enhanced Insertion Sort",],
    n_range=[2**k for k in range(17)], 
    xlabel="Number of elements",
    equality_check=None
)'''