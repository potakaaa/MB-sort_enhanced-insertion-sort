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
    print(arr)
    

    for i in range(n_2):
        j = i #1st pointer - arr[0]
        m = len(arr) - 1 - i #2nd pointer - arr[-1]
        print(arr)

        for g in range(i):

            if arr[j+1] < arr[j]:
                print(f"1st pointer: {arr[j]}")
                arr[j+1], arr[j] = arr[j], arr[j+1]
                print("1st POINTER SWAPPED")
                print(arr)
            
            if arr[m-1] > arr[m]:
                print(f"2nd pointer: {arr[m]}")
                arr[m-1], arr[m] = arr[m], arr[m-1]
                print("2nd POINTER SWAPPED")
                print(arr)
            



# Sample list to be sorted
arr = [39, 12, 72, 10, 2, 18]
print("-----NORMAL BUBBLE SORT-----")
print("Unsorted list is:")
print(arr)

bubble_sort(arr)

print("Sorted list is:")
print(arr)


arr2 = [39, 12, 72, 10, 2, 18]
print("\n-----ENHANCED BUBBLE SORT-----")
print("Unsorted list is:")
print(arr2)


enhanced_bubbleSort(arr2)

print("Sorted list is:")
print(arr2)


