with open('puzzle5.txt') as f:
    stacks = [
        [],
        ['R', 'G', 'H', 'Q', 'S', 'B', 'T', 'N'],
        ['H', 'S', 'F', 'D', 'P', 'Z', 'J'],
        ['Z', 'H', 'V'],
        ['M', 'Z', 'J', 'F', 'G', 'H'],
        ['T', 'Z', 'C', 'D', 'L', 'M', 'S', 'R'],
        ['M', 'T', 'W', 'V', 'H', 'Z', 'J'],
        ['T', 'F', 'P', 'L', 'Z'],
        ['Q', 'V', 'W', 'S'],
        ['W', 'H', 'L', 'M', 'T', 'D', 'N', 'C']
    ]
    msg=[]
    for line in f:
        line = line.split(" ")
        amt = int(line[1])
        source = int(line[3])
        dest = int(line[5])
        while not amt == 0:
            lelemindex = len(stacks[source]) - 1
            lelem = stacks[source][lelemindex]
            stacks[dest].append(lelem)
            stacks[source].pop(lelemindex)
            amt -= 1
    i = 1
    while i <= 9:
        msg.append(stacks[i][len(stacks[i]) - 1])
        i += 1
    print("Part 1:", msg)
######################################################################
with open('puzzle5.txt') as f:
    stacks = [
        [],
        ['R', 'G', 'H', 'Q', 'S', 'B', 'T', 'N'],
        ['H', 'S', 'F', 'D', 'P', 'Z', 'J'],
        ['Z', 'H', 'V'],
        ['M', 'Z', 'J', 'F', 'G', 'H'],
        ['T', 'Z', 'C', 'D', 'L', 'M', 'S', 'R'],
        ['M', 'T', 'W', 'V', 'H', 'Z', 'J'],
        ['T', 'F', 'P', 'L', 'Z'],
        ['Q', 'V', 'W', 'S'],
        ['W', 'H', 'L', 'M', 'T', 'D', 'N', 'C']
    ]
    msg = []
    for line in f:
        line = line.split(" ")
        amt = int(line[1])
        source = int(line[3])
        dest = int(line[5])
        slen = len(stacks[source])
        temp = stacks[source][slen-amt:slen]
        i = 0
        while i < len(temp):
            stacks[dest].append(temp[i])
            i += 1
        while not amt == 0:
            stacks[source].pop(slen-1)
            slen = len(stacks[source])
            amt -= 1
    i = 1
    while i <= 9:
        msg.append(stacks[i][len(stacks[i]) - 1])
        i += 1
    print("Part 2:", msg)