import random

def selection_sort(items):
    result_list = items[:]

    for i in range(len(result_list)):
        min_idx = i

        for j in range(i, len(result_list)):
            if result_list[j] < result_list[min_idx]:
                min_idx = j

        result_list[i], result_list[min_idx] = result_list[min_idx], result_list[i]

    return result_list


all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
unsorted = random.sample(all_numbers, 6)
print(f"Unsorted: {unsorted}")
print(f"Sorted: {selection_sort(unsorted)}")