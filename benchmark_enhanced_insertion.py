from timeit import timeit
import random
import numpy as np
import perfplot
from insertion_sort import insertionSort
from enhanced_insertion import enhanced_insertion

n = 10000

arr1 = random.choices(range(1, 1000), k = n)

t1 = timeit(
    "insertionSort(arr1)",
    setup="from insertion_sort import insertionSort",
    number = 10,
    globals={"arr1":arr1},
)

t2 = timeit(
    "enhanced_insertion(arr1)",
    setup="from enhanced_insertion import enhanced_insertion",
    number = 10,
    globals={"arr1":arr1},
)

l = {t1: "Normal Insertion Sort", t2: "Enhanced Insertion Sort"}

print(f"At {n} datas")
print(f"Fastest: {l.get(min(l))} @ {min(l)}")
print(f"Slowest: {l.get(max(l))} @ {max(l)}")
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