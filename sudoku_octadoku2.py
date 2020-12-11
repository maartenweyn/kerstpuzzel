import argparse
import sys

from sudoku import * 

input = [[0,0,2,0,0,5,1,0],[9,8,1,0,0,0,0,0],[0,0,0,0,0,0,3,6],[0,0,1,5,0,0,0,0],[0,0,0,0,0,0,0,1],[6,10,0,0,0,0,0,0],[0,0,0,0,0,0,0,10],[1,0,0,0,4,0,0,8,0],[0,0,0,4,0,7,0,0]]
inputConstrained = [[0,0,2,0,0,5,1,[3,8]],[9,8,0,0, [2,5,7],[3,5,7],0,0],[0,0,0, [2,5,7],0,0,3,6],[[3,8],0,1,5,0,0,0,0],[0,[3,6],0,0,0,0,0,1],[6,10,0,0,0,0,0,0],[0,0,0,0,[2,3,8],0,0,10],[1,0,0,[2,3,8],4,0,0,8,0],[0,0,0,4,0,7,0,[2,5,7]]]
#inputConstrained = [[0,0,2,0,0,5,1,3],[9,8,0,0, 7,3,0,0],[0, 0,0, 7,0, 0,3, 6],[3,0,1,5,0,0,0,0],[0,6,0,0,0,0,0,1],[6,10,0,0,0,0,0,0],[0,0,0,0,2,0,0,10],[1,0,0,2,4,0,0,8,0],[0,0,0,4,0,7,0,2]]


