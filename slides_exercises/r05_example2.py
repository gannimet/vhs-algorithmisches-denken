def biggest_of_three(a, b, c):
    if a > b and a > c:
        return a
    
    if b > c:
        return b
    
    return c


print(biggest_of_three(2, 4, 6))