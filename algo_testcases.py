import random, time


def test_algo(algo, algo_name, arr):
    print(f"\n\n-----{algo_name} SORT-----")
    #print("Unsorted list is:")
    #print(arr)

    arr_sorted = algo(arr)

    #print("\nSorted list is:")
    #print(arr)


    print("Algo is Correct" if sorted(arr) == arr_sorted[0] else "Algo is Not Correct")


def test_algo_works(algo, algo_name, arr):
    print("Unsorted: ", arr)

    enhanced = algo(arr)[0]

    print("Normal selection sorted: ", sorted(arr))
    print("Enhanced selection sorted: ", enhanced)

    print(f"Enhanced {algo_name} Sort is working" if enhanced == sorted(arr) else f"Enhanced {algo_name} Sort is not working")
    print()


      
    
