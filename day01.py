with open('puzzle01.txt') as f:
    elves = [0]
    max1 = 0
    sum1 = 0
    for line in f:
        line = line.strip()
        if line != "":
            sum1 += int(line)
        else:
            elves.append(sum1)
            sum1 = 0
    for x in elves:
        if x > max1:
            max1 = x
    print("Part 1:", max1)
################################################################
    elves.sort(reverse=True)
    sum2 = elves[0]+elves[1]+elves[2]
    print("Part 2:", sum2)