from benchmark10x_func import *

test_range = 100_000
test = 0 #0 for random, 1 for sorted, 2 for nearly sorted, 3 for reverse sorted
rand = ["Random", "Sorted", "Nearly Sorted", "Reverse Sorted"]

print("For random datas:")


if test == 0:
    # 1-10 at 10 datas
    test_10x(enhanced_insertion, "MB Sort", rand[test], test_range, 10)
    test_10x(insertionSort, "Insertion Sort", rand[test], test_range, 10)

    # 1-10 at 1_000 datas 
    test_10x(enhanced_insertion, "MB Sort", rand[test], test_range, 1_000)
    test_10x(insertionSort, "Insertion Sort", rand[test], test_range, 1_000)

    # 1-10 at 100_000 datas
    test_10x(enhanced_insertion, "MB Sort", rand[test], test_range, 100_000)
    test_10x(insertionSort, "Insertion Sort", rand[test], test_range, 100_000)

    
elif test == 1:
    # 1-10 at 10 datas
    test_10x_sorted(enhanced_insertion, "MB Sort", rand[test], test_range, 10)
    test_10x_sorted(insertionSort, "Insertion Sort", rand[test], test_range, 10)

    # 1-10 at 1_000 datas 
    test_10x_sorted(enhanced_insertion, "MB Sort", rand[test], test_range, 1_000)
    test_10x_sorted(insertionSort, "Insertion Sort", rand[test], test_range, 1_000)

    # 1-10 at 100_000 datas
    test_10x_sorted(enhanced_insertion, "MB Sort", rand[test], test_range, 100_000)
    test_10x_sorted(insertionSort, "Insertion Sort", rand[test], test_range, 100_000)
elif test == 2:
    # 1-10 at 10 datas
    test_10x_n_sorted(enhanced_insertion, "MB Sort", rand[test], test_range, 10)
    test_10x_n_sorted(insertionSort, "Insertion Sort", rand[test], test_range, 10)

    # 1-10 at 1_000 datas 
    test_10x_n_sorted(enhanced_insertion, "MB Sort", rand[test], test_range, 1_000)
    test_10x_n_sorted(insertionSort, "Insertion Sort", rand[test], test_range, 1_000)

    # 1-10 at 100_000 datas
    test_10x_n_sorted(enhanced_insertion, "MB Sort", rand[test], test_range, 100_000)
    test_10x_n_sorted(insertionSort, "Insertion Sort", rand[test], test_range, 100_000)

elif test == 3:
    # 1-10 at 10 datas
    test_10x_r_sorted(enhanced_insertion, "MB Sort", rand[test], test_range, 10)
    test_10x_r_sorted(insertionSort, "Insertion Sort", rand[test], test_range, 10)

    # 1-10 at 1_000 datas 
    test_10x_r_sorted(enhanced_insertion, "MB Sort", rand[test], test_range, 1_000)
    test_10x_r_sorted(insertionSort, "Insertion Sort", rand[test], test_range, 1_000)

    # 1-10 at 100_000 datas
    test_10x_r_sorted(enhanced_insertion, "MB Sort", rand[test], test_range, 100_000)
    test_10x_r_sorted(insertionSort, "Insertion Sort", rand[test], test_range, 100_000)

else:
    print("Invalid number")