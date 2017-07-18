def find_index_of_smallest_int_in_array(arr):
    smallest_index = 0

    for i in range(len(arr)):
        if arr[i] < arr[smallest_index]:
            smallest_index = i

    return smallest_index


def selection_sort(arr):
    sortedArr = []

    for i in range(len(arr)):
        index = find_index_of_smallest_int_in_array(arr)
        sortedArr.append(arr[index])
        arr.pop(index)

    return sortedArr


numbers = [4, 7, 10, 2, 9, 11, 1, 3, 5, 8, 19]

print(selection_sort(numbers))
