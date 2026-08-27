def lookup_phone(phonebook, phone_number):
    for person in phonebook:
        phone_numbers = person["telefon"]
        
        if phone_number in phone_numbers:
            return person["name"]
        
    return None

people = [
    { "name": "Heinz", "telefon": ["12345"], "email": "heinz@example.com" },
    { "name": "Gabi", "telefon": ["4597683", "8735"], "email": "gabi@example.com" }
]

print(lookup_phone(people, "8735"))