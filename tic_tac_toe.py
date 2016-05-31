import random

chars = ["X", "O", "-"]

def randomizeBoard(board):
    for i in range(0,len(board[0])):
        for j in range(0,len(board)):
            board[i][j] = random.choice(chars)

def checkBoard(board):
    N = len(board)
    pathStatuses = []

    # ensure it's a square board
    if len(board[0]) != N:
        raise Exception("different number of rows than columns :(")

    for i in range(0, N):
        # Check all horizontal paths
        pathStatuses.append(checkPath(board, range(i, i), range(0, N)))
        # Check all vertical paths
        pathStatuses.append(checkPath(board, range(0, N), range(i, i))) 
        # Check all diagonal paths
        pathStatuses.append(checkPath(board, range(i, i), range(i, i))) 

    print(pathStatuses)

# assume board cell has:
# X for Xs and 
# O for Os
# - for Empty
#returns -1 if game still in progress
#returns 1 if X won
#returns 2 if O won
#returns 0 if stalemate 
def checkPath(board, rowRange, colRange):
    items = []
    if len(rowRange) == 0:
        # horizontal check
        row = rowRange.start
        for col in colRange:
            items.append(board[row][col])
        return pathStatus(items)

    elif len(colRange) == 0:
        # vertical check
        col = colRange.start
        for row in rowRange:
            items.append(board[row][col])
        print("Path: {0}\tStatus: {1}".format(items, pathStatus(items)))
    elif rowRange == colRange:
        # diagonal check
        for i in rowRange:
            items.append(board[i][i])
        print("Path: {0}\tStatus: {1}".format(items, pathStatus(items)))
    else:
        raise Exception("incorrect ranges!")

def pathStatus(items):
    # if the items contain only one type of mark
    if len(set(items)) == 1:
        # get that mark, return the result.
        mark = items[0]
        if mark == "X":
            # player X wins
            return 0
        elif mark == "O":
            # player O wins
            return 1
        else:
            # game still in play
            return -1
    else:
        # check for stalemate
        if "-" not in items:
            # return stalemate status for this path
            return 2
        else:
            # there are still moves to be made
            return -1
