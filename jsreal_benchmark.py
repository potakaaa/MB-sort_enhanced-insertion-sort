import perfplot
import numpy as np
from jesreal_sort import fastbit_radix_like_sort
from normal_fastbit_radix import fastbit_radix_sort
from radix_sort import radixSort

perfplot.live(
    setup=lambda n: np.random.randint(0, 1000, n).tolist(),
    kernels=[
        radixSort,
        fastbit_radix_like_sort,
        fastbit_radix_sort,
    ],
    labels=["Radix Sort", "Jesreal Radix Sort", "Normal Fastbit Radix Sort"],
    n_range=[2**k for k in range(15)],
    xlabel="Number of elements",
    equality_check=None
)