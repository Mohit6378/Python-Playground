def insertion_sort(arr):
    for i in range(1, len(arr)):
        #taking second element as key
        key = arr[i]
        j = i - 1
        while (j > -1 and arr[j] > key):
            #shifting right side to find place for key
            arr[j + 1] = arr[j]
            j -= 1
        #placing key
        arr[j + 1] = key

sample_list = [8,2,5,3,7,5,9]
print(sample_list, "--before sorting")
insertion_sort(sample_list)
print(sample_list, "--after sorting")