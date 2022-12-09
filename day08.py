with open("puzzle08.txt") as f:
    trees, count, treescores = [], 0, []
    for line in f:
        line = line.strip()
        trees.append(list(line))
    for i, e in enumerate(trees):
        for j, f in enumerate(e):
            trees[i][j] = int(f)
    for i, e in enumerate(trees):
        for j, f in enumerate(e):
            if i == 0 or i == len(trees)-1 or j == 0 or j == len(trees)-1:
                count += 1
            else:
                tree = "invis"
                us, ds, ls, rs = 0, 0, 0, 0
                r, c = i, j
                while r > 0:
                    r -= 1
                    us += 1
                    if trees[r][c] >= f:
                        r = -1
                    if r == 0:
                        tree = "vis"
                r, c = i, j
                while r < len(trees)-1:
                    r += 1
                    ds += 1
                    if trees[r][c] >= f:
                        r = len(trees)
                    if r == len(trees)-1:
                        tree = "vis"
                r, c = i, j
                while c > 0:
                    c -= 1
                    ls += 1
                    if trees[r][c] >= f:
                        c = -1
                    if c == 0:
                        tree = "vis"
                r, c = i, j
                while c < len(trees)-1:
                    c += 1
                    rs += 1
                    if trees[r][c] >= f:
                        c = len(trees)
                    if c == len(trees)-1:
                        tree = "vis"
                if tree == "vis":
                    count += 1
                treescore = us*ds*ls*rs
                treescores.append(treescore)
    print("Part 1:", count)
    treescores.sort(reverse=True)
    print("Part 2:", treescores[0])