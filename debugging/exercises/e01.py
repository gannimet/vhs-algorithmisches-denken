def nur_gerade(zahlen):
    for z in zahlen:
        if z % 2 != 0:
            zahlen.remove(z)
            
    return zahlen

print(nur_gerade([1, 3, 5]))