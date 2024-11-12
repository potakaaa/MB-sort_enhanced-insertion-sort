import numpy as np
import perfplot

from normal_algo.normal_selection import selectionSort
from enhanced_algo.pointer_selection import enhanced_selection
from enhanced_algo.pointer_selection_merge import enhanced_selection_merge
from normal_algo.merge_sort import mergeSort
from normal_algo.radix_sort import radixSort
from normal_algo.bubble_sort import bubbleSort
from normal_algo.insertion_sort import insertionSort
from enhanced_insertion import enhanced_insertion
from enhanced_insertion_mid import enhanced_insertion2
from others.linked_list import list_to_linked_list
from enhanced_algo.jesreal_sort import fastbit_radix_like_sort
from normal_algo.normal_fastbit_radix import fastbit_radix_sort

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
            ],
    n_range=[2**k for k in range(15)],  
    xlabel="Number of elements",
    equality_check=None
)