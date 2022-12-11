with open("puzzle09.txt") as f:
    visited = {(0, 0)}
    knots = {"H": (0, 0), "1": (0, 0), "2": (0, 0), "3": (0, 0), "4": (0, 0),
             "5": (0, 0), "6": (0, 0), "7": (0, 0), "8": (0, 0), "9": (0, 0)}
    for line in f:
        line = line.strip()
        direction, amount = line.split(" ")
        amount = int(amount)
        while amount > 0:
            
            amount -= 1