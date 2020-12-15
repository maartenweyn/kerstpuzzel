import argparse
import sys

from sudoku import * 

#input = [[0,0,6, 0,0,0, 0,0,0], [0,0,0, 0,0,0, 0,4,0], [1,0,9, 0,0,0, 0,0,0], [0,8,0, 0,0,0, 0,3,0], [0,0,2, 5,0,0, 4,0,0], [3,4,0, 8,0,7, 0,0,0], [0,0,0, 0,6,0, 0,0,7], [0,3,0, 0,5,0, 0,0,1], [4,0,0, 0,0,1, 0,0,9]]
input = [[0,0,6, 0,0,0, 0,[1,2,8,9],0], [0,0,0, 0,0,0, 0,4,[2,6,7,8]], [1,0,9, 0,0,0, [3,8],0,0], [0,8,0, 0,0,0, 0,3,0], [0,0,2, 5,0,0, 4,0,0], [3,4,0, 8,0,7, 0,0,0], [0,0,0, 0,6,0, 0,0,7], [0,3,0, 0,5,0, 0,0,1], [4,0,0, 0,0,1, 0,0,9]]


def isValidSudoku(grid, i, j, e):
        squareOk = all([e != grid[i][x] for x in range(9)])
        if squareOk:
                r = int(math.floor(j/3))
                c = j % 3

                rowOk = True
                columnOk = True

                ii = int(math.floor(i/3))

                
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
                                print("Found Solution: ", grid, grid[0][7], grid[1][8], grid[2][6], grid[1][1], grid[8][6], grid[4][5])
                                solution = grid[0][7] * 100000 + grid[1][8] * 10000 + grid[2][6] * 1000 + grid[1][1] * 100 + grid[8][6] * 10 +  grid[4][5]
                                if not solution in solutions:
                                        solutions.append(solution)
                                return_dic[e] = True
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        
        return_dic[e] = False
        return False


def main(argv):

        parser = argparse.ArgumentParser(description='solve sudoke with 3 variables')
        parser.add_argument('-d', '--vard', default=0, type=int)
        parser.add_argument('-e', '--vare', default=0, type=int)
        parser.add_argument('-f', '--varf', default=0, type=int)
        parser.add_argument('-g', '--varg', default=0, type=int)
        parser.add_argument('-hh', '--varh', default=0, type=int)
        parser.add_argument('-i', '--vari', default=0, type=int)

        args=parser.parse_args()
        if args.vard != 0:
                input[0][7] = args.vard
        if args.vare != 0:
                input[1][8] = args.vare
        if args.varf != 0:
                input[2][6] = args.varf
        if args.varg != 0:
                input[1][1] = args.varg
        if args.varh != 0:
                input[8][6] = args.varh
        if args.vari != 0:
                input[4][5] = args.vari

        solveSudoku(input, solveSudokuTrial, isValidSudoku, 9)

if __name__ == "__main__":
   main(sys.argv[1:])