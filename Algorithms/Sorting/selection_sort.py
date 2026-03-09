#Selection sort code
def selection_sort(arr):
    for i in range(len(arr)):
        smallest_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                #selecting index of smallest element in array
                smallest_index = j
        #placing selected smallest with rightmost element through swapping
        arr[i], arr[smallest_index] = arr[smallest_index], arr[i]
    return arr
#Sample run
print(selection_sort([9,4,10,2,0,12]))

