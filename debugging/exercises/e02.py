def umkehren(wort):
    ergebnis = ""
    
    for i in range(len(wort), 0, -1):
        ergebnis += wort[i]
    
    return ergebnis


print(umkehren("Hallo"))