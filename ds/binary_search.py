def iterative(array, target):
    upper_bound = len(array) - 1
    lower_bound = 0

    while True:
        mid = (upper_bound + lower_bound) // 2

        if array[mid] == target:
            return mid
        elif target < array[mid]:
            upper_bound = mid - 1
        elif array[mid] < target:
            lower_bound = mid + 1

        if lower_bound > upper_bound:
            return -1


def recursive(array, target, lower_bound, upper_bound):
    if lower_bound > upper_bound:
        return -1

    mid = (upper_bound + lower_bound) // 2

    if array[mid] == target:
        return mid
    elif target < array[mid]:
        return recursive(array, target, lower_bound, mid - 1)
    elif array[mid] < target:
        return recursive(array, target, mid + 1, upper_bound)