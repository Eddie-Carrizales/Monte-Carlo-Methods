import numpy as np
import random as rand


def treesTotal(data):
    total = 0
    for item1 in data:
        for item2 in item1:
            total = total + item2
    return total


def treeCombine(dataA, dataB):
    numrows = len(dataA)
    numcols = len(dataA[0])
    result = zeros(numrows, numcols)

    for i in range(numrows):
        for j in range(numcols):
            result[i][j] = dataA[i][j] or dataB[i][j]

    return result


def treeCopy(data):
    rowA = []
    colA = []
    colA = []
    for item1 in data:
        rowA = []
        for item2 in item1:
            rowA.append(item2)
        colA.append(rowA)
    return colA


def displayWork(data):
    for item1 in data:
        for item2 in item1:
            if item2 == 1:
                print("🔥", end="")
            elif item2 == 0:
                print("🌳", end="")
            else:
                print(item2, end="")
        print()
    print("-----------")


def zeros(rows, cols):
    return np.zeros((rows, cols))


def forestFire(display):
    height = 20
    width = 50
    prob_north = 0.3
    prob_south = 0.3
    prob_east = 0.3
    prob_west = 0.8

    Trees = zeros(height, width)
    Trees[0][0] = 1

    oldTrees = treeCopy(Trees)
    animation = list()

    oldTrees = treeCopy(Trees)
    looper = treesTotal(oldTrees)
    while (looper > 0):

        newTrees = zeros(height, width)
        for row in range(0, height):
            for col in range(0, width):

                if (oldTrees[row][col] == 1):
                    check = 0
                else:
                    check = 1

                if (col > 0):
                    if (oldTrees[row][col - 1] > 0):
                        test = (rand.random() < prob_west)
                        if (test):
                            newTrees[row][col] = check

                if (row > 0):
                    if (oldTrees[row - 1][col] > 0):

                        test = (rand.random() < prob_north)
                        if (test):
                            newTrees[row][col] = check

                if (row < height - 1):
                    if (Trees[row + 1][col] > 0):
                        test = (rand.random() < prob_south)
                        if (test):
                            newTrees[row][col] = check

                if (col < width - 1):
                    if (oldTrees[row][col + 1] > 0):

                        test = (rand.random() < prob_east)
                        if (test):
                            newTrees[row][col] = check

        oldTrees = treeCombine(oldTrees, newTrees)
        looper = treesTotal(newTrees)
        if (display):
            animation.append(oldTrees)

    if (display):
        fcount = (len(animation))
        key = ''
        for i in range(0, fcount):
            displayWork(animation[i])
            key = input()

    return oldTrees


def monteCarlo():
    N = 30
    N_burned_trees = [0] * N
    Corner_burned = [0] * N

    for running in range(0, N):

        Burning_Trees = forestFire(False)

        total = treesTotal(Burning_Trees)
        N_burned_trees[running] = total
        if (Burning_Trees[0][49] == 1):
            Corner_burned[running] = 1

    min_burned_trees = np.min(N_burned_trees)
    max_burned_trees = np.max(N_burned_trees)
    E_burned_trees = np.mean(N_burned_trees)
    STD_burned_trees = np.std(N_burned_trees)
    E_burned_house = np.mean(Corner_burned)

    tally = [0] * N
    ThirtyPercent = 50 * 20 * 0.30
    for loop1 in range(0, N):
        if (N_burned_trees[loop1] > ThirtyPercent):
            tally[loop1] = 1
        else:
            tally[loop1] = 0
    P_burn_30pct = np.mean(tally)

    tally2 = [0] * N
    for loop1 in range(0, N):
        diff = abs(E_burned_trees - N_burned_trees[loop1])
        if (25 < diff):
            tally2[loop1] = 1
        else:
            tally2[loop1] = 0

    P_differ_by_25 = np.mean(tally2)

    print("Minimum burnt trees: %d" % (min_burned_trees))
    print("Maximum burnt trees: %d" % (max_burned_trees))
    print("Average burnt trees: %5.3f." % (E_burned_trees))
    print("Standard Deviation : %5.3f." % (STD_burned_trees))

    print("Probability house catches fire is %5.3f." % (E_burned_house))

    print("Probability that the actual number of affected trees differs from the estimator by more than 25 trees: ",
          end='')
    print("%d" % (P_differ_by_25))

    print("Probability that 30%% of the forest will be burning: %f" % (P_burn_30pct))

    return

# Comment out forestFire(True) to stop seeing the forest and just see the monteCarlo result.
# Pressing Enter key will show next frame of the forest burning.
forestFire(True)

monteCarlo()
