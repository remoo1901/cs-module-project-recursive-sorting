# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):

    if len(arr) == 0:
        return -1

    elif len(arr) == 1:
        if arr[0] == target:
            return 0
        else:
            return -1
    else:
        middle = (start + end) // 2

        if arr[middle] == target:
            return middle

        elif arr[middle] < target:
            return binary_search(arr, target, middle + 1, end)
            
        else:
            return binary_search(arr, target, start, middle - 1)


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here
