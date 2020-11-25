import math

inputQuasidoku = [[2,0,0,0,0,3,0,0,0],[8,1,0,0,6,0,2,0,0],[0,0,0,0,0,9,3,5,0], [7,0,0,0,0,0,8,0,0], [0,0,8,1,0,0,0,0,2], [0,0,4,0,0,0,9,3,0]]



def findNextCellToFill(grid, i, j):
        for x in range(i,len(grid)):
                for y in range(0,len(grid[x])):
                        # print (x, y, "==", grid[x][y])
                        if grid[x][y] == 0:
                                # print (x, y, "==0")
                                return x,y
        for x in range(0,len(grid)):
                for y in range(0,len(grid[x])):
                        # print (x, y, "==", grid[x][y])
                        if grid[x][y] == 0:
                                # print (x, y, "==0")
                                return x,y
        return -1,-1

def isValidRegular(grid, i, j, e):
        rowOk = all([e != grid[i][x] for x in range(9)])
        if rowOk:
                columnOk = all([e != grid[x][j] for x in range(9)])
                if columnOk:
                        # finding the top left x,y co-ordinates of the section containing the i,j cell
                        secTopX, secTopY = 3 *(i//3), 3 *(j//3) #floored quotient should be used here. 
                        for x in range(secTopX, secTopX+3):
                                for y in range(secTopY, secTopY+3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def isValidQuasidoku(grid, i, j, e):
        print("isvalid?", i, j, e, [e != grid[i][x] for x in range(9)])
        squareOk = all([e != grid[i][x] for x in range(9)])
        if squareOk:
                r = int(math.floor(j/3))
                c = j % 3

                rowOk = True
                columnOk = True

                if (i == 0) or (i == 1):
                        print("row r/c", r, c, [[e != grid[0][(r*3)+x] for x in range(3)], [e != grid[1][(r*3)+x] for x in range(3)], [e != grid[2][(2-r) + (x*3)] for x in range(3)]])
                        rowOk = all([e != grid[0][(r*3)+x] for x in range(3)]) and all([e != grid[1][(r*3)+x] for x in range(3)]) and  all([e != grid[2][(2-r) + (x*3)] for x in range(3)])
                if (i == 3) or (i == 4) or (i == 2):
                        print("row r/c", r, c, [[e != grid[3][(r*3)+x] for x in range(3)], [e != grid[4][(r*3)+x] for x in range(3)], [e != grid[2][(r*3) + (x)] for x in range(3)]])
                        rowOk = all([e != grid[3][(r*3)+x] for x in range(3)]) and all([e != grid[4][(r*3)+x] for x in range(3)]) and all([e != grid[2][(r*3) + (x)] for x in range(3)])
                if (i == 5):
                        rowOk = all([e != grid[0][(2-r)+(x*3)] for x in range(3)]) and all([e != grid[3][(2-r)+ (x*3)] for x in range(3)]) and all( [e != grid[5][(r*3) + (x)] for x in range(3)])

                if (i == 0) or (i == 3):        
                        print("col r/c", r, c, [[e != grid[0][c+(x*3)] for x in range(3)], [e != grid[3][c+ (x*3)] for x in range(3)], [e != grid[5][(2-c)*3 + (x)] for x in range(3)]])
                        columnOk = all([e != grid[0][c+(x*3)] for x in range(3)]) and all([e != grid[3][c+ (x*3)] for x in range(3)],) and all( [e != grid[5][(2-c)*3 + (x)] for x in range(3)])
                if (i == 1) or (i == 4) or (i == 5):
                        print("col r/c", r, c, [[e != grid[1][c+(x*3)] for x in range(3)], [e != grid[4][c+ (x*3)] for x in range(3)], [e != grid[5][c+ (x*3)] for x in range(3)]])
                        columnOk = all([e != grid[1][c+(x*3)] for x in range(3)]) and all( [e != grid[4][c+ (x*3)] for x in range(3)]) and all( [e != grid[5][c+ (x*3)] for x in range(3)])
                if (i == 2):
                        columnOk = all([e != grid[0][(2-c)*3+x] for x in range(3)]) and all( [e != grid[1][(2-c)*3+x] for x in range(3)]) and all( [e != grid[2][(c*3) + (x)] for x in range(3)])

                if rowOk and columnOk:
                        return True
        return False

def solveSudoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValidQuasidoku(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudoku(grid, i, j):
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False

ret = solveSudoku(inputQuasidoku)
print (ret, inputQuasidoku)