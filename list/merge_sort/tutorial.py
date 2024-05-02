def merge_sort(list):
    """
    Sorts a list in ascending order
    Returns a new sorted list

    Divide: Find the midpoint of the list list and divide into sublists
    Conquer: Recursively sort the sublists created in pevious step
    Combine: Merge the sorted sublists created in previous step

    Takes O(n log(n))
    """

    if len(list) <= 1:
        return list

    left_half, right_half = split(list)
    sorted_left_half = merge_sort(left_half)
    sorted_right_half = merge_sort(right_half)

    return merge(sorted_left_half, sorted_right_half)


def split(list):
    """
    Divide the unsorted list at midpoint into sublists
    Returns two sublists - left and right
    """

    mid = len(list) // 2
    left = list[:mid]
    right = list[mid:]

    return left, right


def merge(left, right):
    """
    Merges two lists (arrays), sorting them in the process
    Returns a new merged list
    """
    print(f"Merge sorting {left} and {right}")

    list = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            list.append(left[left_index])
            left_index += 1
        else:
            list.append(right[right_index])
            right_index += 1

    while left_index < len(left):
        list.append(left[left_index])
        left_index += 1

    while right_index < len(right):
        list.append(right[right_index])
        right_index += 1

    return list


def verify_sorted(list):
    n = len(list)

    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify_sorted(list[1:])


alist = [54, 62, 93, 17, 77, 31, 44, 55, 20]
list = merge_sort(alist)
print(verify_sorted(list))


"""Process
    [54, 62, 93, 17, 77, 31, 44, 55, 20]
[54, 62, 93, 17]        [77, 31, 44, 55, 20]
[54, 62] [93, 17]       [77, 31]     [44, 55, 20]
[54] [62] [93] [17]    [77] [31]    [44]  [55, 20]
                                          [55] [20]
"""
