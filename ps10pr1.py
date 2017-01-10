# Devin Cheong
# devin@bu.edu
#
# ps10pr1.py - Connect Four Board class
# IT WORKS 


class Board:
    """ a data type for a Connect Four board with
    arbitrary dimensions
    """
    def __init__(self, height, width):
        """ a constructor for Board objects """
        self.height = height
        self.width = width
        self.slots = [[' '] * self.width for row in range(self.height)]




    def __repr__(self):
        """ returns a string representation of a Board
        """
        s = '' # begin with an empty string
        
        for row in range(self.height):
            s += '|'
            
            for col in range(self.width):
                s += self.slots[row][col] + '|'
                
            s += '\n'

        s += '-'*self.width + '-'*self.width  + '-' + '\n' + ' '
        for i in range(self.width):
            i = i % 10
            s += str(i) + ' '
    
        return s



    def add_checker(self, checker, col):
        """ adds the specified checker to column col
        of the called Board object
        """
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)
        
        row = 0
        while self.slots[row][col] == ' ':
            if row + 1 >= self.height:
                break
            row += 1
        if self.slots[row][col] == 'X' or self.slots[row][col] == 'O':
            self.slots[row-1][col] = checker
        else:
            self.slots[row][col] = checker
            
        

    def reset(self):
        """resets the Board object to become empty af
        """
        for i in range(self.height):
            for j in range(self.width):
                self.slots[i][j] = ' '



    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
        checkers in those columns of the called Board object, 
        starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'

        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)

            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'



    def can_add_to(self,col):
        """returns True if it is valid to place a checker in the column col on
        the calling Board object. Otherwise, it should return False.
        """
        if col < 0 or col >= self.width:
            return False
        for i in range(self.height):
            if self.slots[i][col] != ' ':
                return False
            else:
                return True



    def is_full(self):
        """returns True if board is full
        False otherwise
        """
        x=0
        for i in range(self.height):
            for j in range(self.width):
                if self.slots[i][j] == ' ':
                    x += 1

        if x > 0:
            return False
        else:
            return True


    def remove_checker(self, col):
        """Removes top checker from col
        if empty, do nothing
        """
        for i in range(self.height):
            if self.slots[i][col] != ' ':
                self.slots[i][col] = ' '
                break


    def is_win_for(self, checker):
        """takes 'X' or 'O' as checker and returns True if it wins, False if it loses
        """
        assert(checker == 'X' or checker == 'O')

        # call helper functions
        if self.is_horizontal_win(checker) == True or self.is_vertical_win(checker) == True or self.is_down_diagonal_win(checker) == True or self.is_up_diagonal_win(checker) == True:
            return True
        else:
            return False


    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True

        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ check for vertical win for X or O
        """
        for i in range(self.height-3):
            for col in range(self.width):
                if self.slots[i][col] == checker and \
                   self.slots[i+1][col] == checker and \
                   self.slots[i+2][col] == checker and \
                   self.slots[i+3][col] == checker:
                    return True


        return False


    def is_down_diagonal_win(self, checker):
        """ check for down diagonal win from left to right
        """
        for row in range(self.height-3):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row+1][col+1] == checker and \
                   self.slots[row+2][col+2] == checker and \
                   self.slots[row+3][col+3] == checker:
                    return True

        return False


    def is_up_diagonal_win(self, checker):
        """ check for up diagonal win from left to right
        """
        for row in range(3, self.height):
            for col in range(self.width - 3):
                if self.slots[row][col] == checker and \
                   self.slots[row-1][col+1] == checker and \
                   self.slots[row-2][col+2] == checker and \
                   self.slots[row-3][col+3] == checker:
                    return True

        return False
                
        
        

        
                
        
        
             
        
