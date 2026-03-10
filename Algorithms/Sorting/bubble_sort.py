def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            #taking largest element to rightmost side
            if (arr[j] > arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  #no swap means already sorted
            break
    return arr
#sample run
print(bubble_sort([2,8,3,10,6,1]))