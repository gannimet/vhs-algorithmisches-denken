s = "LLWLLLWWWL"

land_counter = 0
is_land = False

for c in s:
    if c == "L":
        if not is_land:
            land_counter += 1
        is_land = True
    else:
        is_land = False
        
print(f"Result: {land_counter}")