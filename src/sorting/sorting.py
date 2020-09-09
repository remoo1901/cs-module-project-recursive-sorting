# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    for i in arrA:
        merged_arr.append(i)
    for j in arrB:
        merged_arr.append(j)

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively


def partition(arr):

    left = []
    pivot = arr[0]
    right = []

    for num in arr[1:]:
        if num <= pivot:
            left.append(num)
        else:
            right.append(num)

    return left, pivot, right


def merge_sort(arr):

    if len(arr) <= 1:
        return arr

    left, pivot, right = partition(arr)

    arr = merge_sort(left) + [pivot] + merge_sort(right)

    return arr


# STRETCH: implement the recursive logic for merge sort in a way that doesn't
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists
# or data structures; it can only re-use the memory it was given as input
""" def merge_in_place(arr, start, mid, end):
    # Your code here


def merge_sort_in_place(arr, l, r):
    # Your code here
 """
