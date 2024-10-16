import random

def quickselect(a, k, left=0, right=None):
    if right is None:
        right = len(a) - 1
    pivotIndex = random.randint(left, right)
    pivotIndex = partition(a, left, right, pivotIndex)
    if pivotIndex == k - 1:
        return a[pivotIndex]
    elif pivotIndex < k - 1:
        return quickselect(a, k, pivotIndex + 1, right)
    else:
        return quickselect(a, k, left, pivotIndex - 1)

def partition(a, left, right, pivotIndex):
    pivotValue = a[pivotIndex]
    a[pivotIndex], a[right] = a[right], a[pivotIndex]
    storeIndex = left
    for i in range(left, right):
        if a[i] < pivotValue:
            a[i], a[storeIndex] = a[storeIndex], a[i]
            storeIndex += 1
    a[right], a[storeIndex] = a[storeIndex], a[right]
    return storeIndex

a = list(map(int, input("Enter the array: ").split()))
k = int(input("Enter value of k: "))
print(f"The {k}th smallest element is: {quickselect(a, k)}")


"""Enter the array: 3 1 4 1 5 9 2 6 5 3 5
Enter value of k: 4
The 4th smallest element is: 3"""

