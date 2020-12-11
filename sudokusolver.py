import math
import copy

inputQuasidoku = [[2,0,0,0,0,3,0,0,0],[8,1,0,0,6,0,2,0,0],[0,0,0,0,0,9,3,5,0],[7,0,0,0,0,0,8,0,0],[0,0,8,1,0,0,0,0,2],[0,0,4,0,0,0,9,3,0]]
#inputLovedoku = [[0,0,1,0,0,0,0,7,0],[0,0,0,0,0,4,0,0,0],[7,0,0,2,0,0,0,6,0],[0,4,0,0,0,9,6,2,0],[0,0,0,0,0,0,0,0,2],[1,0,0,3,0,0,0,8,0],[0,5,8,1,0,0,0,0,0],[5,0,3,0,4,0,0,0,9],[0,0,0,0,3,0,0,0,0]]
inputLovedoku = [[0,0,1,0,0,0,0,7,0],[0,0,0,0,0,4,0,0,0],[7,0,0,2,8,0,0,6,0],[0,4,0,0,0,9,6,2,0],[0,0,0,0,0,0,0,0,2],[1,0,6,3,0,0,0,8,0],[0,5,8,1,0,0,0,0,0],[5,0,3,0,4,0,0,0,9],[0,0,0,0,3,5,0,0,0]]

link = [[5, 1, 2, 4], [4, 6, 5, 2], [0, 2, 8, 5]]

inputLovedoku2 = [[0, 0, 1, 0, 0, 0, 0, 7, 0], [0, 0, 0, 0, 0, 4, 0, 0, 0], [7, 0, 0, 2, 8, 0, 0, 6, 0], [0, 4, 0, 0, 0, 9, 6, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 2], [1, 0, 6, 3, 0, 0, 0, 8, 0], [0, 5, 8, 1, 0, 0, 0, 0, 0], [5, 0, 3, 0, 4, 0, 0, 0, 9], [0, 0, 0, 0, 3, 5, 0, 0, 0]]
#inputLovedoku2 =  [[0, 0, 1, 0, 0, 0, 0, 7, 0], [0, 0, 0, 0, 0, 4, 0, 0, 0], [7, 0, 0, 2, 8, 0, 0, 6, 0], [0, 4, 0, 0, 0, 9, 6, 2, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 3, 5, 0, 0, 0]]
#inputsubLovedoku2 =  [[0, 0, 1, 0, 0, 0, 0, 7, 0], [0, 0, 0, 0, 0, 4, 0, 0, 0], [7, 0, 0, 2, 8, 0, 0, 6, 0], [0, 4, 0, 0, 0, 9, 6, 2, 0], [0, 0, 0, 0, 3, 5, 0, 0, 0]]

def findNextCellToFill(grid, i, j):
        for x in range(i,len(grid)):
                for y in range(j,len(grid[x])):
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
        squareOk = all([e != grid[i][x] for x in range(9)])
        if squareOk:
                r = int(math.floor(j/3))
                c = j % 3

                rowOk = True
                columnOk = True

                if (i == 0) or (i == 1):
                        # print("row r/c", r, c, [[e != grid[0][(r*3)+x] for x in range(3)], [e != grid[1][(r*3)+x] for x in range(3)], [e != grid[2][(2-r) + (x*3)] for x in range(3)]])
                        rowOk = all([e != grid[0][(r*3)+x] for x in range(3)]) and all([e != grid[1][(r*3)+x] for x in range(3)]) and  all([e != grid[2][(2-r) + (x*3)] for x in range(3)])
                if (i == 3) or (i == 4) or (i == 2):
                        # print("row r/c", r, c, [[e != grid[3][(r*3)+x] for x in range(3)], [e != grid[4][(r*3)+x] for x in range(3)], [e != grid[2][(r*3) + (x)] for x in range(3)]])
                        rowOk = all([e != grid[3][(r*3)+x] for x in range(3)]) and all([e != grid[4][(r*3)+x] for x in range(3)]) and all([e != grid[2][(r*3) + (x)] for x in range(3)])
                if (i == 5):
                        rowOk = all([e != grid[0][(2-r)+(x*3)] for x in range(3)]) and all([e != grid[3][(2-r)+ (x*3)] for x in range(3)]) and all( [e != grid[5][(r*3) + (x)] for x in range(3)])

                if (i == 0) or (i == 3):        
                        # print("col r/c", r, c, [[e != grid[0][c+(x*3)] for x in range(3)], [e != grid[3][c+ (x*3)] for x in range(3)], [e != grid[5][(2-c)*3 + (x)] for x in range(3)]])
                        columnOk = all([e != grid[0][c+(x*3)] for x in range(3)]) and all([e != grid[3][c+ (x*3)] for x in range(3)],) and all( [e != grid[5][(2-c)*3 + (x)] for x in range(3)])
                if (i == 1) or (i == 4) or (i == 5):
                        # print("col r/c", r, c, [[e != grid[1][c+(x*3)] for x in range(3)], [e != grid[4][c+ (x*3)] for x in range(3)], [e != grid[5][c+ (x*3)] for x in range(3)]])
                        columnOk = all([e != grid[1][c+(x*3)] for x in range(3)]) and all( [e != grid[4][c+ (x*3)] for x in range(3)]) and all( [e != grid[5][c+ (x*3)] for x in range(3)])
                if (i == 2):
                        columnOk = all([e != grid[0][(2-c)*3+x] for x in range(3)]) and all( [e != grid[1][(2-c)*3+x] for x in range(3)]) and all( [e != grid[2][(c*3) + (x)] for x in range(3)])

                if rowOk and columnOk:
                        # print("isValidQuasidoku?", i, j, e, "YES")
                        return True
        
        # print("isValidQuasidoku?", i, j, e, [e != grid[i][x] for x in range(9)], "NO")
        return False

