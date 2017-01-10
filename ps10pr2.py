# Devin Cheong
# devin@bu.edu
#
# ps10pr2.py (Problem Set 10, Problem 2)
#
# A Connect-Four Player class 
#

from ps10pr1 import Board

# write your class below


class Player:
    """ a data type for a Connect Four player object
    """
    def __init__(self, checker):
        """constructor for Player Objects
        """
        assert(checker == 'X' or checker == 'O')
        
        self.checker = checker
        self.num_moves = 0


    def __repr__(self):
        """string
        """
        s = 'Player ' + self.checker
        return s


    def opponent_checker(self):  
        """returns 1 character string representing the checker of the
        Player object's opponent
        """
        if self.checker == 'X':
            return 'O'
        else:
            return 'X'


    def next_move(self, board):
        """ accepts a Board object as a parameter and returns the
        column where the player wants to make the next move. To do this, the
        method should ask the user to enter a column number that
        represents where the user wants to place a checker on the board.
        The method should repeatedly ask for a column number until
        a valid column number is given.
        """
        x = int(input('Enter a column: '))
        while not board.can_add_to(x):
            print('Try again!')
            x = int(input('Enter a column: '))
            
        
        self.num_moves += 1
        return x
            
        
        
        
        
        
