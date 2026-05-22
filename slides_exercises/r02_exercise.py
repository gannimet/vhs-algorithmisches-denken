def most_frequent_character(text):
    lower_text = text.lower()
    word_counter = {}
    
    for c in lower_text:
        if c in word_counter:
            word_counter[c] += 1
        else:
            word_counter[c] = 1
            
    record_character = None
    record_frequency = 0
    
    for c in word_counter:
        if word_counter[c] > record_frequency:
            record_frequency = word_counter[c]
            record_character = c
            
    return record_character


text = "Abschlussbegutachtungsbeschluss"

print(most_frequent_character(text))