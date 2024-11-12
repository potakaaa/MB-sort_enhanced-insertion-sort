from benchmark10x_func import *

test_range = 10

rand = ["Random", "Sorted", "Nearly Sorted", "Reverse Sorted"]

print("For random datas:")
# 1-10 at 10 datas
test_10x(enhanced_insertion, "MB Sort", rand[0], test_range, 10)
test_10x(insertionSort, "Insertion Sort", rand[0], test_range, 10)

# 1-10 at 1_000 datas 
test_10x(enhanced_insertion, "MB Sort", rand[0], test_range, 1_000)
test_10x(insertionSort, "Insertion Sort", rand[0], test_range, 1_000)

# 1-10 at 100_000 datas
test_10x(enhanced_insertion, "MB Sort", rand[0], test_range, 100_000)
test_10x(insertionSort, "Insertion Sort", rand[0], test_range, 100_000)


print("For sorted datas:")
# 1-10 at 10 datas
test_10x_sorted(enhanced_insertion, "MB Sort", rand[1], test_range, 10)
test_10x_sorted(insertionSort, "Insertion Sort", rand[1], test_range, 10)

# 1-10 at 1_000 datas 
test_10x_sorted(enhanced_insertion, "MB Sort", rand[1], test_range, 1_000)
test_10x_sorted(insertionSort, "Insertion Sort", rand[1], test_range, 1_000)

# 1-10 at 100_000 datas
test_10x_sorted(enhanced_insertion, "MB Sort", rand[1], test_range, 100_000)
test_10x_sorted(insertionSort, "Insertion Sort", rand[1], test_range, 100_000)


print("For nearly sorted datas:")
# 1-10 at 10 datas
test_10x_n_sorted(enhanced_insertion, "MB Sort", rand[2], test_range, 10)
test_10x_n_sorted(insertionSort, "Insertion Sort", rand[2], test_range, 10)

# 1-10 at 1_000 datas 
test_10x_n_sorted(enhanced_insertion, "MB Sort", rand[2], test_range, 1_000)
test_10x_n_sorted(insertionSort, "Insertion Sort", rand[2], test_range, 1_000)

# 1-10 at 100_000 datas
test_10x_n_sorted(enhanced_insertion, "MB Sort", rand[2], test_range, 100_000)
test_10x_n_sorted(insertionSort, "Insertion Sort", rand[2], test_range, 100_000)


print("For reversed sorted datas:")
# 1-10 at 10 datas
test_10x_r_sorted(enhanced_insertion, "MB Sort", rand[3], test_range, 10)
test_10x_r_sorted(insertionSort, "Insertion Sort", rand[3], test_range, 10)

# 1-10 at 1_000 datas 
test_10x_r_sorted(enhanced_insertion, "MB Sort", rand[3], test_range, 1_000)
test_10x_r_sorted(insertionSort, "Insertion Sort", rand[3], test_range, 1_000)

# 1-10 at 100_000 datas
test_10x_r_sorted(enhanced_insertion, "MB Sort", rand[3], test_range, 100_000)
test_10x_r_sorted(insertionSort, "Insertion Sort", rand[3], test_range, 100_000)