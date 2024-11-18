from enhanced_insertion import enhanced_insertion
from enhanced_insertion_mid import enhanced_insertion2
from bst_insertion import enhanced_insertion_bst
import random

a = random.choices(range(1, 10), k = 10)
a2 = [random.uniform(1, 1000) for _ in range(10)]


#print(sorted(a) == enhanced_selection_merge(a))

a = [3, 3, 9, 4, 5, 9, 1, 5, 6, 8]
print(enhanced_insertion(a) == sorted(a))
