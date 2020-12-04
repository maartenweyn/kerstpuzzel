import math
import copy
import multiprocessing 
import argparse
import sys

input = [[0,0,6, 0,0,0, 0,0,0], [0,0,0, 0,0,0, 0,4,0], [1,0,9, 0,0,0, 0,0,0], [0,8,0, 0,0,0, 0,3,0], [0,0,2, 5,0,1, 4,0,0], [3,4,0, 8,0,7, 0,0,0], [0,0,0, 0,6,0, 0,0,7], [0,3,0, 0,5,0, 0,0,1], [4,0,0, 0,0,1, 0,0,9]]
#nput = [[4, 8, 6, 5, 2, 3, 9, 1, 5], [3, 2, 0, 6, 6, 6, 9, 4, 1], [1, 5, 9, 8, 8, 4, 3, 2, 6], [0, 8, 0, 0, 0, 0, 0, 3, 0], [6, 0, 2, 5, 0, 5, 4, 0, 0], [3, 4, 2, 8, 6, 7, 0, 6, 2], [2, 0, 0, 2, 6, 0, 2, 0, 7], [0, 3, 4, 0, 5, 4, 0, 9, 1], [4, 5, 0, 0, 5, 1, 8, 5, 9]]

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

def solveSudokuTrial(grid,  e, return_dic, options, i=0, j=0):     
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return_dic[e] = True
                return True
        #for e in range(1,10):
        for e in options[i][j]:
                if isValidSudoku(grid,i,j,e):
                        grid[i][j] = e
                        if solveSudokuTrial(grid, e, return_dic, options, i, j):
                                print("Found Solution: ", grid, grid[1][1], grid[8][6], grid[4][5])
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


        #while (prev_length != min_length or min_i != prev_i or min_j != prev_j):
        for i in range (0, len(options)):
                for j in range (0, len(options[i])):
                        if (len(options[i][j]) > 1):
                                for e in options[i][j]:
                                        test_grid = copy.deepcopy(grid)
                                        test_grid[i][j] = e
                                        print("testing ", i, j, options[i][j], e)
                                        p = multiprocessing.Process(target=solveSudokuTrial, args=(test_grid,e, return_dict, options,0, 0))
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
                                        grid[min_i][min_j] = options[min_i][min_j][0]
                                        print("NEW grid ", grid)
                                
                                if len(options[min_i][min_j]) == 0:
                                        print ("ERROR CAN NOT SOLVE THIS SUDOKU")
                                        return False

        print("trying last option")
        return solveSudokuTrial(grid)
                # min_length = 10
                # prev_i = min_i
                # prev_j = min_j
                # prev_length = min_length
                # for i in range (0, len(options)):
                #         for j in range (0, len(options[i])):
                #                 # print(i, j, len(options[i][j]), min_length, min_i, min_j)
                #                 if (len(options[i][j]) > 1 and len(options[i][j]) < min_length):
                #                         min_length = len(options[i][j]) 
                #                         min_i = i
                #                         min_j = j

                # print("examining ", min_i, min_j, prev_length, min_length)
                # if min_i == -1:
                #         print("trying last option")
                #         return solveSudokuTrial(grid)

                # nr_processes = 0

                

        # print("FINISHED", found, min_i, min_j)

def main(argv):

        parser = argparse.ArgumentParser(description='solve sudoke with 3 variables')
        parser.add_argument('-d', '--vard', default=0, type=int)
        parser.add_argument('-e', '--vare', default=0, type=int)
        parser.add_argument('-f', '--varf', default=0, type=int)
        parser.add_argument('-g', '--varg', default=0, type=int)
        parser.add_argument('-hh', '--varh', default=0, type=int)
        parser.add_argument('-i', '--vari', default=0, type=int)

        args=parser.parse_args()
        input[0][7] = args.vard
        input[1][8] = args.vare
        input[2][6] = args.varf
        input[1][1] = args.varg
        input[8][6] = args.varh
        input[4][5] = args.vari

        solveSudoku(input)

if __name__ == "__main__":
   main(sys.argv[1:])