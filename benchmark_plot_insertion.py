import numpy as np
import perfplot

from normal_algo.insertion_sort import insertionSort
from enhanced_insertion import enhanced_insertion


perfplot.live(
    setup = lambda n: np.random.rand(n).tolist(),
    kernels=[
        insertionSort,
        enhanced_insertion,
        
    ],
    labels=[
            "Insertion Sort",
            "Enhanced Insertion Sort",
            ],
    n_range=[2**k for k in range(15)],  
    xlabel="Number of input samples",
    equality_check=None,
    show_progress=True,
    logx=True,
    logy=True,
)