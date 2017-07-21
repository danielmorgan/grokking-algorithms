# My solution, manipulate array and pass it down
def sum(arr, total = 0):
    if (len(arr) == 0):
        return total
    else:
        num = arr.pop()
        total += num
        return sum(arr, total)

print(sum([1, 2, 3, 4, 5, 5, 1])) # 21


# Terser solution from book
def sum_answer(list):
    if list == []:
        return 0
    return list[0] + sum_answer(list[1:])

print(sum_answer([1, 2, 3, 4, 5])) # 15
