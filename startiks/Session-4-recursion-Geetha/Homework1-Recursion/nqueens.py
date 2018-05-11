import copy
def isSafe(board,row,col):
    N= len(board)
    for i in range(N):
        '''if any [row][0..N] is marked, it is unsafe '''
        if board[row][i]== 1 :
            return False
        '''if any [0..N][col] is marked, it is unsafe'''
        if board[i][col] ==1:
            return False

    '''This is checking for  diagonal elements
    if any [row to 0][col to 0] or [row to N][col to N] or 
    [row to 0][col to N] or [row to N][col to 0] 
    is marked it is unsafe'''

    drow = row
    dcol = col
    while ((drow >=0) and (dcol >=0)):
        if board[drow][dcol]== 1 :
            return False
        else :
            drow = drow - 1
            dcol = dcol - 1
    drow = row
    dcol = col
    while ((row <= drow < N) and 0 <=dcol <=col ):
        if board[drow][dcol]== 1 :
            return False
        else:
            drow = drow + 1
            dcol = dcol - 1
    drow = row
    dcol = col
    while((0 <= drow < row) and (col <=dcol <N)):
        if board[drow][dcol]== 1 :
            return False
        else:
            drow = drow - 1
            dcol = dcol + 1
    drow = row
    dcol = col
    while ((row <= drow < N) and (col <= dcol < N)):
        if board[drow][dcol] == 1:
            return False
        else:
            drow = drow + 1
            dcol = dcol + 1
    return True

def nqueens(result_boards,board,col):
    N=len(board)
    if col >= N :
        #printboard(board)
        result_boards.append(copy.deepcopy(board))
        return

    for i in range(N):
        if (isSafe(board,i,col)):
            board [i][col] = 1
            nqueens(result_boards,board,col+1)
            board [i][col] = 0  #backtracking
    return


def printboard(board):
    N= len(board)
    for i in range(N):
        board_line = ""
        for j in range(N):
            board_line = board_line + str(board[i][j]) + ","
        print (board_line)
        #print(" \n")


n= 4
board = [ [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0],
              [0, 0, 0, 0]
             ]
result = []
nqueens(result,board,0 )
for i in range (len(result)):
    printboard(result[i])
    print("end")
