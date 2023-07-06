from typing import List, Tuple
from board import Board

class Chess:

    def __init__(self):
        self.board = Board()

    def input_to_coordinate(self, input: str)-> Tuple[int, int]:
        """converts chess tile names to list indices for searching and updating self.board"""
        letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
        for letter in letters:
            if input[0] == letter:
                col = letters.index(letter)
        return (int(input[1]) - 1, col)

    def __play(self):
        end = False
        while end is not True:
            for i in range(len(self.board.convert_board_to_string())):
                print(self.board.convert_board_to_string()[7 - i])
            

if __name__ == '__main__':