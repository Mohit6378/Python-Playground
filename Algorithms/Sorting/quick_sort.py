def quick_sort(arr):
    #base-case
    if (len(arr) < 2):
        return arr
    #recursive-case
    else:
    #finding the right pivot element
        mid = len(arr) // 2
        pivot_candidates = [arr[0], arr[mid], arr[-1]]
        pivot = sorted(pivot_candidates)[1]
        #partitioning the array
        greater = [i for i in arr if i > pivot]
        equal = [i for i in arr if i == pivot]
        lesser = [i for i in arr if i < pivot]
        
        return quick_sort(lesser) + equal + quick_sort(greater)
#sample run
print(quick_sort([5,2,10,7,1,9]))