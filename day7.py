with open('puzzle7.txt') as f:
    dirs = {"/": {"parentDir": "",
                  "files": {},
                  "childDirs": [],
                  "dirSize": 0}}
    currentDir = "/"
    for line in f:
        line = line.strip()
        line = list(line)
        dirname = ""
        if line[0:3] == ["d", "i", "r"]:
            temp = line[4:]
            for c in temp:
                dirname += c
            tempPdir = dirs[currentDir]["parentDir"]
            dirname = currentDir + "/" + dirname
            while not tempPdir == "":
                dirname = tempPdir + dirname
                tempPdir = dirs[tempPdir]["parentDir"]
            dirs.update({dirname: {"parentDir": currentDir,
                                   "files": {},
                                   "childDirs": [],
                                   "dirSize": 0}})
            dirs[currentDir]["childDirs"].append(dirname)
        elif line[0] == "$":
            if line[2:4] == ["c", "d"]:
                if line[5:7] == [".", "."]:
                    currentDir = dirs[currentDir].get("parentDir")
                else:
                    temp, cdDirName = line[5:],  ""
                    for c in temp:
                        cdDirName += c
                    for e in dirs[currentDir]["childDirs"]:
                        if cdDirName in e:
                            currentDir = e
                            break
        else:
            fileName, fileSize = "", ""
            for i, c in enumerate(line):
                if c == " ":
                    temp = line[i+1:]
                    for d in temp:
                        fileName += d
                    break
                fileSize += c
            fileSize = int(fileSize)
            dirs[currentDir]["files"].update({fileName: fileSize})
            dirs[currentDir]["dirSize"] += fileSize
            pDir = dirs[currentDir]["parentDir"]
            while not pDir == "":
                dirs[pDir]["dirSize"] += fileSize
                pDir = dirs[pDir]["parentDir"]
    totalSize = 0
    for d in dirs:
        if dirs[d]["dirSize"] <= 100000:
            totalSize += dirs[d]["dirSize"]
    print("Part 1:", totalSize)
    remainingMem = 70000000 - dirs["/"]["dirSize"]
    reqdMem = 30000000 - remainingMem
    dirCands = []
    for d in dirs:
        if dirs[d]["dirSize"] >= reqdMem:
            dirCands.append(dirs[d]["dirSize"])
    dirCands.sort()
    print("Part 2:", dirCands[0])