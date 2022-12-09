with open('puzzle04.txt') as f:
    count = 0
    for line in f:
        line = line.strip()
        temp = line.split(",")
        elf1 = temp[0].split("-")
        elf2 = temp[1].split("-")
        i = 0
        while i < len(elf1):
            elf1[i] = int(elf1[i])
            elf2[i] = int(elf2[i])
            i += 1
        if elf1[0] >= elf2[0] and elf1[1] <= elf2[1]:
            count += 1
        elif elf1[0] <= elf2[0] and elf1[1] >= elf2[1]:
            count += 1
    print("Part 1:", count)
#######################################################################
with open('puzzle04.txt') as f:
    count = 0
    for line in f:
        line = line.strip()
        temp = line.split(",")
        elf1 = temp[0].split("-")
        elf2 = temp[1].split("-")
        i = 0
        while i < len(elf1):
            elf1[i] = int(elf1[i])
            elf2[i] = int(elf2[i])
            i += 1
        if elf1[0] <= elf2[0] <= elf1[1]:
            count += 1
        elif elf2[0] <= elf1[0] <= elf2[1]:
            count += 1
    print("Part 2:", count)