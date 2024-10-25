import random, time


def test_algo(algo, algo_name, arr):
    print(f"\n\n-----{algo_name} SORT-----")
    #print("Unsorted list is:")
    #print(arr)

    arr_sorted = algo(arr)

    #print("\nSorted list is:")
    #print(arr)


    print("Algo is Correct" if sorted(arr) == arr_sorted[0] else "Algo is Not Correct")
    
