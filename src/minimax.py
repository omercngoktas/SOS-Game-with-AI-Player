import sys

class Minimax_Alpha_Beta:
    def __init__(self, board):
        self.board = board
        
    def evaluate(self, row, col, value):
        evaluation_result = self.board.evaluate(row, col, value)
        return evaluation_result

    def minimax(self, depth, alpha, beta, maximizingPlayer, row=None, col=None, value=None):
        made_moves = []
        return self.__minimax(depth, alpha, beta, maximizingPlayer, row, col, value, made_moves)

    def __minimax(self, depth, alpha, beta, maximizing_player, row=None, col=None, value=None, current_moves=None):
        if depth == 0 or self.board.is_game_over():
            score = self.evaluate(row, col, value)['score']
            return {'score': score, 'move': {'row': row, 'col': col, 'value': value}, 'moves': current_moves.copy()}

        if maximizing_player:
            max_eval = {'score': -sys.maxsize, 'move': None, 'moves': current_moves.copy()}
            for move in self.board.get_available_moves():
                row = move['available_move'][0]
                col = move["available_move"][1]
                value = move["value"]

                self.board.move(row, col, value)
                current_moves.append({'move': (row, col), 'value': value, 'player': 'max'})
                eval = self.__minimax(depth - 1, alpha, beta, False, row, col, value, current_moves)
                self.board.undo_move(row, col)
                
                if eval['score'] == 0:
                    random_move = self.board.get_best_move()
                    row = random_move['row']
                    col = random_move['col']
                    value = random_move['value']
                    eval['score'] = random_move['score']
                    current_moves.pop()
                    current_moves.append({'move': (row, col), 'value': value, 'player': 'max'})
                    eval['moves'] = current_moves.copy()
                
                check_score = self.board.check_score_for_move(row, col, value)
                if check_score != None and len(check_score) > 0:
                    max_eval['score'] = len(check_score)
                    max_eval['move'] = {'row': row, 'col': col, 'value': value}
                    max_eval['moves'] = current_moves.copy()
                    

                if eval['score'] > max_eval['score']:
                    max_eval['score'] = eval['score']
                    max_eval['move'] = {'row': row, 'col': col, 'value': value}
                    max_eval['moves'] = eval['moves']

                alpha = max(alpha, eval['score'])
                
                current_moves.pop()
                
                if beta <= alpha:
                    break
            return max_eval

        else:
            min_eval = {'score': -sys.maxsize, 'move': None, 'moves': current_moves.copy()}
            for move in self.board.get_available_moves():
                row = move['available_move'][0]
                col = move["available_move"][1]
                value = move["value"]

                self.board.move(row, col, value)
                current_moves.append({'move': (row, col), 'value': value, 'player': 'min'})
                eval = self.__minimax(depth - 1, alpha, beta, True, row, col, value, current_moves)

                if -eval['score'] < -min_eval['score']:
                    min_eval['score'] = eval['score']
                    min_eval['move'] = {'row': row, 'col': col, 'value': value}
                    min_eval['moves'] = eval['moves']

                beta = min(beta, -eval['score'])
                self.board.undo_move(row, col)
                current_moves.pop()
                
                if beta <= alpha:
                    break
            return min_eval