import math
import copy
import multiprocessing 
import argparse
import sys

input  = [[0,0,1,0,0,0,0,7,0],[0,0,0,0,0,4,0,0,0],[7,0,0,2,8,0,0,6,0],[0,4,0,0,0,9,6,2,0],[0,0,0,0,0,0,0,0,2],[1,0,6,3,0,0,0,8,0],[0,5,8,1,0,0,0,0,0],[5,0,3,0,4,0,0,0,9],[0,0,0,0,3,5,0,0,0]]

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

                if (i == 0) or (i == 1)  or (i == 2):
                        rowOk = all ([e != grid[0][0+r*3], e != grid[0][1+r*3], e != grid[0][2+r*3], e != grid[1][0+r*3], e != grid[1][1+r*3], e != grid[1][2+r*3], e != grid[2][0+r*3], e != grid[2][1+r*3], e != grid[2][2+r*3]])
                if (i == 4) or (i == 5)  or (i == 7):
                        rowOk = all ([e != grid[4][0+r*3], e != grid[4][1+r*3], e != grid[4][2+r*3], e != grid[5][0+r*3], e != grid[5][1+r*3], e != grid[5][2+r*3], e != grid[7][0+r*3], e != grid[7][1+r*3], e != grid[7][2+r*3]])
                if (i == 3):
                        rowOk = all ([e != grid[0][2-r+0], e != grid[0][2-r+3], e != grid[0][2-r+6], e != grid[3][0+r*3], e != grid[3][1+r*3], e != grid[3][2+r*3], e != grid[2][r+0], e != grid[2][r+3], e != grid[2][r+6]])
                if (i==8) or (i==6):
                        rowOk = all ([e != grid[8][0+r*3], e != grid[8][1+r*3], e != grid[8][2+r*3], e != grid[6][0+r*3], e != grid[6][1+r*3], e != grid[6][2+r*3], e != grid[5][r+0], e != grid[5][r+3], e != grid[5][r+6]])
                
                if (i == 0) :
                        columnOk = all ([e != grid[0][c+0], e != grid[0][c+3], e != grid[0][c+6], e != grid[3][(2-c)*3+0], e != grid[3][(2-c)*3+1], e != grid[3][(2-c)*3+2], e != grid[2][(2-c)+0], e != grid[2][(2-c)+3], e != grid[2][(2-c)+6]])
                if (i == 2) :
                        columnOk = all ([e != grid[2][c+0], e != grid[2][c+3], e != grid[2][c+6], e != grid[3][(c)*3+1], e != grid[3][(c)*3+1], e != grid[3][(c)*3+2], e != grid[0][(2-c)+0], e != grid[0][(2-c)+3], e != grid[0][(2-c)+6]])

                if (i == 1) or (i == 3)  or (i == 8) :
                        columnOk = all ([e != grid[1][c+0], e != grid[1][c+3], e != grid[1][c+6], e != grid[3][c+0], e != grid[3][c+3], e != grid[3][c+6], e != grid[8][c+0], e != grid[8][c+3], e != grid[8][c+6]])

                if (i == 4) or (i == 6):
                        columnOk = all ([e != grid[4][c+0], e != grid[4][c+3], e != grid[4][c+6], e != grid[6][c+0], e != grid[6][c+3], e != grid[6][c+6], e != grid[7][2-c+0], e != grid[7][2-c+3], e != grid[7][2-c+6]])
                if (i == 7):
                        columnOk = all ([e != grid[4][2-c+0], e != grid[4][2-c+3], e != grid[4][2-c+6], e != grid[6][2-c+0], e != grid[6][2-c+3], e != grid[6][2-c+6], e != grid[7][c+0], e != grid[7][c+3], e != grid[7][c+6]])
                if (i == 5):
                        columnOk = all ([e != grid[5][c+0], e != grid[5][c+3], e != grid[5][c+6], e != grid[6][(c*3)+0], e != grid[6][(c*3)+1], e != grid[6][(c*3)+2], e != grid[8][(c*3)+0], e != grid[8][(c*3)+1], e != grid[8][(c*3)+2]])

                # if (i == 0) or (i == 1)  or (i == 2):
                #         rowOk = all([e != grid[0][(r*3)+x] for x in range(3)]) and all([e != grid[1][(r*3)+x] for x in range(3)]) and  all([e != grid[2][(r*3)+x] for x in range(3)])
                # if (i == 4) or (i == 5)  or (i == 7):
                #         rowOk = all([e != grid[4][(r*3)+x] for x in range(3)]) and all([e != grid[5][(r*3)+x] for x in range(3)]) and  all([e != grid[7][(r*3)+x] for x in range(3)])
                # if (i == 6) or (i == 8):
                #         rowOk = all([e != grid[8][(r*3)+x] for x in range(3)]) and all([e != grid[6][(r*3)+x] for x in range(3)]) and  all([e != grid[5][(r)+3*x] for x in range(3)])
                # if (i == 3):
                #         rowOk = all([e != grid[0][(2-r)+3*x] for x in range(3)]) and all([e != grid[3][(r*3)+x] for x in range(3)]) and  all([e != grid[2][(r)+3*x] for x in range(3)])

                # if (i == 0) :
                #         columnOk = all([e != grid[0][(c)+x*3] for x in range(3)]) and all([e != grid[3][(2-c)*3+x] for x in range(3)]) and  all([e != grid[2][(2-c)+3*x] for x in range(3)])
                # if (i == 2) :
                #         columnOk = all([e != grid[0][(2-c)+x*3] for x in range(3)]) and all([e != grid[3][(c)*3+x] for x in range(3)]) and  all([e != grid[2][(c)+3*x] for x in range(3)])
                # if (i == 1) or (i == 3)  or (i == 8):
                #         columnOk = all([e != grid[1][(c)+x*3] for x in range(3)]) and all([e != grid[3][(c)+x*3] for x in range(3)]) and  all([e != grid[8][(c)+3*x] for x in range(3)])
                # if (i == 4) or (i == 6)  or (i == 7):
                #         columnOk = all([e != grid[4][(c)+x*3] for x in range(3)]) and all([e != grid[6][(c)+x*3] for x in range(3)]) and  all([e != grid[7][(2-c)+3*x] for x in range(3)])
                # if (i == 5):
                #         columnOk = all([e != grid[5][(c)+x*3] for x in range(3)]) and all([e != grid[6][(c*3)+x] for x in range(3)]) and  all([e != grid[8][(c*3)+x] for x in range(3)])

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

