from benchmark10x_func import *

test_range = 1_000

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
