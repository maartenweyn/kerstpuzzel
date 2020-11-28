import math
import copy

input = [[0,0,6, 0,0,0, 0,0,0], [0,0,0, 0,0,0, 0,4,0], [1,0,9, 0,0,0, 0,0,0], [0,8,0, 0,0,0, 0,3,0], [0,0,2, 5,0,1, 4,0,0], [3,4,0, 8,0,7, 0,0,0], [0,0,0, 0,6,0, 0,0,7], [0,3,0, 0,5,0, 0,0,1], [4,0,0, 0,0,1, 0,0,9]]

def findNextCellToFill(grid, i, j):
        for x in range(i,len(grid)):
                for y in range(j,len(grid[x])):
                        if grid[x][y] == 0:
                                return x,y
        for x in range(0,len(grid)):
                for y in range(0,len(grid[x])):
                        if grid[x][y] == 0:
                                return x,y
        return -1,-1



def isValidSudoku(grid, i, j, e):
        squareOk = all([e != grid[i][x] for x in range(9)])
        if squareOk:
                r = int(math.floor(j/3))
                c = j % 3

                rowOk = True
                columnOk = True

                ii = int(math.floor(i/3))

                if (i == 0) or (i == 1) or  (i == 2):
                        rowOk     = all([e != grid[ii*3][(r*3)+x] for x in range(3)]) and all([e != grid[ii*3+1][(r*3)+x] for x in range(3)]) and all([e != grid[ii*3+2][ r*3 + x ] for x in range(3)])

                if (i == 0) or (i == 7) or  (i == 5):        
                         columnOk = all([e != grid[0][c+(x*3)]    for x in range(3)]) and all([e != grid[7][c+ (x*3)]     for x in range(3)]) and all([e != grid[5][c+ (x*3)]     for x in range(3)])

                if (i == 3) or (i == 1) or  (i == 8):        
                         columnOk = all([e != grid[3][c+(x*3)] for x in range(3)]) and all([e != grid[1][c+ (x*3)] for x in range(3)]) and all( [e != grid[8][c+ (x*3)] for x in range(3)])
                
                if (i == 6) or (i == 4) or  (i == 2):        
                         columnOk = all([e != grid[6][c+(x*3)] for x in range(3)]) and all([e != grid[4][c+ (x*3)] for x in range(3)]) and all( [e != grid[2][c+ (x*3)] for x in range(3)])

                if rowOk and columnOk:
                        return True
        
        return False

def findoptions(grid):
        options = []
        nr_options = 0
        for i in range (0, len(grid)):
                sq_options = []
                for j in range (0, len(grid[i])):
                        cell_options = []
                        if (grid[i][j] == 0):
                                for e in range(1,10):
                                        if isValidSudoku(grid,i,j,e):
                                                cell_options.append(e)
                        else:
                                cell_options.append(grid[i][j])
                        if (len(cell_options) > 1):
                                nr_options += len(cell_options)
                        sq_options.append(cell_options)
                options.append(sq_options)
        print("nr of options", math.pow(10, nr_options))
        return options


count = 0
options = []
solve_size = 2

def solveSudokuTrial(grid,  i=0, j=0):
        global count
        i,j = findNextCellToFill(grid, i, j)
        count += 1
        # if (count % 1000000 == 0):
        #         print (count/1000000)
        if i == -1:
                return True
        #for e in range(1,10):
        for e in options[i][j]:
                if isValidSudoku(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudokuTrial(grid, i, j):
                                print("Found Solution: ", grid, grid[1][1], grid[8][6], grid[4][5])
                                # return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False

def solveSudoku(grid, i=0, j=0):
        global count
        global options

        if (count == 0):
                options = findoptions(grid)
                print(options)

        prev_i = 0
        prev_j = 0
        found = False


        min_length = 10
        min_i = -1
        min_j = -1

        while (not found and min_i != prev_i and min_j != prev_j):
                for i in range (0, len(options)):
                        for j in range (0, len(options[i])):
                                # print(i, j, len(options[i][j]), min_length, min_i, min_j)
                                if (len(options[i][j]) > 1 and len(options[i][j]) < min_length):
                                        min_length = len(options[i][j]) 
                                        min_i = i
                                        min_j = j
                if min_i == -1:
                        return solveSudokuTrial(grid)

                for e in options[min_i][min_j]:
                        test_grid = copy.deepcopy(grid)
                        test_grid[min_i][min_j] = e
                        print("testing ", min_i, min_j, options[min_i][min_j], e)
                        test = solveSudokuTrial(test_grid)
                        if not test:
                                options[min_i][min_j].remove(e)

                                print(options)

                if (len(options[min_i][min_j]) == 1):
                        grid[min_i][min_j] = e
                        print("NE grid ", grid)
                
                if len(options[min_i][min_j] == 0):
                        print ("ERROR CAN NOT SOLVE THIS SUDOKU")
                        return False


input[0][7] = 8
input[1][8] = 1
input[2][6] = 5

solveSudoku(input)
