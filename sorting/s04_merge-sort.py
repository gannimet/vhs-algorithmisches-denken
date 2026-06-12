import random

def split(items):
    split_index = len(items) // 2

    return (items[:split_index], items[split_index:])

def merge(left_list, right_list):
    merged_list = []
    left_index, right_index = 0, 0

    while left_index < len(left_list) and right_index < len(right_list):
        l = left_list[left_index]
        r = right_list[right_index]

        if l <= r:
            merged_list.append(l)
            left_index += 1
        else:
            merged_list.append(r)
            right_index += 1

    merged_list += left_list[left_index:]
    merged_list += right_list[right_index:]

    return merged_list

def merge_sort(items):
    if len(items) <= 1:
        return items
    
    (left_list, right_list) = split(items)
    
    return merge(merge_sort(left_list), merge_sort(right_list))


all_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
unsorted = random.sample(all_numbers, 9)
print(f"Unsorted: {unsorted}")
print(f"Sorted: {merge_sort(unsorted)}")