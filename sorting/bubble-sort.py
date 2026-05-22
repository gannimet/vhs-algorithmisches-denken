import random

def bubble_sort(items):
    result_list = items[:]

    for iteration in range(len(result_list)):
        swapped = False

        for i in range(len(result_list) - iteration - 1):
            if result_list[i] > result_list[i + 1]:
                result_list[i], result_list[i + 1] = result_list[i + 1], result_list[i]
                swapped = True

        if not swapped:
            break

    return result_list

all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
unsorted = random.sample(all_numbers, 6)
print(f"Unsorted: {unsorted}")
print(f"Sorted: {bubble_sort(unsorted)}")