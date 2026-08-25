def are_signs_alternating(numbers):
    for i in range(1, len(numbers)):
        pred_positive = numbers[i-1] >= 0
        curr_positive = numbers[i] >= 0
        
        if pred_positive == curr_positive:
            return False
        
    return True


numbers = [4, -3, 6, -1, 12, -23, 8, -13]

print(are_signs_alternating(numbers))