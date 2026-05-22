def run_length_encode(text):
    if len(text) == 0:
        return ""
    
    last_char = text[0]
    current_length = 1
    result_str = ""
    
    for i in range(1, len(text)):
        current_char = text[i]
        
        if current_char == last_char:
            current_length += 1
        else:
            result_str += f"{last_char}{current_length}"
            current_length = 1
            last_char = current_char
            
    result_str += f"{last_char}{current_length}"
    
    return result_str


print(run_length_encode("aabccc"))