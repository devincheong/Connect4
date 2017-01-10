# Devin Cheong
# devin@bu.edu
#
# ps10pr4.py (Problem Set 10, Problem 4)
#
# AI Player for use in Connect Four
#

import random  
from ps10pr3 import *


class AIPlayer(Player):
    """
    """

    def __init__(self, checker, tiebreak, lookahead):
        """ init for AIPlayer
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        super().__init__(checker)

        self.tiebreak = tiebreak
        self.lookahead = lookahead


    def __repr__(self):
        """new repr for AIPlayer
        """
        s = 'Player ' + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s


    def max_score_column(self, scores):
        """index of max score of column 
        """
        x = max(scores)
        list = []
        for c in range(0, len(scores)):
            if scores[c] == x:
                list += str(c)
        if self.tiebreak == 'LEFT':
            return int(list[0])
        elif self.tiebreak == 'RIGHT':
            return int(list[-1])
        else:
            return int(random.choice(list)) 
            
    

    def scores_for(self, board):
        """returns scores of each column in a list of yours and opponent
        """
        scores = [50] * board.width

        for col in range(board.width):
            if not board.can_add_to(col):
                scores[col] = -1
            elif board.is_win_for(self.checker):
                scores[col] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[col] = 0
            elif self.lookahead == 0:
                scores[col] = 50
            else:              
                board.add_checker(self.checker, col)
                opponent = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opponent.scores_for(board)
                if max(opp_scores) == 100:
                    scores[col] = 0
                elif max(opp_scores) == 0:
                    scores[col] = 100
                else:
                    scores[col] = 50
                board.remove_checker(col)

        return scores


    def next_move(self, board):
        """next move for the AIPlayer overriding class Player
        """
        x = self.max_score_column(self.scores_for(board))
        self.num_moves += 1
        return x
        

                    
                
                
          
    
    

        