def solveSudokuTrial(grid,  e, return_dic, options, solutions, i=0, j=0):     
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return_dic[e] = True
                return True
        #for e in range(1,10):
        for e in options[i][j]:
                if isValidSudoku(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudokuTrial(grid, e, return_dic, options, solutions, i, j):
                                print("Found Solution: ", grid, grid[2][4], grid[5][2], grid[8][5], grid[1][6], grid[7][6], grid[3][0])      
                                solution = grid[2][4] * 100000 + grid[5][2] * 10000 + grid[8][5] * 1000 + grid[1][6] * 100 + grid[7][6] * 10 +  grid[3][0]
                                if not solution in solutions:
                                        solutions.append(solution)
                                return_dic[e] = True
                                return_dic[e] = True
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        
        return_dic[e] = False
        return False

def solveSudoku(grid, i=0, j=0):
        global count
        global options

        if (count == 0):
                options_length = 0
                prev = -1
                while (prev != options_length):
                        prev = options_length
                        options = findoptions(grid)
                        options_length = 0
                        for i in range (0, len(options)):
                                for j in range (0, len(options[i])):
                                        options_length += len(options[i][j])

                        print(options_length, options)
                        for i in range (0, len(options)):
                                for j in range (0, len(options[i])):
                                        if (len(options[i][j]) == 1):
                                                grid[i][j] = options[i][j][0]

                        print("new grid", grid)

        processes = []
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        solutions = manager.list()


        #while (prev_length != min_length or min_i != prev_i or min_j != prev_j):
        for i in range (0, len(options)):
                for j in range (0, len(options[i])):
                        if (len(options[i][j]) > 1):
                                for e in options[i][j]:
                                        test_grid = copy.deepcopy(grid)
                                        test_grid[i][j] = e
                                        print("testing ", i, j, options[i][j], e)
                                        p = multiprocessing.Process(target=solveSudokuTrial, args=(test_grid,e, return_dict, options,solutions, 0, 0))
                                        #test = solveSudokuTrial(test_grid)
                                        processes.append(p)
                                        p.start()


                                for process in processes:
                                        process.join()
                                
                                        print("join")

                                print("JOIINED")
                                processes = []

                                for e in options[i][j]:
                                        if (return_dict.has_key(e)):
                                                print("return ", e, return_dict[e])
                                                if not return_dict[e]:
                                                        options[i][j].remove(e)
                                                        print("removed ", e, options)
                                        else:
                                                print ("cannot find key ", i, j, e, " in ", return_dict)

                                if (len(options[i][j]) == 1):
                                        grid[i][j] = options[i][j][0]
                                        print("NEW grid ", grid)
                                
                                if len(options[i][j]) == 0:
                                        print ("ERROR CAN NOT SOLVE THIS SUDOKU")
                                        return False

        print("trying last option")
        solveSudokuTrial(grid, 0, return_dict, options, solutions)
        
        print("solutions")
        for s in solutions:
                print(s)

def main(argv):

        parser = argparse.ArgumentParser(description='solve sudoke with 3 variables')
        parser.add_argument('-a', '--vara', default=8, type=int)
        parser.add_argument('-b', '--varb', default=6, type=int)
        parser.add_argument('-c', '--varc', default=5, type=int)
        parser.add_argument('-d', '--vard', default=0, type=int)
        parser.add_argument('-e', '--vare', default=0, type=int)
        parser.add_argument('-f', '--varf', default=0, type=int)

        args=parser.parse_args()
        input[2][4] = args.vara
        input[5][2] = args.varb
        input[8][5] = args.varc
        input[1][6] = args.vard
        input[7][6] = args.vare
        input[3][0] = args.varf

        solveSudoku(input)

if __name__ == "__main__":
   main(sys.argv[1:])