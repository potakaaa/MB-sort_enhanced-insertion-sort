from pointer_selection_merge import enhanced_selection_merge
from enhanced_insertion import enhanced_insertion
from enhanced_insertion_mid import enhanced_insertion2
from jesreal_sort import fastbit_radix_like_sort
import random

a = random.choices(range(1, 1000), k = 10000)
a2 = [random.uniform(1, 1000) for _ in range(10)]


#print(sorted(a) == enhanced_selection_merge(a))

print(a2)
print(sorted(a2) == fastbit_radix_like_sort(a2))
print(a2)