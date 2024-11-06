import numpy as np
import perfplot

from normal_selection import selectionSort
from pointer_selection import enhanced_selection
from pointer_selection_merge import enhanced_selection_merge
from merge_sort import mergeSort
from radix_sort import radixSort
from bubble_sort import bubbleSort
from insertion_sort import insertionSort
from enhanced_insertion import enhanced_insertion
from enhanced_insertion_mid import enhanced_insertion2

perfplot.live(
    setup = lambda n: np.random.rand(n).tolist(),
    kernels=[
        selectionSort,
        enhanced_selection,
        enhanced_selection_merge,
        bubbleSort,
        insertionSort,
        enhanced_insertion,
        enhanced_insertion2,
        sorted,
        mergeSort,
        radixSort,
    ],
    labels=["Normal Selection", 
            "Enhanced Selection", 
            "Enhanced Selection Merge", 
            "Bubble Sort",
            "Insertion Sort",
            "Enhanced Insertion Sort",
            "Enhanced Insertion Sort 2",
            "Default Python Sort", 
            "Normal Merge Sort", 
            "Radix Sort",],
    n_range=[2**k for k in range(15)],  
    xlabel="Number of elements",
    equality_check=None
)