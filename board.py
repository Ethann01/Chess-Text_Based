from typing import List, Tuple
from piece import Piece

class Board:
    """Anything related to the game board. Updating, flipping, you name it.
    Note that checking whether a move is valid occurs in chess.py, the main game file. 
    Updating the board occurs here after checking if a move is valid.
    
    also remember to print self.board backwards because i messed up"""

    def __init__(self)-> None:
        self.board = self.new_board()
    """
    def flip_board(self)-> List[List[Piece]]:

        flipped = []
        if self.board != []:
            for row in range(len(self.board)):
                flipped.append(self.board[len(self.board) - 1 - row])
        self.board = flipped
        return self.board"""
    
    def new_board(self)-> List[List[Piece]]:
        """Returns a new chess board."""
        board = []
        w_pieces = [Piece.Rook((0,0), 'white'), Piece.Knight((0,1), 'white'), Piece.Bishop((0,2), 'white'), \
            Piece.Queen((0,3), 'white'), Piece.King((0,4), 'white'), Piece.Bishop((0,5), 'white'), \
                Piece.Knight((0,6), 'white'), Piece.Rook((0,7), 'white')]
        b_pieces = [Piece.Rook((7,0), 'black'), Piece.Knight((7,1), 'black'), Piece.Bishop((7,2), 'black'), \
            Piece.Queen((7,3), 'black'), Piece.King((7,4), 'black'), Piece.Bishop((7,5), 'black'), \
                Piece.Knight((7,6), 'black'), Piece.Rook((7,7), 'black')]
        b_pieces = 
        w_pawns = []
        b_pawns = []
        for i in range(8):
            board.append([])
            w_pawns.append(Piece.Pawn((1,i), 'white'))
            b_pawns.append(Piece.Pawn((6,i), 'black'))
            for j in range(8):
                board[i].append(Piece.Empty((i,j)))
        board[0] = w_pieces
        board[1] = w_pawns
        board[6] = b_pawns
        board[7] = b_pieces
        return board
    
    def update(self, start: Tuple[int, int], end: Tuple[int, int])-> List[List[Piece]]:
        if end in self.board[start[0]][start[1]].possible_moves(self.board):
            self.board[end[0]][end[1]] = self.board[start[0]][start[1]]
            self.board[start[0]][start[1]] = Piece.Empty(start)
        return self.board

    def convert_board_to_string(self)-> List[str]:
        board = []
        for i in range(8):
            row = ""
            for j in range(8):
                row += self.board[i][j].string_rep + ' '
            board.append(row)
        return board

