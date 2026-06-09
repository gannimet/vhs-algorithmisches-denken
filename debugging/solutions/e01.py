def nur_gerade(zahlen):
    gerade_zahlen = []
    
    for z in zahlen:
        if z % 2 == 0:
            gerade_zahlen.append(z)
            
    return gerade_zahlen

print(nur_gerade([1, 3, 5]))