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
from linked_list import list_to_linked_list
from jesreal_sort import fastbit_radix_like_sort
from normal_fastbit_radix import fastbit_radix_sort

perfplot.live(
    setup = lambda n: np.random.rand(n).tolist(),
    kernels=[
        selectionSort,
        enhanced_selection,
        enhanced_selection_merge,
        bubbleSort,
        insertionSort,
        enhanced_insertion,
        lambda arr: enhanced_insertion2(list_to_linked_list(arr)),
        sorted,
        mergeSort,
        radixSort,
        fastbit_radix_like_sort,
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
            "Radix Sort",
            "Jesreal Radix Sort",],
    n_range=[2**k for k in range(15)],  
    xlabel="Number of elements",
    equality_check=None
)