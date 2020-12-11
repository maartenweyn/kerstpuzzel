import math
import multiprocessing 
import sys
import copy

def findoptions(grid, isValidSudoku, end):
        options = []
        nr_options = 0
        for i in range (0, len(grid)):
                sq_options = []
                # print("len", i, len(grid[i]))
                for j in range (0, len(grid[i])):
                        cell_options = []
                        # print("testing option", i, j)
                        if (isinstance(grid[i][j], list)):
                                for e in grid[i][j]:
                                        cell_options.append(e)
                        else:
                                if (grid[i][j] == 0):
                                        for e in range(1,end+1):
                                                if isValidSudoku(grid,i,j,e):
                                                        cell_options.append(e)
                                                        # print("adding option", i, j, e)
                                else:
                                        cell_options.append(grid[i][j])
                                        # print("adding defaults", i, j, grid[i][j])
                        if (len(cell_options) > 1):
                                nr_options += len(cell_options)
                        sq_options.append(cell_options)
                options.append(sq_options)
        print("nr of options", nr_options)
        return options


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

def solveSudoku(grid, solveSudokuTrial, isValidSudoku, end_nr):
        options = []
        count = 0
        options_length = 0

        if (count == 0):
                options_length = 0
                prev = -1
                while (prev != options_length):
                        prev = options_length
                        options = findoptions(grid, isValidSudoku, end_nr)
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

                input = copy.deepcopy(grid)
                for i in range (0, len(input)):
                        for j in range (0, len(input[i])):
                                if (isinstance(input[i][j], list)):
                                        input[i][j] = 0

                print("new input", input)

        processes = []
        manager = multiprocessing.Manager()
        return_dict = manager.dict()
        solutions = manager.list()


        #while (prev_length != min_length or min_i != prev_i or min_j != prev_j):
        for i in range (0, len(options)):
                for j in range (0, len(options[i])):
                        if (len(options[i][j]) > 1):
                                for e in options[i][j]:
                                        test_grid = copy.deepcopy(input)
                                        test_grid[i][j] = e
                                        print("testing ", i, j, options[i][j], e)
                                        p = multiprocessing.Process(target=solveSudokuTrial, args=(test_grid, e, return_dict, options,solutions, 0, 0))
                                        processes.append(p)
                                        p.start()

                                for process in processes:
                                        process.join()
                                
                                        print("join")

                                print("JOIINED")
                                processes = []

                                for e in return_dict:
                                        print(e, return_dict[e])

                                for e in options[i][j]:
                                        if (return_dict.has_key(e)):
                                                print("return ", e, return_dict[e])
                                                if not return_dict[e]:
                                                        options[i][j].remove(e)
                                                        print("removed ", e, options)
                                        else:
                                                print ("cannot find key ", i, j, e, " in ", return_dict)

                                if (len(options[i][j]) == 1):
                                        input[i][j] = options[i][j][0]
                                        for e in range(0, len(options[i])):
                                                if e != j:
                                                        if input[i][j] in options[i][e]:
                                                               options[i][e].remove(input[i][j]) 
                                        print("NEW grid ", options)
                                
                                if len(options[i][j]) == 0:
                                        print ("ERROR CAN NOT SOLVE THIS SUDOKU")
                                        return False

        print("trying last option")
        print("options", options)
        print("input", input)
        solveSudokuTrial(input, 0, return_dict, options, solutions)
        
        print("solutions")
        for s in solutions:
                print(s)