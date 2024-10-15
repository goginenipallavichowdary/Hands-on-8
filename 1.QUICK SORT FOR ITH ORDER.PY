import random

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quickselect(arr, low, high, k):
    if low == high:
        return arr[low]
    
    pivot_index = partition(arr, low, high)
    
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, low, pivot_index - 1, k)
    else:
        return quickselect(arr, pivot_index + 1, high, k)

def ith_order_statistic(arr, i):
    if i < 1 or i > len(arr):
        return None
    
    arr_copy = arr.copy()
    
    return quickselect(arr_copy, 0, len(arr_copy) - 1, i - 1)

# Demonstration
arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Original array:", arr)

for i in range(1, len(arr) + 1):
    result = ith_order_statistic(arr, i)
    print(f"{i}th order statistic: {result}")

# Verify the results
sorted_arr = sorted(arr)
print("Sorted array:", sorted_arr)
