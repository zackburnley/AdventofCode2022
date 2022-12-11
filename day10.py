with open("puzzle10.txt") as f:
    cycle, valx, cinst = 0, 1, -1
    executing = False
    instructions = []
    specials = {20: 0, 60: 0, 100: 0, 140: 0, 180: 0, 220: 0}
    pixels = {0: [], 1: [], 2: [], 3: [], 4: [], 5: [], 6: []}
    for line in f:
        line = line.strip()
        instruction, value = line[:4], line[5:]
        if value:
            value = int(value)
        ituple = (instruction, value)
        instructions.append(ituple)
    while cycle > -1:
        cycle += 1
        row = cycle // 40
        if cycle % 40 == 0:
            row -= 1
        pixel = (cycle-1) % 40
        if abs(valx - pixel) in [0, 1]:
            pixels[row].append("#")
        else:
            pixels[row].append(".")
        if cycle in specials:
            specials[cycle] = cycle*valx
        if not executing:
            if cinst < len(instructions)-1:
                cinst += 1
            else:
                cycle = -1
                continue
            instruction, value = instructions[cinst][0], instructions[cinst][1]
        else:
            valx += value
            executing = False
            continue
        if instruction == "noop":
            continue
        else:
            executing = True
    print("Part 1:", sum(specials.values()))
    for key in pixels:
        print(pixels.get(key))