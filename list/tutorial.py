def linear_search(list, target):
    """
    Returns the index position of the target if found, else returns None
    """

    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


def verify(index):
    if index is not None:
        print("Target found at index:", index)
    else:
        print("Target not found in list")


def binary_search(list, target):
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1
    return None


def recursive_binary_search(list, target):
    if len(list) == 0:
        return False
    else:
        midpoint = len(list) // 2

        if list[midpoint] == target:
            return True
        else:
            if list[midpoint] < target:
                return recursive_binary_search(list[midpoint + 1 :], target)
            else:
                return recursive_binary_search(list[:midpoint], target)


my_list = [1, 3, 6, 8, 9]

result = linear_search(my_list, 1)
verify(result)

result = binary_search(my_list, 10)
verify(result)

result = recursive_binary_search(my_list, 1)
verify(result)
