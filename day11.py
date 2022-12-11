with open("puzzle11.txt") as f:
    divisors = []
    monkeys = {0: {"items": [], "oNum2": 0, "operator": "+", "testDiv": 1, "tThrow": 0, "fThrow": 0, "inspections": 0},
               1: {"items": [], "oNum2": 0, "operator": "+", "testDiv": 1, "tThrow": 0, "fThrow": 0, "inspections": 0},
               2: {"items": [], "oNum2": 0, "operator": "+", "testDiv": 1, "tThrow": 0, "fThrow": 0, "inspections": 0},
               3: {"items": [], "oNum2": 0, "operator": "+", "testDiv": 1, "tThrow": 0, "fThrow": 0, "inspections": 0},
               4: {"items": [], "oNum2": 0, "operator": "+", "testDiv": 1, "tThrow": 0, "fThrow": 0, "inspections": 0},
               5: {"items": [], "oNum2": 0, "operator": "+", "testDiv": 1, "tThrow": 0, "fThrow": 0, "inspections": 0},
               6: {"items": [], "oNum2": 0, "operator": "+", "testDiv": 1, "tThrow": 0, "fThrow": 0, "inspections": 0},
               7: {"items": [], "oNum2": 0, "operator": "+", "testDiv": 1, "tThrow": 0, "fThrow": 0, "inspections": 0}}
    mID = "0"
    for line in f:
        line = line.strip()
        line = line.split(" ")
        if len(line) == 1:
            continue
        if line[0] == "Monkey":
            mID = line[1]
            mID = mID[:1]
            mID = int(mID)
        elif line[0] == "Starting":
            items = line[2:]
            for item in items:
                item = item[:2]
                item = int(item)
                monkeys[mID]["items"].append(item)
        elif line[0] == "Operation:":
            operator = line[4]
            oNum2 = line[5]
            monkeys[mID]["operator"] = operator
            monkeys[mID]["oNum2"] = oNum2
        elif line[0] == "Test:":
            testDiv = line[3]
            monkeys[mID]["testDiv"] = int(testDiv)
            divisors.append(int(testDiv))
        elif line[1] == "true:":
            tThrow = line[5]
            monkeys[mID]["tThrow"] = int(tThrow)
        elif line[1] == "false:":
            fThrow = line[5]
            monkeys[mID]["fThrow"] = int(fThrow)
    mRound = 1
    while not mRound == 10001:
        for monkey in monkeys:
            if not len(monkeys[monkey]["items"]) == 0:
                while len(monkeys[monkey]["items"]) > 0:
                    monkeys[monkey]["inspections"] += 1
                    item = monkeys[monkey]["items"][0]
                    cItem = item
                    num2 = monkeys[monkey]["oNum2"]
                    if monkeys[monkey]["operator"] == "+":
                        if num2 == "old":
                            cItem = cItem + cItem
                        else:
                            num2 = int(num2)
                            cItem = cItem + num2
                    else:
                        if num2 == "old":
                            cItem = cItem * cItem
                        else:
                            num2 = int(num2)
                            cItem = cItem * num2
                    #cItem = cItem // 3
                    lcm = 1
                    for div in divisors:
                        lcm *= div
                    cItem = cItem % lcm
                    if cItem % monkeys[monkey]["testDiv"] == 0:
                        throwTo = monkeys[monkey]["tThrow"]
                        monkeys[throwTo]["items"].append(cItem)
                        monkeys[monkey]["items"].pop(0)
                    else:
                        throwTo = monkeys[monkey]["fThrow"]
                        monkeys[throwTo]["items"].append(cItem)
                        monkeys[monkey]["items"].pop(0)
        mRound += 1
    inspectionList = []
    for monkey in monkeys:
        inspectionList.append(monkeys[monkey]["inspections"])
    inspectionList.sort(reverse=True)
    print("Part 2:", inspectionList[0]*inspectionList[1])