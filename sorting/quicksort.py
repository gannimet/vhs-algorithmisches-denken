import random

def quicksort(items):
    list_length = len(items)

    if list_length <= 1:
        return items

    pivot_index = list_length // 2
    pivot_element = items[pivot_index]
    smaller_than_pivot = []
    bigger_than_pivot = []
    equal_to_pivot = []

    for e in items:
        if e < pivot_element:
            smaller_than_pivot.append(e)
        elif e > pivot_element:
            bigger_than_pivot.append(e)
        else:
            equal_to_pivot.append(e)

    return [*quicksort(smaller_than_pivot), *equal_to_pivot, *quicksort(bigger_than_pivot)]


all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
unsorted = random.sample(all_numbers, 6)
print(f"Unsorted: {unsorted}")
print(f"Sorted: {quicksort(unsorted)}")