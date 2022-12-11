with open("puzzle09.txt") as f:
    hx, hy, tx, ty = 0, 0, 0, 0
    visited = {(0, 0)}
    for line in f:
        line = line.strip()
        direction, amount = line.split(" ")
        amount = int(amount)
        while amount > 0:
            if direction == "R":
                hx += 1
                if abs(hx - tx) > 1 and hy - ty == 0:
                    tx += 1
                    ttuple = (tx, ty)
                    visited.add(ttuple)
                elif abs(hx - tx) > 1 and hy - ty == 1:
                    tx += 1
                    ty += 1
                    ttuple = (tx, ty)
                    visited.add(ttuple)
                elif abs(hx - tx) > 1 and hy - ty == -1:
                    tx += 1
                    ty -= 1
                    ttuple = (tx, ty)
                    visited.add(ttuple)
            elif direction == "L":
                hx -= 1
                if abs(hx - tx) > 1 and hy - ty == 0:
                    tx -= 1
                    ttuple = (tx, ty)
                    visited.add(ttuple)
                elif abs(hx - tx) > 1 and hy - ty == 1:
                    tx -= 1
                    ty += 1
                    ttuple = (tx, ty)
                    visited.add(ttuple)
                elif abs(hx - tx) > 1 and hy - ty == -1:
                    tx -= 1
                    ty -= 1
                    ttuple = (tx, ty)
                    visited.add(ttuple)
            elif direction == "U":
                hy += 1
                if abs(hy - ty) > 1 and hx - tx == 0:
                    ty += 1
                    ttuple = (tx, ty)
                    visited.add(ttuple)
                elif abs(hy - ty) > 1 and hx - tx == 1:
                    ty += 1
                    tx += 1
                    ttuple = (tx, ty)
                    visited.add(ttuple)
                elif abs(hy - ty) > 1 and hx - tx == -1:
                    tx -= 1
                    ty += 1
                    ttuple = (tx, ty)
                    visited.add(ttuple)
            elif direction == "D":
                hy -= 1
                if abs(hy - ty) > 1 and hx - tx == 0:
                    ty -= 1
                    ttuple = (tx, ty)
                    visited.add(ttuple)
                elif abs(hy - ty) > 1 and hx - tx == 1:
                    ty -= 1
                    tx += 1
                    ttuple = (tx, ty)
                    visited.add(ttuple)
                elif abs(hy - ty) > 1 and hx - tx == -1:
                    ty -= 1
                    tx -= 1
                    ttuple = (tx, ty)
                    visited.add(ttuple)
            amount -= 1
    print("Part 1:", len(visited))