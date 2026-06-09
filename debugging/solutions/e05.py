def maximum(zahlen):
    max_wert = zahlen[0]
    
    for i in range(1, len(zahlen)):
        z = zahlen[i]
        
        if z > max_wert:
            max_wert = z
            
    return max_wert


print(maximum([-3, -7, -1]))