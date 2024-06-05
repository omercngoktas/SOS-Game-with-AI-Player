import sys

class Player:
    def __init__(self, player_type, depth, minimax, board):
        self.depth = depth
        self.player_type = player_type
        self.score = 0
        self.board = board
        self.minimax = minimax
    
    def play(self):
        if self.player_type == 'max':
            return self.__play()
        else:
            return self.__play()
        
    def __play(self):
        if self.player_type == 'max':
            max_possible_score = self.board.get_best_move()
            mps_row = max_possible_score['row']
            mps_col = max_possible_score['col']
            mps_value = max_possible_score['value']
            mps_gained_score = self.board.check_score_for_move(mps_row, mps_col, mps_value)
            mps_gained_score = len(mps_gained_score) if mps_gained_score != None else 0
            
            result = self.minimax.minimax(4, -sys.maxsize, sys.maxsize, True if self.player_type == 'max' else False)
            mm_row = result['move']['row']
            mm_col = result['move']['col']
            mm_value = result['move']['value']
            mm_gained_score = self.board.check_score_for_move(mm_row, mm_col, mm_value)
            mm_gained_score = len(mm_gained_score) if mm_gained_score != None else 0
            
            if mm_gained_score != None:
                if mps_gained_score > mm_gained_score:
                    row = mps_row
                    col = mps_col
                    value = mps_value
                    gained_score = mps_gained_score
                    
                else:
                    row = mm_row
                    col = mm_col
                    value = mm_value
                    gained_score = mm_gained_score
            
            if mm_gained_score == None:
                random_move = self.board.get_random_move()
                rm_row = random_move['row']
                rm_col = random_move['col']
                rm_value = random_move['value']
                rm_gained_score = self.board.check_score_for_move(rm_row, rm_col, rm_value)
                rm_gained_score = len(rm_gained_score) if rm_gained_score != None else 0
            
                row = rm_row
                col = rm_col
                value = rm_value
                gained_score = rm_gained_score
            
        else:
            result = self.minimax.minimax(4, -sys.maxsize, sys.maxsize, True if self.player_type == 'max' else False)
            row = result['move']['row']
            col = result['move']['col']
            value = result['move']['value']
            
            gained_score = self.board.check_score_for_move(row, col, value)
            gained_score = len(gained_score) if gained_score != None else 0
            if gained_score == 0:
                random_move = self.board.get_random_move()
                row = random_move['row']
                col = random_move['col']
                value = random_move['value']
                gained_score = self.board.check_score_for_move(row, col, value)
                gained_score = len(gained_score) if gained_score != None else 0
            
        self.board.move(row, col, value)
        self.set_score(gained_score)
    
    def get_score(self):
        return self.score
    
    def set_score(self, score):
        self.score += score
        
    def __str__(self):
        return self.player_type + " player -> depth: " + str(self.depth) + " | score: " + str(self.score)
    