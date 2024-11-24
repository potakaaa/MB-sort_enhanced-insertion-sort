import numpy as np
import perfplot

from normal_algo.normal_selection import selectionSort
from normal_algo.merge_sort import mergeSort
from normal_algo.radix_sort import radixSort
from normal_algo.bubble_sort import bubbleSort
from normal_algo.quick_sort import quickSort
from normal_algo.insertion_sort import insertionSort
from enhanced_insertion import enhanced_insertion

test = perfplot.bench(
    setup = lambda n: np.random.rand(n),
    kernels=[
        selectionSort,
        bubbleSort,
        insertionSort,
        enhanced_insertion,
        radixSort,
    ],
    labels=["Selection Sort", 
            "Bubble Sort",
            "Insertion Sort",
            "MB Sort", 
            "Radix Sort",
            ],
    n_range=[2**k for k in range(15)],  
    xlabel="Number of elements",
    equality_check=None,
)

print(test)