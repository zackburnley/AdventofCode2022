with open('puzzle6.txt') as f:
    for line in f:
        line = line.strip()
        line = list(line)
        i = 0
        while i < len(line)-13:
            sub = line[i:i+14]
            contents = {}
            for e in sub:
                contents[e] = contents.get(e, 0) + 1
            if len(contents) == 14:
                print(i+14)
                break
            i += 1