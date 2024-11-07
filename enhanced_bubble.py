def bubble_sort(arr):

    # Outer loop to iterate through the list n times
    for n in range(len(arr) - 1, 0, -1):

        # Inner loop to compare adjacent elements
        for i in range(n):
            if arr[i] > arr[i + 1]:

                # Swap elements if they are in the wrong order
                swapped = True
                arr[i], arr[i + 1] = arr[i + 1], arr[i]


def enhanced_bubbleSort(arr):
    n = len(arr)
    n_2 = n//2
    

    j = 0 #1st pointer - arr[0]
    m = len(arr) - 1 #2nd pointer - arr[-1]
    
    for i in range(n_2):
        j = i #1st pointer - arr[0]
        m = len(arr) - 1 - i #2nd pointer - arr[-1]

        for g in range(i):

            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
            
            if arr[m-1] > arr[m]:
                arr[m-1], arr[m] = arr[m], arr[m-1]
            


from timeit import timeit
import random

n = 5000

arr1 = random.choices(range(1, 1000), k = n)
arr1_copy = arr1.copy()

t1 = timeit(
    "bubble_sort(arr1)",
    setup="from enhanced_bubble import bubble_sort",
    number = 10,
    globals={"arr1":arr1},
)

t2 = timeit(
    "enhanced_bubbleSort(arr1_copy)",
    setup="from enhanced_bubble import enhanced_bubbleSort",
    number = 10,
    globals={"arr1_copy":arr1_copy},
)



l = {t1: "Normal Bubble Sort", t2: "Enhanced Bubble Sort"}
l_sorted = dict(sorted(l.items()))
'''print(f"At {n} datas")
print(f"Fastest: {l.get(min(l))} @ {min(l)}")
print(f"Slowest: {l.get(max(l))} @ {max(l)}")
print()'''

print()
i = 1
print(f"At {n} datas")
for key, value in l_sorted.items():
    print(f"{i}. {value} @ {key} seconds")
    i += 1
print()


