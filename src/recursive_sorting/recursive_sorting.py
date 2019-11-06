# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge( arrA, arrB ):
	#elements = len( arrA ) + len( arrB )
	#merged_arr = arrA + arrB
    elements = len( arrA ) + len( arrB )
    merged_arr = [0] * elements
    #unsorted_arr = arrA + arrB
	# TO-DO
	# iterate and push elements from arrA and arrB to merged_arr
    elem_i = 0
    arrA_i = 0
    arrB_i = 0	

    while elem_i < elements:
        if arrA_i > len(arrA) - 1:
            merged_arr[elem_i] = arrB[arrB_i]
            arrB_i += 1
        elif arrB_i > len(arrB) - 1:
            merged_arr[elem_i] = arrA[arrA_i]
            arrA[arrA_i] += 1
        elif arrA[arrA_i] < arrB[arrB_i]:
            merged_arr[elem_i] = arrA[arrA_i]
            arrA_i += 1
        elif arrA[arrA_i] > arrB[arrB_i]:
            merged_arr[elem_i] = arrB[arrB_i]
            arrB_i += 1
        elem_i += 1
 
    return merged_arr


# TO-DO: implement the Merge Sort function below USING RECURSION
def merge_sort( arr ):
    # TO-DO
    if len(arr) <= 1:
        return arr
    arrA = arr[:len(arr)//2]
    arrB = arr[len(arr)//2:]
    return merge(merge_sort(arrA), merge_sort(arrB))


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r): 
    # TO-DO

    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort( arr ):

    return arr

arr1 = [ 2, 7, 9, 1, 8, 3, 6, 4, 0, 5,]  
arr2 = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]
print(merge_sort(arr1))
print(merge_sort(arr2))
