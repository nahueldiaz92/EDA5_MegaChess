import unittest
import board_moves


board = [
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#0
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#1
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#2
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#3
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#4
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#5
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#6
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#7
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#8
[' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#9
[' ', 'P', ' ', ' ', 'q', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#10
[' ', ' ', ' ', 'P', 'P', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#11
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#12
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#13
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#14
[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],#15
]#0   #1   #2   #3   #4   #5   #6   #7   #8   #9   #10  #11  #12  #13  #14  #15

class test_sample(unittest.TestCase):

    def test_white(self):
        white = True
        result = board_moves.is_white_piece(board, 11, 3)
        self.assertEqual(white, result)
        black = False
        result = board_moves.is_white_piece(board, 10, 4)
        self.assertEqual(black, result)
        empty = False
        result = board_moves.is_white_piece(board, 1, 1)
        self.assertEqual(empty,result)

    def test_black(self):
        black = True
        result = board_moves.is_black_piece(board, 10, 4)
        self.assertEqual(black, result)
        white = False
        result = board_moves.is_black_piece(board, 10, 1)
        self.assertEqual(white, result)
        empty = False
        result = board_moves.is_black_piece(board, 1, 1)
        self.assertEqual(empty, result)
    
    def test_empty(self):
        empty = True
        result = board_moves.empty_square(board, 1, 1)
        self.assertEqual(empty, result)
        white = False
        result = board_moves.empty_square(board, 10, 1)
        self.assertEqual(white, result)
        black = False
        result = board_moves.empty_square(board, 10, 4)
        self.assertEqual(black, result)




