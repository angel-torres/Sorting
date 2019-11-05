# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(0, len(arr) - 1): # iterate through arr
        cur_index = i # initialize cur index
        smallest_index = cur_index # set up reference to smallest current index
        for index in range(i, len(arr)): # iterate through right side of arr
            if arr[smallest_index] > arr[index]: # check if arr[index] is less than current smallest_indes
                smallest_index = index # if it's less, set up new smallest index
        cur_num = arr[i] # set reference to the current number 
        arr[cur_index] = arr[smallest_index] # place smallest index at the curr index
        arr[smallest_index] = cur_num # place curr index at the place where the smallest num was
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( arr ):
    i = 0
    while i < len(arr):
        print(arr[i])
        i += 1
    return arr


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

array = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
bubble_sort(array)
