import numpy as np

#convert the board string into a 16x16 board
def get_board(board_str):

    board = np.array(list(board_str), dtype=str)
    board = board.reshape(16,16)
    print(board)
    return(board)

#defines black and white pieces
black_piece = "prkhbq"
white_piece = "PRQHBK"

#check if the position in the board is empty
def empty_square(board, row, col):
    if board[row][col] == " ":
        return True
    return False

#check if the position in the board is a black piece
def is_black_piece(board, row, col):
    if board[row][col] in black_piece:
        return True
    return False

#check if the position in the board is a white piece
def is_white_piece(board, row, col):
    if board[row][col] in white_piece:
        return True
    return False

"""
Check the complete board to find possible moves, and return a list of capture moves,
or a list of regular moves if there is no capture moves
"""
def moving_white(board):
    white_move = []
    white_capture = []
    for row in range(16):
        for col in range(16):
            if board[row][col] == "P":
                if col > 0 and is_black_piece(board, row-1, col-1):
                    white_capture.insert(0,[row, col, row-1,col-1])
                if col < 15 and is_black_piece(board, row-1, col+1):
                    white_capture.insert(0,[row, col, row-1,col+1])
                if row < 12 and empty_square(board, row -1,col):
                    white_move.append([row, col, row-1,col])
                if row == 12 and empty_square(board, row-2, col):
                    white_move.append([row, col, row-2,col])
                if row == 13 and empty_square(board, row-2, col):
                    white_move.append([row, col, row-2,col])
            if board[row][col] == "Q":
                if row < 15 and col < 15 and is_black_piece(board,row+1,col+1):
                    white_capture.append([row,col,row+1,col+1])
                if row < 15 and is_black_piece(board,row+1,col):
                    white_capture.append([row,col,row+1,col])
                if col <15 and row > 0 and is_black_piece(board,row-1,col+1):
                    white_capture.append([row,col,row-1,col+1])
                if row > 0 and col > 0 and is_black_piece(board,row-1,col-1):
                    white_capture.append([row,col,row-1,col-1])
                if row > 0 and is_black_piece(board,row-1,col):
                    white_capture.append([row,col,row-1,col])
                if col < 15 and is_black_piece(board,row,col+1):
                    white_capture.append([row,col,row,col+1])
                if col > 0 and is_black_piece(board,row,col-1):
                    white_capture.append([row,col,row,col-1])
                if row < 15 and col > 0 and is_black_piece(board,row+1,col-1):
                    white_capture.append([row,col,row+1,col-1])
            if board[row][col] == "R":
                if row < 15 and is_black_piece(board,row+1,col):
                    white_capture.append([row,col,row+1,col])
                if row > 0 and is_black_piece(board,row-1,col):
                    white_capture.append([row,col,row-1,col])
                if col < 15 and is_black_piece(board,row,col+1):
                    white_capture.append([row,col,row,col+1])
                if col > 0 and is_black_piece(board,row,col-1):
                    white_capture.append([row,col,row,col-1])
            if board[row][col] == "B":
                if row < 15 and col < 15 and is_black_piece(board,row+1,col+1):
                    white_capture.append([row,col,row+1,col+1])
                if col <15 and row > 0 and is_black_piece(board,row-1,col+1):
                    white_capture.append([row,col,row-1,col+1])
                if row > 0 and col > 0 and is_black_piece(board,row-1,col-1):
                    white_capture.append([row,col,row-1,col-1])
                if row < 15 and col > 0 and is_black_piece(board,row+1,col-1):
                    white_capture.append([row,col,row+1,col-1])
            if board[row][col] == "K":
                if row < 15 and col < 15 and empty_square(board,row+1,col+1) and not is_black_piece(board, row or row +1 or row-1, col or col +1 or col-1):
                    white_move.append([row,col,row+1,col+1])
                if row < 15 and empty_square(board,row+1,col) and not is_black_piece(board, row or row +1 or row-1, col or col +1 or col-1):
                    white_move.append([row,col,row+1,col])
                if col <15 and row > 0 and empty_square(board,row-1,col+1) and not is_black_piece(board, row or row +1 or row-1, col or col +1 or col-1):
                    white_move.append([row,col,row-1,col+1])
                if row > 0 and col > 0 and empty_square(board,row-1,col-1) and not is_black_piece(board, row or row +1 or row-1, col or col +1 or col-1):
                    white_move.append([row,col,row-1,col-1])
                if row > 0 and empty_square(board,row-1,col) and not is_black_piece(board, row or row +1 or row-1, col or col +1 or col-1):
                    white_move.append([row,col,row-1,col])
                if col < 15 and empty_square(board,row,col+1) and not is_black_piece(board, row or row +1 or row-1, col or col +1 or col-1):
                    white_move.append([row,col,row,col+1])
                if col > 0 and empty_square(board,row,col-1) and not is_black_piece(board, row or row +1 or row-1, col or col +1 or col-1):
                    white_move.append([row,col,row,col-1])
                if row < 15 and col > 0 and empty_square(board,row+1,col-1) and not is_white_piece(board, row or row +1 or row-1, col or col +1 or col-1):
                    white_move.append([row,col,row+1,col-1])
                if row < 15 and col < 15 and is_black_piece(board,row+1,col+1):
                    white_capture.append([row,col,row+1,col+1])
                if row < 15 and is_black_piece(board,row+1,col):
                    white_capture.append([row,col,row+1,col])
                if col <15 and row > 0 and is_black_piece(board,row-1,col+1):
                    white_capture.append([row,col,row-1,col+1])
                if row > 0 and col > 0 and is_black_piece(board,row-1,col-1):
                    white_capture.append([row,col,row-1,col-1])
                if row > 0 and is_black_piece(board,row-1,col):
                    white_capture.append([row,col,row-1,col])
                if col < 15 and is_black_piece(board,row,col+1):
                    white_capture.append([row,col,row,col+1])
                if col > 0 and is_black_piece(board,row,col-1):
                    white_capture.append([row,col,row,col-1])
                if row < 15 and col > 0 and is_black_piece(board,row+1,col-1):
                    white_capture.append([row,col,row+1,col-1])
                   
    #The caoture list is reversed so it takes priority for defensive moves
    if white_capture != []:
        return list(reversed(white_capture))
    else:
        return white_move

