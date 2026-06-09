def has_at_least_8_characters(password):
    return len(password) >= 8

def contains_uppercase_character(password):
    for char in password:
        if char.isupper():
            return True
        
    return False

def contains_lowercase_character(password):
    for char in password:
        if char.islower():
            return True
        
    return False

def contains_number(password):
    for char in password:
        if char.isnumeric():
            return True
        
    return False

def is_password_safe(password):
    return (
        has_at_least_8_characters(password) and
        contains_uppercase_character(password) and
        contains_lowercase_character(password) and
        contains_number(password)
    )
    
    
print(is_password_safe("GP$6?AU25"))