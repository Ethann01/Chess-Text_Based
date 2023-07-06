from typing import List, Any, Tuple
from chess import Chess
from board import Board



class Piece:
    """abstract"""
    def __init__(self, coor: Tuple[int, int], side: str)-> None:
        self.coor = coor
        self.side = side
        
    def possible_moves(self, board: List[List[Piece]]):
        pass


class Pawn(Piece):
    def __init__(self, coor: Tuple[int, int], side: str)-> None:
        Piece.__init__(coor, side)
        if self.side == 'white':
            self.string_rep = "♙"
        else:
            self.string_rep = "♟"
        self.moved = False

    def capture(self, board: List[List[Piece]])-> List[Tuple[int, int]]:
        """Check if the pawn can capture and returns """
        #Pawn capturing: pawns can capture opposing pieces that are in front and 
        # directly, diagonally adjacent
        moves = []
        if self.side == 'white':
            if self.coor[1] - 1 >= 0:
                if not isinstance(board[self.coor[0] + 1][self.coor[1] - 1], (Empty, King):
                    moves.append(self.coor[0] + 1, self.coor[1] - 1)
            if self.coor[1] + 1 >= 0:
                if not isinstance(board[self.coor[0] + 1][self.coor[1] + 1], (Empty, King):
                    moves.append(self.coor[0] + 1, self.coor[1] + 1)

        if self.side == 'black':
            if self.coor[1] - 1 >= 0:
                if not isinstance(board[self.coor[0] - 1][self.coor[1] - 1], (Empty, King):
                    moves.append(self.coor[0] - 1, self.coor[1] - 1)
            if self.coor[1] + 1 >= 0:
                if not isinstance(board[self.coor[0] - 1][self.coor[1] + 1], (Empty, King):
                    moves.append(self.coor[0] - 1, self.coor[1] + 1)
        return moves

    def has_moved(self, counter: bool)-> bool:
        """Function to only be used for the pawn's En Passant rule"""
        self.moved = counter
        return self.moved

    def possible_moves(self, board: List[List[Piece]])-> List[Tuple[int, int]]:
        """Returns a list of self.board elements (tiles on the board) in which
        the pawn can move to."""
        moves = []

        #A pawn can always move one square forward from its position, provided the square that
        #is in front of it is vacant.
        if self.side == 'white':
            if isinstance(board[self.coor[0] + 1][self.coor[1]], Empty):
                moves.append((self.coor[0] + 1, self.coor[1]))
        elif self.side == 'black':
            if isinstance(board[self.coor[0] - 1][self.coor[1]], Empty):
                moves.append((self.coor[0] - 1, self.coor[1]))

        #Condition if the pawn has not yet moved (as it can move 2 squares forward as opposed to one)
        if self.coor[0] == 1 and self.side == 'white':
            if isinstance(board[3][self.coor[1]], Empty):
                moves.append((3, self.coor[1]))
        elif self.coor[0] == 6 and self.side == 'black':
            if isinstance(board[4][self.coor[1]], Empty):
                moves.append((4, self.coor[1]))
        moves += self.capture(board)
        return moves

class Rook(Piece):
    def __init__(self, coor: Tuple[int, int], side: str)-> None:
        Piece.__init__(coor, side)
        if self.side == 'white':
            self.string_rep = "♖"
        else:
            self.string_rep = "♜"
    
    def possible_moves(self, board: List[List[Piece]])-> List[Tuple[int, int]]:
        """4 variables, up, down, left, right to account for every direction the rook can move"""
        moves = []
        up = 7 - self.coor[0]
        down = self.coor[0] 
        left = self.coor[1] 
        right = 7 - self.coor[1]
        lst = [up, down, left, right]
        while not lst == [0,0,0,0]:
            up_coor = (7 - lst[0] + 1, self.coor[1])
            down_coor = (lst[1] - 1, self.coor[1])
            left_coor = (self.coor[0], lst[2] - 1)
            right_coor = (self.coor[0], 7 - lst[3] + 1)
            lst2 = [up_coor, down_coor, left_coor, right_coor]
            for i in range(4):
                if lst[i] != 0:
                    if not isinstance(board[lst2[i][0]][lst2[i][1]], King):
                        if isinstance(board[lst2[i][0]][lst2[i][1]], Empty):    
                            moves.append(lst2[i])
                            lst[i] -= 1
                        else:
                            if board[lst2[i][0]][lst2[i][1]].side != board[self.coor[0]][self.coor[1]].side:
                                moves.append(lst2[i])
                            lst[i] = 0
        return moves

class Bishop(Piece):
    def __init__(self, coor: Tuple[int, int], side: str)-> None:
        Piece.__init__(coor, side)
        if self.side == 'white':
            self.string_rep = "♗"
        else:
            self.string_rep = "♝"

    def possible_moves(self, board: List[List[Piece]])-> List[Tuple[int, int]]:
        """4 variables, up, down, left, right to account for every diagonal the bishop can move"""
        moves = []
        up = 7 - self.coor[0]
        down = self.coor[0] 
        left = self.coor[1] 
        right = 7 - self.coor[1]
        lst = [[up, left], [up, right], [down, left], [down, right]]
        
        while not ((0 in lst[0]) and (0 in lst[1]) and (0 in lst[2]) and (0 in lst[3])):
            upleft_coor = (7 - lst[0][0] + 1, lst[0][1] - 1)
            upright_coor = (7 - lst[1][0] + 1, 7 - lst[1][1] + 1)
            botleft_coor = (lst[2][0] - 1, lst[2][1] - 1)
            botright_coor = (lst[3][0] - 1, 7 - lst[3][1] + 1)
            lst2 = [upleft_coor, upright_coor, botleft_coor, botright_coor]

            for i in range(4):
                if not (lst[i][0] == 0 or lst[i][1] == 0):
                    if not isinstance(board[lst2[i][0]][lst2[i][1]], King):
                        if isinstance(board[lst2[i][0]][lst2[i][1]], Empty):    
                            moves.append(lst2[i])
                            lst[i][0] -= 1
                            lst[i][1] -= 1
                        else:
                            if board[lst2[i][0]][lst2[i][1]].side != board[self.coor[0]][self.coor[1]].side:
                                moves.append(lst2[i])
                            lst[i][0] = 0
        return moves
        
class Knight(Piece):
    def __init__(self, coor: Tuple[int, int], side: str)-> None:
        Piece.__init__(coor, side)
        if self.side == 'white':
            self.string_rep = "♘"
        else:
            self.string_rep = "♞"

    def possible_moves(self, board: List[List[Piece]])-> List[Tuple[int, int]]:
        all_moves = [(self.coor[0] + 2, self.coor[1] - 1), (self.coor[0] + 2, self.coor[1] + 1), \
            (self.coor[0] - 2, self.coor[1] - 1), (self.coor[0] - 2, self.coor[1] + 1), \
                (self.coor[0] - 1, self.coor[1] + 2), (self.coor[0] + 1, self.coor[1] + 2), \
                    (self.coor[0] - 1, self.coor[1] - 2), (self.coor[0] + 1, self.coor[1] - 2)]
        moves = []
        for pair in all_moves:
            if pair[0] >= 0 and pair[0] <= 7 and pair[1] >= 0 and pair[1] <= 7:
                if not isinstance(board[pair[0]][pair[1]], King):
                    if isinstance(board[pair[0]][pair[1]], Empty):
                        moves.append(pair)
                    else:
                        if board[pair[0]][pair[1]].side != board[self.coor[0]][self.coor[1]].side:
                            moves.append(pair)
        return moves

class Queen(Piece):
    def __init__(self, coor: Tuple[int, int], side: str)-> None:
        Piece.__init__(coor, side)
        if self.side == 'white':
            self.string_rep = "♕"
        else:
            self.string_rep = "♛"    
    
    def possible_moves(self, board: List[List[Piece]])-> List[Tuple[int, int]]:
        moves = []
        rook_moves = Rook((self.coor[0], self.coor[1]), self.side)
        moves += rook_moves.possible_moves(board)
        bishop_moves = Bishop((self.coor[0], self.coor[1]), self.side)
        moves += bishop_moves.possible_moves(board)
        return moves

                
class King(Piece):
    def __init__(self, coor: Tuple[int, int], side: str)-> None:
        Piece.__init__(coor, side)
        if self.side == 'white':
            self.string_rep = "♔"
        else:
            self.string_rep = "♚"  

    def check_enemy_king(self, sq: Tuple[int, int], board: List[List[Piece]])-> bool:
        """ Given a possible square the king can move to (that is empty), check if the enemy king is 
        adjacent as if the enemy king is nearby, the king cannot move to the given square.
        If True, then enemy king is nearby and sq is not a valid square for the king."""
        moves = [(sq[0] + 1, sq[1]), (sq[0] - 1, sq[1]), \
            (sq[0], sq[1] + 1), (sq[0], sq[1] - 1), \
                (sq[0] + 1, sq[1] + 1), (sq[0] + 1, sq[1] - 1), \
                    (sq[0] - 1, sq[1] + 1), (sq[0] - 1, sq[1] - 1)]
        for pair in moves:
            if isinstance(board[pair[0]][pair[1]], King):
                if board[pair[0]][pair[1]].side != piece.side:
                    return True
        return False
    
    def possible_moves(self, board: List[List[Piece]])-> List[Tuple[int, int]]:
        all_moves = [(self.coor[0] + 1, self.coor[1]), (self.coor[0] - 1, self.coor[1]), \
            (self.coor[0], self.coor[1] + 1), (self.coor[0], self.coor[1] - 1), \
                (self.coor[0] + 1, self.coor[1] + 1), (self.coor[0] + 1, self.coor[1] - 1), \
                    (self.coor[0] - 1, self.coor[1] + 1), (self.coor[0] - 1, self.coor[1] - 1)]

        moves = []

        for pair in all_moves:
            if pair[0] >= 0 and pair[0] <= 7 and pair[1] >= 0 and pair[1] <= 7:
                if isinstance(board[pair[0]][pair[1]], Empty):
                    if not self.check_enemy_king(pair, board):
                        moves.append(pair)
                else:
                    can_move = True
                    for row in board:
                        for square in row:
                            if square.side != self.side:
                                if isinstance(square, Pawn):
                                    """This distinction is important as the pawn can be in front of 
                                    the enemy king but the enemy king is not in check. It is not 
                                    enough to check that the enemy king is in a pawn's possible_moves,
                                    thus the capture method is required to look for possible checks."""
                                    if pair in square.capture(board):
                                        can_move = False
                                else:
                                    if pair in square.possible_moves(board):
                                        can_move = False
                    if can_move is True:
                        moves.append(pair)
        return moves
            
class Empty(Piece):
    def __init__(self, coor: Tuple[int, int], side: str = None):
        Piece.__init__(coor, side)
        self.string_rep = " "

    def possible_moves(self, board: List[List[Piece]]):
        return None

