import math
import copy
import multiprocessing 
import argparse
import sys

input = [[0,0,2,0,0,5,1,0],[9,8,1,0,0,0,0,0],[0,0,0,0,0,0,3,6],[0,0,1,5,0,0,0,0],[0,0,0,0,0,0,0,1],[6,10,0,0,0,0,0,0],[0,0,0,0,0,0,0,10],[1,0,0,0,4,0,0,8,0],[0,0,0,4,0,7,0,0]]


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
        squareOk = all([e != grid[i][x] for x in range(len(grid[i]))])
        if squareOk:
                neighbourok = True

                ii = int(math.floor(i/3))

                
                if j == 4:
                        if (i % 3 < 2):
                                neighbourok =  all([e != grid[i+1][x] for x in range(8) if x != 3])
                if j == 7:
                        if (i < 6):
                            neighbourok =  all([e != grid[i+3][x] for x in range(8) if x != 0])

                if (j == 3):
                        if (i % 3 > 0):
                            neighbourok = all([e != grid[i-1][x] for x in range(8) if x != 4])

                if (j == 0):
                        if (i > 2):
                            neighbourok = all([e != grid[i-3][x] for x in range(8) if x != 7])

                if neighbourok:
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
        print("nr of options", nr_options)
        return options


count = 0
options = []
solve_size = 2

def solveSudokuTrial(grid,  e, return_dic, solutions, options, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return_dic[e] = True
                return True
        #for e in range(1,10):
        for e in options[i][j]:
                if isValidSudoku(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudokuTrial(grid, e, return_dic, solutions, options, i, j):
                                print("Found Solution: ", grid, grid[8][7], grid[0][7],grid[4][1],grid[2][3],grid[7][3], grid[1][5])
                                if (len(solutions) == 1):
                                        solutions.append([grid[2][3],grid[7][3], grid[1][5]])
                                else:
                                        found = False
                                        for sol in solutions:
                                                if ((sol[0] == grid[2][3]) and (sol[1] == grid[7][3]) and (sol[2] == grid[1][5])):
                                                        found = True
                                                        break
                                        
                                        if (not found):
                                                solutions.append([grid[2][3],grid[7][3], grid[1][5]])
                                
                                print(solutions)

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
                options = findoptions(grid)
                print(options)

        processes = []
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        solutions = manager.list()

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
                        p = multiprocessing.Process(target=solveSudokuTrial, args=(test_grid,e, return_dict, solutions, options,0, 0))
                        #test = solveSudokuTrial(test_grid)
                        processes.append(p)
                        p.start()

                for process in processes:
                        process.join()

                for e in options[min_i][min_j]:
                        print("return ", e, return_dict[e])
                        if not return_dict[e]:
                                options[min_i][min_j].remove(e)
                                print(options)

                if (len(options[min_i][min_j]) == 1):
                        grid[min_i][min_j] = e
                        print("NEW grid ", grid)
                
                if len(options[min_i][min_j]) == 0:
                        print ("ERROR CAN NOT SOLVE THIS SUDOKU")
                        return False

        print("solutions", solutions)
        for sol in solutions:
                print("JKL", sol)

def main(argv):

        parser = argparse.ArgumentParser(description='solve sudoke with 3 variables')
        # parser.add_argument('-d', '--vard', default=0, type=int)
        # parser.add_argument('-e', '--vare', default=0, type=int)
        # parser.add_argument('-f', '--varf', default=0, type=int)

        args=parser.parse_args()
        # input[0][7] =  args.vard
        # input[1][8] = args.vare
        # input[2][6] = args.varf

        solveSudoku(input)

if __name__ == "__main__":
   main(sys.argv[1:])