from pointer_selection_merge import enhanced_selection_merge
from enhanced_insertion import enhanced_insertion
from enhanced_insertion_mid import enhanced_insertion2
import random

a = random.choices(range(1, 1000), k = 10000)


#print(sorted(a) == enhanced_selection_merge(a))

print(sorted(a) == enhanced_insertion2(a))