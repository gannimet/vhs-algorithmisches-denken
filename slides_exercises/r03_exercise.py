coins = [2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

def give_change(amount):
    remaining_amount = amount
    change_map = {}
    
    for coin in coins:
        how_often = remaining_amount // coin
        remaining_amount = round(remaining_amount % coin, 2)
        change_map[coin] = int(how_often)
        
    return change_map


change = give_change(0.73)

for coin in change:
    how_often = change[coin]
    
    if how_often > 0:
        print(f"{how_often} x {coin} €")