"""
Check the complete board to find possible moves, and return a list of capture moves,
or a list of regular moves if there is no capture moves
"""

def moving_black(board):
    black_move = []
    black_capture = []
    for row in range(16):
        for col in range(16):
            if board[row][col] == "p":
                if col > 0 and is_white_piece(board, row+1, col-1):
                    black_capture.append([row, col, row+1,col-1])
                if col < 15 and is_white_piece(board, row+1, col+1):
                    black_capture.append([row, col, row+1,col+1])
                if row == 3 and empty_square(board, row+2, col) and empty_square(board, row+1, col):
                    black_move.append([row, col, row +2, col])
                if row == 2 and empty_square(board, row+2, col) and empty_square(board, row+1, col):
                    black_move.append([row, col, row +2, col])    
                if row > 3 and empty_square(board,row+1,col):
                    black_move.append([row, col, row+1, col])

            if board[row][col] == "q":
                if row < 15 and col < 15 and is_white_piece(board,row+1,col+1):
                    black_capture.append([row,col,row+1,col+1])
                if row < 15 and is_white_piece(board,row+1,col):
                    black_capture.append([row,col,row+1,col])
                if col <15 and row > 0 and is_white_piece(board,row-1,col+1):
                    black_capture.append([row,col,row-1,col+1])
                if row > 0 and col > 0 and is_white_piece(board,row-1,col-1):
                    black_capture.append([row,col,row-1,col-1])
                if row > 0 and is_white_piece(board,row-1,col):
                    black_capture.append([row,col,row-1,col])
                if col < 15 and is_white_piece(board,row,col+1):
                    black_capture.append([row,col,row,col+1])
                if col > 0 and is_white_piece(board,row,col-1):
                    black_capture.append([row,col,row,col-1])
                if row < 15 and col > 0 and is_white_piece(board,row+1,col-1):
                    black_capture.append([row,col,row+1,col-1])
            if board[row][col] == "r":
                if row < 15 and is_white_piece(board,row+1,col):
                    black_capture.append([row,col,row+1,col])
                if row > 0 and is_white_piece(board,row-1,col):
                    black_capture.append([row,col,row-1,col])
                if col < 15 and is_white_piece(board,row,col+1):
                    black_capture.append([row,col,row,col+1])
                if col > 0 and is_white_piece(board,row,col-1):
                    black_capture.append([row,col,row,col-1])
            if board[row][col] == "b":
                if row < 15 and col < 15 and is_white_piece(board,row+1,col+1):
                    black_capture.append([row,col,row+1,col+1])
                if col <15 and row > 0 and is_white_piece(board,row-1,col+1):
                    black_capture.append([row,col,row-1,col+1])
                if row > 0 and col > 0 and is_white_piece(board,row-1,col-1):
                    black_capture.append([row,col,row-1,col-1])
                if row < 15 and col > 0 and is_white_piece(board,row+1,col-1):
                    black_capture.append([row,col,row+1,col-1])
            if board[row][col] == "k":
                if row < 15 and col < 15 and empty_square(board,row+1,col+1):
                    black_move.append([row,col,row+1,col+1])
                if row < 15 and empty_square(board,row+1,col):
                    black_move.append([row,col,row+1,col])
                if col <15 and row > 0 and empty_square(board,row-1,col+1):
                    black_move.append([row,col,row-1,col+1])
                if row > 0 and col > 0 and empty_square(board,row-1,col-1):
                    black_move.append([row,col,row-1,col-1])
                if row > 0 and empty_square(board,row-1,col):
                    black_move.append([row,col,row-1,col])
                if col < 15 and empty_square(board,row,col+1):
                    black_move.append([row,col,row,col+1])
                if col > 0 and empty_square(board,row,col-1):
                    black_move.append([row,col,row,col-1])
                if row < 15 and col > 0 and empty_square(board,row+1,col-1):
                    black_move.append([row,col,row+1,col-1])
                if row < 15 and col < 15 and is_white_piece(board,row+1,col+1):
                    black_capture.append([row,col,row+1,col+1])
                if row < 15 and is_white_piece(board,row+1,col):
                    black_capture.append([row,col,row+1,col])
                if col <15 and row > 0 and is_white_piece(board,row-1,col+1):
                    black_capture.append([row,col,row-1,col+1])
                if row > 0 and col > 0 and is_white_piece(board,row-1,col-1):
                    black_capture.append([row,col,row-1,col-1])
                if row > 0 and is_white_piece(board,row-1,col):
                    black_capture.append([row,col,row-1,col])
                if col < 15 and is_white_piece(board,row,col+1):
                    black_capture.append([row,col,row,col+1])
                if col > 0 and is_white_piece(board,row,col-1):
                    black_capture.append([row,col,row,col-1])
                if row < 15 and col > 0 and is_white_piece(board,row+1,col-1):
                    black_capture.append([row,col,row+1,col-1])
  #The move list is reversed so it takes priority in offensive moves
    if black_capture != []:
        return black_capture
    else:
        return list(reversed(black_move))
