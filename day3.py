with open('puzzle3.txt') as f:
    sum, prio = 0, 0
    for line in f:
        line = line.strip()
        mid = int(len(line)/2)
        fhalf = line[:mid]
        shalf = line[mid:]
        for c in fhalf:
            if c in shalf:
                prio = ord(c)
                if prio >= 97:#lowercase
                    prio -= 96
                else:#uppercase
                    prio -= 38
                sum += prio
                break
    print("Part 1:", sum)
############################################################################
with open('puzzle3.txt') as g:
    count, sum2, = 1, 0
    elf1, elf2, elf3 = "", "", ""
    for line in g:
        line = line.strip()
        if count == 1:
            elf1 = line
            count += 1
        elif count == 2:
            elf2 = line
            count += 1
        elif count == 3:
            elf3 = line
            for c in elf1:
                if c in elf2:
                    if c in elf3:
                        prio = ord(c)
                        if prio >= 97:#lowercase
                            prio -= 96
                        else:#uppercase
                            prio -= 38
                        sum2 += prio
                        count = 1
                        break
    print("Part 2:", sum2)