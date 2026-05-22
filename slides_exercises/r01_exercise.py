def are_signs_alternating(numbers):
    if len(numbers) <= 1:
        return True
    
    is_current_element_positive = numbers[0] >= 0

    for i in range(1, len(numbers)):
        is_new_element_positive = numbers[i] >= 0
        
        if is_current_element_positive == is_new_element_positive:
            return False
        
        is_current_element_positive = is_new_element_positive
        
    return True


numbers = [4, -3, 6, -1, 12, -23, 8, -13]

print(are_signs_alternating(numbers))