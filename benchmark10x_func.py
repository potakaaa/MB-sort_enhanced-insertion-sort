from timeit import timeit
import random
from normal_algo.insertion_sort import insertionSort
from enhanced_insertion import enhanced_insertion
from nearly_sort import nearly_sorted

def test_10x(func, name, r, n):
    print(f"Benchmark for {name} \n@ {n} datas ranging from 1 - {r}")
    for i in range(1,11):
        arr1 = random.choices(range(1, r), k = n)
        t1 = timeit(
        lambda: func(arr1),
        number = 1,
        globals={"arr1": arr1, "func": func},
        )
        print(f"{t1}")
    print()

def test_10x_n_sorted(func, name, r, n):
    print(f"Benchmark for {name} \n@ {n} sorted datas ranging from 1 - {r}")
    for i in range(1,11):
        arr1 = random.choices(range(1, r), k = n)
        arr1 = nearly_sorted(arr1)
        t1 = timeit(
        lambda: func(arr1),
        number = 1,
        globals={"arr1": arr1, "func": func},
        )
        print(f"{t1}")
    print()

def test_10x_sorted(func, name, r, n):
    print(f"Benchmark for {name} \n@ {n} sorted datas ranging from 1 - {r}")
    for i in range(1,11):
        arr1 = random.choices(range(1, r), k = n)
        arr1.sort()
        t1 = timeit(
        lambda: func(arr1),
        number = 1,
        globals={"arr1": arr1, "func": func},
        )
        print(f"{t1}")
    print()