def isValidLovedoku(grid, i, j, e):
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
                        # print("isValidLovedoku?", i, j, e, "YES")
                        return True
        
        # print("isValidLovedoku?", i, j, e, [e != grid
        # [i][x] for x in range(9)], "NO")
        return False

def isValidSubLovedoku(grid, i, j, e):
        squareOk = all([e != grid[i][x] for x in range(9)])
        if squareOk:
                r = int(math.floor(j/3))
                c = j % 3

                rowOk = True
                columnOk = True

                if (i == 0) or (i == 1)  or (i == 2):
                        rowOk = all ([e != grid[0][0+r*3], e != grid[0][1+r*3], e != grid[0][2+r*3], e != grid[1][0+r*3], e != grid[1][1+r*3], e != grid[1][2+r*3], e != grid[2][0+r*3], e != grid[2][1+r*3], e != grid[2][2+r*3]])
                if (i == 3):
                        rowOk = all ([e != grid[0][2-r+0], e != grid[0][2-r+3], e != grid[0][2-r+6], e != grid[3][0+r*3], e != grid[3][1+r*3], e != grid[3][2+r*3], e != grid[2][r+0], e != grid[2][r+3], e != grid[2][r+6]])
                
                if (i == 0) :
                        columnOk = all ([e != grid[0][c+0], e != grid[0][c+3], e != grid[0][c+6], e != grid[3][(2-c)*3+0], e != grid[3][(2-c)*3+1], e != grid[3][(2-c)*3+2], e != grid[2][(2-c)+0], e != grid[2][(2-c)+3], e != grid[2][(2-c)+6]])
                if (i == 2) :
                        columnOk = all ([e != grid[2][c+0], e != grid[2][c+3], e != grid[2][c+6], e != grid[3][(c)*3+1], e != grid[3][(c)*3+1], e != grid[3][(c)*3+2], e != grid[0][(2-c)+0], e != grid[0][(2-c)+3], e != grid[0][(2-c)+6]])

                if (i == 1) or (i == 3)   :
                        columnOk = all ([e != grid[1][c+0], e != grid[1][c+3], e != grid[1][c+6], e != grid[3][c+0], e != grid[3][c+3], e != grid[3][c+6], e != grid[4][c+0], e != grid[4][c+3], e != grid[4][c+6]])


                if rowOk and columnOk:
                        # print("isValidLovedoku?", i, j, e, "YES")
                        return True
        
        # print("isValidLovedoku?", i, j, e, [e != grid[i][x] for x in range(9)], "NO")
        return False

def solveLovedoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValidLovedoku(grid,i,j,e):
                        grid[i][j] = e
                        if solveLovedoku(grid, i, j):
                                print("Found Solution: ", grid, grid[1][6], grid[7][6], grid[3][0])
                                # return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False

def solveSubLovedoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValidSubLovedoku(grid,i,j,e):
                        grid[i][j] = e
                        if solveSubLovedoku(grid, i, j):
                                print("Found Solution: ", grid)
                                # return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False

def solveQuasidoku(grid, i=0, j=0):
        i,j = findNextCellToFill(grid, i, j)
        # print (i, j)
        if i == -1:
                return True
        for e in range(1,10):
                if isValidQuasidoku(grid,i,j,e):
                        grid[i][j] = e
                        if solveQuasidoku(grid, i, j):
                                print("Found Solution: ", grid, grid[5][1], grid[4][6], grid[0][2])
                                # return True
                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False

# def solve2Sudokus(input0, input1, link):
#         for x in range(0,len(link)):
#                for e in range(1,10):
#                         print(x, e)
#                         if isValidQuasidoku(input0,link[x][0],link[x][1],e):
#                                 input0[link[x][0]][link[x][1]] = e
#                                 print("trying with ", x, e, input0)
#                                 grid0 = copy.deepcopy(input0)
#                                 ret = solveQuasidoku(grid0)
#                                 if (ret):
#                                         print("Found Quasidoku", grid0)
#                                         grid1 = copy.deepcopy(input1)
#                                         for x in range(0,len(link)):
#                                                 grid1[link[x][2]][link[x][3]] = grid0[link[x][0]][link[x][1]]
#                                                 print (x, link[x][0], link[x][1] , '->', link[x][2], link[x][3] , ':', grid0[link[x][0]][link[x][1]], grid1[link[x][2]][link[x][3]])
#                                         print("trying with ", grid1)
#                                         ret = solveLovedoku(grid1)
#                                         if ret:
#                                                 print("Found double solution")
#                                                 print("Quasidoku", grid0)
#                                                 print("Lovedoku", grid1)
#                                         else:
#                                                 print("cannot find double solution")

#                                 else:
#                                         print("cannot find solution")

#solve2Sudokus(inputQuasidoku, inputLovedoku, link)


solveQuasidoku(inputQuasidoku)

#solveLovedoku(inputLovedoku2)
#solveSubLovedoku(inputsubLovedoku2)
