import numpy as np

defaultSudoku=[[5,3,0,0,7,0,0,0,0],
               [6,0,0,1,9,5,0,0,6],
               [0,9,8,0,0,0,0,6,0],
               [8,0,0,0,6,0,0,0,3],
               [4,0,0,8,0,3,0,0,1],
               [7,0,0,0,2,0,0,0,6],
               [0,6,0,0,0,0,2,8,0],
               [0,0,0,4,1,9,0,0,5],
               [0,0,0,0,8,0,0,7,9]]
#board= np.matrix(defaultSudoko)
#print(board)

def Overallpossibility(row,col,num):
    global defaultSudoku
    for i in range(0,9):
        if defaultSudoku[row][i] == num:
            return False
    for i in range(0,9):
        if defaultSudoku[i][col] == num:
            return False
    x0 = (row // 3) * 3
    y0 = (col // 3) * 3
    for i in range(0, 3):
        for j in range(0, 3):
            if defaultSudoku[y0 + i][x0 + j] == num:
                return False
    return True


def  Solve():
    global defaultSudoko
    for row in range(0,9):
        for column in range(0,9):
            if defaultSudoku[row][column] == 0:
                for number in range(1,10):
                    if Overallpossibility(row,column,number):
                        defaultSudoku[row][column] = number
                        Solve()
                        defaultSudoku[row][column]=0
                #return

    print(np.matrix(defaultSudoku))
    input("More?")




Solve()





