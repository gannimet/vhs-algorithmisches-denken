def average_of_numbers(numbers):
    sum = 0
    count = len(numbers)
    
    for n in numbers:
        sum += n
    
    return sum / count


numbers = [3, 7, 4, 9, 10, 2]

print(average_of_numbers(numbers))