def zaehle(text, buchstabe):
    anzahl = 0
    
    for b in text:
        if b == buchstabe:
            anzahl += 1
            
        return anzahl
    

print(zaehle("programmieren", "r"))