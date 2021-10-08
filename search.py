import math


def linear_search(array, x):
    for item in array:
        if item == x:
            return x
    return -1


def binary_search_recursive(array, x):
    size = len(array)

    if size < 1:
        return -1
    elif size == 1:
        return x if array[0] == x else -1

    mid = size // 2

    if array[mid] == x:
        return x
    elif array[mid] > x:
        return binary_search_recursive(array[0: mid], x)
    else:
        return binary_search_recursive(array[mid: size], x)
    return -1


def binary_search_iterative(array, x):
    low = 0
    high = len(array)

    while low < high:
        mid = low + ((high - low) // 2)
        if array[mid] == x:
            return x
        elif x < array[mid]:
            high = mid
        else:
            low = mid

    return -1


arr = [2, 3, 4, 10, 40, 41, 45, 50]
print(binary_search_iterative(arr, 50))
