import math
import copy
import argparse
import sys

from sudoku import * 

input = [[0,0,2,0,0,5,1,0],[9,8,0,0,0,0,0,0],[0,0,0,0,0,0,3,6],[0,0,1,5,0,0,0,0],[0,0,0,0,0,0,0,1],[6,10,0,0,0,0,0,0],[0,0,0,0,0,0,0,10],[1,0,0,0,4,0,0,8,0],[0,0,0,4,0,7,0,0]]
#inputConstrained = [[0,0,2,0,0,5,1,[3,8]],[9,8,0,[2,5,7],[3,5,7],0,0,0],[0,0,[2,5,7],0,0,0,3,6],[[3,8],0,1,5,0,0,0,0],[0,[3,6],0,0,0,0,0,1],[6,10,0,0,0,0,0,0],[0,0,0,0,[2,3,8],0,0,10],[1,0,0,[2,3,8],4,0,0,8,0],[0,0,0,4,0,7,0,[2,5,7]]]
#inputConstrained = [[3,4,2,0,0,5,1,8],[9,8,0,[2,5,7],[3,5,7],0,0,0],[0,0,[2,5,7],0,0,0,3,6],[[3,8],0,1,5,0,0,0,0],[0,[3,6],0,0,0,0,0,1],[6,10,0,0,0,0,0,0],[0,0,0,0,[2,3,8],0,0,10],[1,0,0,[2,3,8],4,0,0,8,0],[0,0,0,4,0,7,0,[2,5,7]]]
inputConstrained = [[6,4,2,0,0,5,1,[3,8]],[9,8,0,[2,5,7],[3,5,7],0,0,0],[0,0,[2,5,7],0,0,0,3,6],[[3,8],0,1,5,0,0,0,0],[0,[3,6],0,0,0,0,0,1],[6,10,0,0,0,0,0,0],[0,0,0,0,[2,3,8],0,0,10],[1,0,0,[2,3,8],4,0,0,8,0],[0,0,0,4,0,7,0,[2,5,7]]]


# (364, [[[3, 4, 6, 7, 8, 9], [3, 4, 6, 7, 8, 9], [2], [3, 4, 6, 7, 8, 9], [3, 4, 6, 7], [5], [1], [3, 8]], [[9], [8], [1, 2, 3, 4, 5, 6, 7], [2, 5, 7], [3, 5, 7], [1, 2, 3, 4, 5, 6, 7], [1, 2, 3, 4, 5, 6, 7], [2, 3, 4, 5, 6, 7]], [[1, 2, 4, 5, 7, 8, 9], [1, 2, 4, 5, 7, 8, 9], [2, 5, 7], [1, 2, 4, 5, 7], [1, 2, 4, 5, 7, 8, 9], [1, 2, 4, 5, 7, 8, 9], [3], [6]], [[3, 8], [2, 3, 4, 6, 7, 8, 9], [1], [5], [2, 3, 4, 6, 7, 8, 9], [2, 3, 4, 6, 7, 8, 9], [2, 3, 4, 6, 7, 8, 9], [2, 3, 4, 6, 7, 8, 9]], [[2, 3, 4, 5, 6, 7], [3, 6], [2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 6, 7, 8, 9], [2, 3, 4, 5, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 4, 5, 6, 7, 8, 9], [1]], [[6], [10], [1, 2, 3, 4, 5, 7, 8, 9], [2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 4, 5, 7, 8, 9], [1, 2, 3, 5, 8, 9]], [[2, 3, 4, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [2, 3, 8], [1, 2, 3, 4, 5, 6, 7, 8, 9], [1, 2, 3, 4, 5, 6, 7, 8, 9], [10]], [[1], [2, 3, 5, 6, 7, 9], [2, 3, 5, 6, 7, 9], [2, 3, 8], [4], [2, 3, 5, 6, 7, 9], [2, 3, 5, 6, 7, 9], [8], [2, 3, 5, 6, 7, 9]], [[1, 2, 3, 5, 8, 9], [1, 2, 3, 5, 6, 8, 9], [1, 2, 3, 5, 6, 8, 9], [4], [1, 2, 3, 5, 6, 8, 9], [7], [1, 2, 3, 5, 6, 8, 9], [2, 5, 7]]])
# ('new grid', [[0, 0, 2, 0, 0, 5, 1, [3, 8]], [9, 8, 0, [2, 5, 7], [3, 5, 7], 0, 0, 0], [0, 0, [2, 5, 7], 0, 0, 0, 3, 6], [[3, 8], 0, 1, 5, 0, 0, 0, 0], [0, [3, 6], 0, 0, 0, 0, 0, 1], [6, 10, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, [2, 3, 8], 0, 0, 10], [1, 0, 0, [2, 3, 8], 4, 0, 0, 8, 0], [0, 0, 0, 4, 0, 7, 0, [2, 5, 7]]])
# ('new input', [[0, 0, 2, 0, 0, 5, 1, 0], [9, 8, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 3, 6], [0, 0, 1, 5, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1], [6, 10, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 10], [1, 0, 0, 0, 4, 0, 0, 8, 0], [0, 0, 0, 4, 0, 7, 0, 0]])


