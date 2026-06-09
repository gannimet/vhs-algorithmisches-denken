def maximum(zahlen):
    max_wert = 0
    
    for z in zahlen:
        if z > max_wert:
            max_wert = z
            
    return max_wert


print(maximum([-3, -7, -1]))