def group_words(words):
    grouped_words = {}
    
    for word in words:
        start_letter = word[0].lower()
        
        if start_letter in grouped_words:
            grouped_words[start_letter] += [word]
        else:
            grouped_words[start_letter] = [word]
            
    return grouped_words


print(group_words(["Apfel", "Banane", "Ananas", "Birne", "Mango", "Pfirsich"]))