def isValidSudoku(grid, i, j, e):
        squareOk = all([e != grid[i][x] for x in range(len(grid[i]))])
        if squareOk:
                neighbourok = True

                ii = int(math.floor(i/3))

                if j == 4:
                        if ((i % 3) < 2):
                                neighbourok =  all([e != grid[i+1][x] for x in range(8) if x != 3])
                if j == 7:
                        if (i < 6):
                                neighbourok =  all([e != grid[i+3][x] for x in range(8) if x != 0])

                if (j == 3):
                        if ((i % 3) > 0):
                                neighbourok = all([e != grid[i-1][x] for x in range(8) if x != 4])

                if (j == 0):
                        if (i > 2):
                                neighbourok = all([e != grid[i-3][x] for x in range(8) if x != 7])

                if neighbourok:
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
                        if j == 4:
                                if (i % 3 < 2):
                                        grid[i+1][3] = e
                        if j == 7:
                                if (i < 6):
                                        grid[i+3][0] = e

                        if (j == 3):
                                if (i % 3 > 0):
                                        grid[i-1][4] = e

                        if (j == 0):
                                if (i > 2):
                                        grid[i-3][7] = e

                        if solveSudokuTrial(grid, e, return_dic, options, solutions, i, j):
                                print("Found Solution: ", grid, grid[8][7], grid[0][7], grid[4][1], grid[2][3], grid[7][3], grid[1][5]) 
                                solution = grid[8][7] * 100000 + grid[0][7] * 10000 + grid[4][1] * 1000 + grid[2][3] * 100 + grid[7][3] * 10 +  grid[1][5]
                                if not solution in solutions:
                                        solutions.append(solution)
                                return_dic[e] = True
                                return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
                        if j == 4:
                                if (i % 3 < 2):
                                        grid[i+1][3] = 0
                        if j == 7:
                                if (i < 6):
                                        grid[i+3][0] = 0

                        if (j == 3):
                                if (i % 3 > 0):
                                        grid[i-1][4] = 0

                        if (j == 0):
                                if (i > 2):
                                        grid[i-3][7] = 0
        
        return_dic[e] = False
        return False



def main(argv):

        parser = argparse.ArgumentParser(description='solve sudoke with 3 variables')
        parser.add_argument('-g', '--varg', default=0, type=int)
        parser.add_argument('-hh', '--varh', default=0, type=int)
        parser.add_argument('-i', '--vari', default=0, type=int)
        parser.add_argument('-j', '--varj', default=0, type=int)
        parser.add_argument('-k', '--vark', default=0, type=int)
        parser.add_argument('-l', '--varl', default=0, type=int)

        args=parser.parse_args()
        if args.varg != 0:
                input[8][7] = args.varg
        if args.varh != 0:
                input[0][7] = args.varh
                input[3][0] = args.varh
        if args.vari != 0:
                input[4][1] = args.vari
        if args.varj != 0:
                input[2][3] = args.varj
                input[1][4] = args.varj
        if args.vark != 0:
                input[7][3] = args.vark
                input[6][4] = args.vark
        if args.varl != 0:
                input[1][5] = args.varl

        print("INPUT", inputConstrained)

        solveSudoku(inputConstrained, solveSudokuTrial, isValidSudoku)

if __name__ == "__main__":
   main(sys.argv[1:])