import pandas as pd
from timeit import timeit

df = pd.read_excel('./data/testdata2.xlsx', sheet_name=1) # can also index sheet by name or fetch all sheets
mylist2 = df['TOTAL INCOME'].tolist()

#print(mylist)
mylist = mylist2[0:5000]

t1 = timeit(
    "insertionSort(mylist)",
    setup="from insertion_sort import insertionSort",
    number = 1,
    globals={"mylist":mylist},
)

t2 = timeit(
    "enhanced_insertion(mylist)",
    setup="from enhanced_insertion import enhanced_insertion",
    number = 1,
    globals={"mylist":mylist},
)

l = {t1: "Normal Insertion Sort", t2: "Enhanced Insertion Sort"}

print(f"At {len(mylist)} datas")
print(f"Fastest: {l.get(min(l))} @ {min(l)}")
print(f"Slowest: {l.get(max(l))} @ {max(l)}")
print()
