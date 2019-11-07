# TO-DO: Complete the selection_sort() function below 
def selection_sort( arr ):
    for i in range(0, len(arr) - 1): # iterate through arr
        cur_index = i # initialize cur index
        smallest_index = cur_index # set up reference to smallest current index
        for index in range(i, len(arr)): # iterate through right side of arr
            if arr[smallest_index] > arr[index]: # check if arr[index] is less than current smallest_indes
                smallest_index = index # if it's less, set up new smallest index
        #cur_num = arr[i] # set reference to the current number 
        #arr[cur_index] = arr[smallest_index] # place smallest index at the curr index
        #arr[smallest_index] = cur_num # place curr index at the place where the smallest num was
        arr[cur_index], arr[smallest_index] = arr[smallest_index], arr[cur_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort( array ):
    # loop over list and compare current index to next index
    # if current is greater than next -> flip numbers
    # if there is a flip then set flip to true
    # continue to loop over list until there are no flips
    # return sorted list
    flip = True 
    while flip is True:
        flips = 0
        for i in range(0, len(array) - 1):
            if array[i] > array[i + 1]:
                curr_value = array[i]
                array[i] = array[i + 1]
                array[i + 1 ] = curr_value
                flips += 1
        if flips == 0:
            flip = False
    return array


# STRETCH: implement the Count Sort function below
def count_sort( arr, maximum=-1 ):

    return arr

array1 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(bubble_sort(array1))
