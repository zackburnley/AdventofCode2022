with open('puzzle2.txt') as f:
    opponent = ""
    me = ""
    score1 = 0
    for line in f:
        line = line.strip()
        opponent = line[0]
        me = line[2]
        if (opponent == "A"):#rock
            if (me=="X"):
                score1 += 4
            elif (me=="Y"):
                score1 += 8
            else:
                score1 += 3
        elif (opponent == "B"):#paper
            if (me == "X"):
                score1 += 1
            elif (me == "Y"):
                score1 += 5
            else:
                score1 += 9
        else:#scissors
            if (me=="X"):
                score1 += 7
            elif (me=="Y"):
                score1 += 2
            else:
                score1 += 6
    print("Part 1:", score1)
#####################################################################
with open('puzzle2.txt') as g:
    opponent = ""
    me = ""
    score2 = 0
    for line in g:
        line = line.strip()
        opponent = line[0]
        me = line[2]
        if(opponent=="A"):#rock
            if(me=="X"):#loss
                score2 += 3
            elif(me == "Y"):#draw
                score2 += 4
            else:#win
                score2 += 8
        elif(opponent=="B"):#paper
            if(me=="X"):#loss
                score2 += 1
            elif(me == "Y"):#draw
                score2 += 5
            else:#win
                score2 += 9
        elif (opponent == "C"):#scissors
            if (me == "X"):#loss
                score2 += 2
            elif (me == "Y"):#draw
                score2 += 6
            else:#win
                score2 += 7
    print("Part 2:", score2)