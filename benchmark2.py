import numpy as np
import perfplot

from normal_selection import selectionSort
from pointer_selection import enhanced_selection
from pointer_selection_merge import enhanced_selection_merge

perfplot.live(
    setup = lambda n: np.random.rand(n).tolist(),
    kernels=[
        selectionSort,
        enhanced_selection,
        enhanced_selection_merge,
    ],
    labels=["Normal Selection", "Enhanced Selection", "Enhanced Selection Merge"],
    n_range=[2**k for k in range(15)],  
    xlabel="Number of elements",

)