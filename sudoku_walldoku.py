import argparse

from sudoku import * 


input = [[0,9,0, 0,0,0, 0,0,0],[0,6,0, 0,0,0, 7,0,0], [0,0,0, 0,0,0, 9,0,5], [0,0,0, 0,0,0, 0,0,4], [9,0,0, 0,8,5, 6,0,0], [8,1,0, 4,0,0, 5,0,0], [8,0,0, 0,0,6, 1,2,0], [0,0,0, 0,0,0, 0,4,0], [0,0,1, 0,0,0, 0,0,0]]
inputConstrained = [[[1,3],9,0, 0,0,0, 0,0,0],[0,6,0, 0,0,0, 7,0,[2,3,8]], [0,0,0, 0,0,0, 9,0,5], [0,0,0, 0,0,0, 0,0,4], [9,0,0, 0,8,5, 6,0,0], [8,1,0, 4,0,0, 5,0,0], [8,0,0, 0,[2,3,7],6, 1,2,0], [2,0,0, 0,0,0, 0,4,[2,5,7]], [0,0,1, 0,0,0, [2,6,7,9],0,0]]

def isValidSudoku(grid, i, j, e):
        squareOk = all([e != grid[i][x] for x in range(9)])
        if squareOk:
                r = int(math.floor(j/3))
                c = j % 3

                rowOk = True
                columnOk = True

                ii = int(math.floor(i/3))

                if (ii == 0) or (ii == 1):
                        # print(i, j, ii, r, c)
                        rowOk = all([e != grid[ii*3][(r*3)+x] for x in range(3)]) and all([e != grid[ii*3+1][(r*3)+x] for x in range(3)]) and all([e != grid[ii*3+2][ r*3 + x ] for x in range(3)])
                if (i == 6):
                        rowOk = all([e != grid[6][(r*3)+x] for x in range(3)]) and all([e != grid[2][r+ (x*3)]  for x in range(3)]) and all([e != grid[3][r+ (x*3)]  for x in range(3)]) 
                if (i == 7):
                        rowOk = all([e != grid[7][(r*3)+x] for x in range(3)]) and all([e != grid[8][r+ (x*3)]  for x in range(3)]) and all([e != grid[4][(2-r)+ (x*3)]  for x in range(3)]) 
                if (i == 8):
                        rowOk = all([e != grid[7][(r*3)+x] for x in range(3)]) and all([e != grid[0][(2-r)+ (x*3)]  for x in range(3)]) and all([e != grid[5][(2-r)+ (x*3)]  for x in range(3)]) 


                if (i == 0) or (i == 5):        
                         columnOk = all([e != grid[0][c+(x*3)]    for x in range(3)]) and all([e != grid[5][c+ (x*3)]     for x in range(3)]) and all([e != grid[5][(2-c)*3+ (x)]     for x in range(3)])

                if (i == 1) or (i == 6) or  (i == 7):        
                         columnOk = all([e != grid[1][c+(x*3)] for x in range(3)]) and all([e != grid[6][c+ (x*3)] for x in range(3)]) and all( [e != grid[7][c+ (x*3)] for x in range(3)])
                
                if (i == 2) or (i == 3):        
                         columnOk = all([e != grid[2][c+(x*3)] for x in range(3)]) and all([e != grid[3][c+ (x*3)] for x in range(3)]) and all( [e != grid[6][c*3+ (x)] for x in range(3)])

                if (i == 4):        
                         columnOk = all([e != grid[4][c+(x*3)] for x in range(3)]) and all([e != grid[8][2-c+ (x*3)] for x in range(3)]) and all( [e != grid[7][(2-c)*3+ (x)] for x in range(3)])

                if (i == 8):        
                         columnOk = all([e != grid[8][c+(x*3)] for x in range(3)]) and all([e != grid[4][2-c+ (x*3)] for x in range(3)]) and all( [e != grid[7][c*3+ (x)] for x in range(3)])

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
                                print("Found Solution: ", grid, grid[7][8], grid[1][8], grid[6][4], grid[7][0], grid[0][0], grid[8][6])
                                solution = grid[7][8] * 100000 + grid[1][8] * 10000 + grid[6][4] * 1000 + grid[7][0] * 100 + grid[0][0] * 10 +  grid[8][6]
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
        parser.add_argument('-j', '--varj', default=0, type=int)
        parser.add_argument('-k', '--vark', default=0, type=int)
        parser.add_argument('-l', '--varl', default=0, type=int)
        parser.add_argument('-m', '--varm', default=0, type=int)
        parser.add_argument('-n', '--varn', default=0, type=int)
        parser.add_argument('-o', '--varo', default=0, type=int)

        args=parser.parse_args()
        if args.varj != 0:
                input[7][8] = args.varj
        if args.vark != 0:
                input[1][8] = args.vark
        if args.varl != 0:
                input[6][4] = args.varl
        if args.varm != 0:
                input[7][0] = args.varm
        if args.varn != 0:
                input[0][0] = args.varn
        if args.varo != 0:
                input[8][6] = args.varo

        print("INPUT", inputConstrained)

        solveSudoku(inputConstrained)

if __name__ == "__main__":
   main(sys.argv[1:])