def isValidSudoku(grid, i, j, e):
        testlist = [grid[i][x] for x in range(len(grid[i]))]
        squareOk = testlist.count(e) == 0

        # print("isvalid", i, j, e, grid)
        # print("squareOk", i, j, e, testlist, squareOk, grid)

        if squareOk:
                rowOk = True
                columnOk = True

                ii = int(math.floor(i/3))
                jj = int((i%3))

                if (j == 3):
                        testlist = [grid[(ii*3)][3], grid[(ii*3)][1], grid[(ii*3)][2], grid[(ii*3)][5], grid[(ii*3)][6], grid[(ii*3+1)][3], grid[(ii*3)+1][1], grid[(ii*3)+1][2], grid[(ii*3)+1][5], grid[(ii*3)+1][6], grid[(ii*3)+2][3], grid[(ii*3)+2][1], grid[(ii*3)+2][2], grid[(ii*3)+2][5], grid[(ii*3)+2][6], grid[(ii*3)+2][4]]
                        # rowOk = all([e != grid[(ii*3)+x][3] for x in range(3)]) and all([e != grid[(ii*3)+x][1] for x in range(3)]) and all([e != grid[(ii*3)+x][5] for x in range(3)]) and all([e != grid[(ii*3)+x][2] for x in range(3)]) and all([e != grid[(ii*3)+x][6] for x in range(3)]) and (e != grid[(ii*3)+2][4])
                        
                if (j == 4):
                        testlist = [grid[(ii*3)][3], grid[(ii*3)][4], grid[(ii*3)][1], grid[(ii*3)][2], grid[(ii*3)][5], grid[(ii*3)][6], grid[(ii*3+1)][4], grid[(ii*3)+1][1], grid[(ii*3)+1][2], grid[(ii*3)+1][5], grid[(ii*3)+1][6], grid[(ii*3)+2][4], grid[(ii*3)+2][1], grid[(ii*3)+2][2], grid[(ii*3)+2][5], grid[(ii*3)+2][6]]

                        # rowOk = all([e != grid[(ii*3)+x][4] for x in range(3)]) and all([e != grid[(ii*3)+x][1] for x in range(3)]) and all([e != grid[(ii*3)+x][5] for x in range(3)]) and all([e != grid[(ii*3)+x][2] for x in range(3)]) and all([e != grid[(ii*3)+x][6] for x in range(3)]) and (e != grid[(ii*3)][3])
                        # if (not rowOk):
                        #         return False
                if (((j == 1) or (j == 2)) and ((jj == 0) or (jj == 2))) or (((j == 5) or (j == 6)) and ((jj == 1))):
                        testlist = [grid[(ii*3)][3], grid[(ii*3)][1], grid[(ii*3)][2], grid[(ii*3)][4], grid[(ii*3)+1][5], grid[(ii*3)+1][6], grid[(ii*3)+1][4], grid[(ii*3)+2][1], grid[(ii*3)+2][2], grid[(ii*3)+2][4]]

                        # rowOk = all([e != grid[(ii*3)+x][3] for x in range(3)]) and (e != grid[(ii*3)][1]) and (e != grid[(ii*3)][2])  and (e != grid[(ii*3)+1][5]) and (e != grid[(ii*3)+1][6]) and (e != grid[(ii*3)+2][1]) and (e != grid[(ii*3)+2][2]) and (e != grid[(ii*3)+2][4])
                if (((j == 5) or (j == 6)) and ((jj == 0) or (jj == 2))) or (((j == 1) or (j == 2)) and ((jj == 1))):
                        testlist = [grid[(ii*3)][3], grid[(ii*3)][5], grid[(ii*3)][6], grid[(ii*3)][4], grid[(ii*3)+1][1], grid[(ii*3)+1][2], grid[(ii*3)+1][4], grid[(ii*3)+2][5], grid[(ii*3)+2][6], grid[(ii*3)+2][4]]
                        

                if ((j != 0) and (j != 7)):
                        rowOk = testlist.count(e) == 0
                        # print("rowOk", i, j, e, testlist.count(e), rowOk, testlist)
                        if (not rowOk):
                                return False

                if (j == 0):
                        columnOk = all([e != grid[jj+x*3][0] for x in range(3)]) and all([e != grid[jj+x*3][1] for x in range(3)])  and all([e != grid[jj+x*3][2] for x in range(3)]) and all([e != grid[jj+x*3][5] for x in range(3)])  and all([e != grid[jj+x*3][6] for x in range(3)]) and (e != grid[jj+6][7])
                        
                if (j == 7):
                        columnOk = all([e != grid[jj+x*3][7] for x in range(3)]) and all([e != grid[jj+x*3][1] for x in range(3)])  and all([e != grid[jj+x*3][2] for x in range(3)]) and all([e != grid[jj+x*3][5] for x in range(3)])  and all([e != grid[jj+x*3][6] for x in range(3)]) and (e != grid[jj+6][0])
   
                if (((j == 1) or (j == 5)) and ((ii == 0) or (ii == 2))) or (((j == 2) or (j == 6)) and ((ii == 1))):
                        columnOk = all([e != grid[jj+x*3][0] for x in range(3)]) and (e != grid[jj][2])  and (e != grid[jj][6])   and (e != grid[jj+3][1])   and (e != grid[jj+3][5]) and (e != grid[jj+6][2])   and (e != grid[jj+6][6]) and (e != grid[jj+6][7])

                if (((j == 2) or (j == 6)) and ((ii == 0) or (ii == 2))) or (((j == 1) or (j == 5)) and ((ii == 1))):
                        columnOk = all([e != grid[jj+x*3][0] for x in range(3)]) and (e != grid[jj][1])  and (e != grid[jj][5])   and (e != grid[jj+3][2])   and (e != grid[jj+3][6]) and (e != grid[jj+6][1])   and (e != grid[jj+6][5]) and (e != grid[jj+6][7])


                if ((j != 3) and (j != 4)):
                        # print("columnOk", i, j, e, columnOk)
                        if (not columnOk):
                                return False


                
                if rowOk and columnOk:
                        neighbourok = True
                        if j == 4:
                                if (i % 3 < 2):
                                        neighbourok =  all([e != grid[i+1][x] for x in range(8) if x != 3])
                                        # if (neighbourok):
                                        #         grid[i+1][3] = e
                        if j == 7:
                                if (i < 6):
                                        neighbourok =  all([e != grid[i+3][x] for x in range(8) if x != 0])
                                        # if (neighbourok):
                                        #         grid[i+3][0] = e

                        if (j == 3):
                                if (i % 3 > 0):
                                        neighbourok = all([e != grid[i-1][x] for x in range(8) if x != 4])
                                        # if (neighbourok):
                                        #         grid[i-1][4] = e

                        if (j == 0):
                                if (i > 2):
                                        neighbourok = all([e != grid[i-3][x] for x in range(8) if x != 7])
                                        # if (neighbourok):
                                        #         grid[i-3][7] = e

                        # print("neighbourok", neighbourok)
                        if neighbourok:
                                return True
        
        return False


def solveSudokuTrial(grid,  x, return_dic, options, solutions, i=0, j=0): 
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return_dic[x] = True
                return True
        #for e in range(1,10):
        return_dic[x] = False
        
        for e in options[i][j]:
                # print ("testing ", e, "from", options[i][j], "for", i, j)
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

                        # print("iterating with", i, j, e, grid)
                        if solveSudokuTrial(grid, e, return_dic, options, solutions, i, j):
                                print("Found Solution: ", grid, grid[8][7], grid[0][7], grid[4][1], grid[2][3], grid[7][3], grid[1][5]) 
                                solution = grid[8][7] * 100000 + grid[0][7] * 10000 + grid[4][1] * 1000 + grid[2][3] * 100 + grid[7][3] * 10 +  grid[1][5]
                                if not solution in solutions:
                                        solutions.append(solution)
                                return_dic[x] = True
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

        solveSudoku(inputConstrained, solveSudokuTrial, isValidSudoku, 10)

if __name__ == "__main__":
   main(sys.argv[1:])