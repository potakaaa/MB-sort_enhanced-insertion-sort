from timeit import timeit
import random
import numpy as np
import perfplot
from normal_algo.insertion_sort import insertionSort
from enhanced_insertion import enhanced_insertion
from others.linked_list import LinkedList


n = 10000

arr1 = random.choices(range(1, 1000), k = n)
arr1_copy = arr1.copy()
arr1_copy2 = arr1.copy()
arr1_copy3 = arr1.copy()

t1 = timeit(
    "insertionSort(arr1)",
    setup="from normal_algo.insertion_sort import insertionSort",
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
    "binary_insertion_sort(arr1_copy2)",
    setup="from binary_insertion import binary_insertion_sort",
    number = 10,
    globals={"arr1_copy2":arr1_copy2},
)

'''t3 = timeit(
    "enhanced_insertion2(list_to_linked_list(arr1_copy2))",
    setup="from enhanced_insertion_mid import enhanced_insertion2\nfrom linked_list import list_to_linked_list",
    number = 10,
    globals={"arr1_copy2":arr1_copy2},
)'''

t4 = timeit(
    "sorted(arr1_copy3)",
    number = 10,
    globals={"arr1_copy3":arr1_copy3},
)

l = {t1: "Normal Insertion Sort", t2: "Enhanced Insertion Sort", t3: "Binsertion Sort", t4: "Power Sort"}
l_sorted = dict(sorted(l.items()))
'''print(f"At {n} datas")
print(f"Fastest: {l.get(min(l))} @ {min(l)}")
print(f"Slowest: {l.get(max(l))} @ {max(l)}")
print()'''

i, runtime = 1, []

for key, value in l.items():
    runtime.append(key)

print()
print(f"At {n} datas")
for key, value in l_sorted.items():
    print(f"{i}. {value} @ {key} seconds")
    i += 1
print()


improv_per = ((runtime[0] - runtime[1]) / runtime[0]) * 100


print(f"Improvement Percentage: {round(improv_per)} % | {"Slower" if list(l_sorted.values())[1] == "Normal Insertion Sort" else "Faster"}")

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