def is_sorted_ascending(numbers):
    for i in range(len(numbers) - 1):
        if numbers[i] > numbers[i+1]:
            return False
        
    return True


numbers = [3, 5, 8, 2]

print(is_sorted_ascending(numbers))