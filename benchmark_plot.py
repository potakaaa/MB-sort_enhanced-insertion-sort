import numpy as np
import perfplot

from normal_algo.normal_selection import selectionSort
from normal_algo.merge_sort import mergeSort
from normal_algo.radix_sort import radixSort
from normal_algo.bubble_sort import bubbleSort
from normal_algo.insertion_sort import insertionSort
from enhanced_insertion import enhanced_insertion

test = perfplot.bench(
    setup = lambda n: np.random.rand(n).tolist(),
    kernels=[
        selectionSort,
        bubbleSort,
        insertionSort,
        enhanced_insertion,
        mergeSort,
        radixSort,
        
    ],
    labels=["Normal Selection", 
            "Bubble Sort",
            "Insertion Sort",
            "MB Sort",
            "Normal Merge Sort", 
            "Radix Sort",
            ],
    n_range=[2**k for k in range(15)],  
    xlabel="Number of elements",
    equality_check=None
)

print(test)