import sys
from cell import Cell
from random import randint

class Board:
    def __init__(self, height=5, width=5):
        self.height = height
        self.width = width
        self.cells = []
        self.made_moves = []
    
    # create the board with cells 
    def create_board(self):
        # create cells for the board (with row and col values)
        for row in range(self.height):
            for col in range(self.width):
                cell = Cell(row + 1, col + 1)
                self.add_cell(cell)
        # fill the corner cells with a value (with S by default)    
        self.fill_corner_cells()
        
    # filling the corner cells with a value (with S by default)
    def fill_corner_cells(self, value="S"):
        self.change_cell_value(1, 1, value)
        self.change_cell_value(1, self.width, value)
        self.change_cell_value(self.height, 1, value)
        self.change_cell_value(self.height, self.width, value)
    
    # add a cell to the board
    def add_cell(self, cell):
        self.cells.append(cell)
    
    # print the board
    def print_board(self):
        current_row = 1
        row_first_time = True
        col_first_time = True
        
        for cell in self.cells:
            # print column numbers
            if row_first_time:
                print("  ", end = '')
                for col in range(self.width):
                    print(col + 1, end = ' ')
                print()    
                row_first_time = False
            # print row numbers and cell values
            if cell.row == current_row:
                # print row numbers
                if col_first_time:
                    print(cell.row, end = ' ')
                    col_first_time = False
                # print cell values
                print(cell.value, end = ' ')
            # print new line and row numbers
            else:
                print("\n" + str(cell.row) + " " + cell.value, end = ' ')
                current_row += 1
        print("\n")
    
    # change the value of a cell in the board
    def change_cell_value(self, row, col, value):
        for cell in self.cells:
            if (cell.row == row) and (cell.col == col):
                if cell.value == "_":
                    cell.set_value(value)
                    # print("Cell value changed")
                    return True
                else:
                    cell.set_value(value)
                    # print("Cell already has a value")
        return False
    
    def get_available_moves(self):
        return self.__available_moves()
        
    # returns a list of available moves
    def __available_moves(self):
        available_moves = []
        for cell in self.cells:
            if cell.value == "_":
                available_moves.append({"available_move": (cell.row, cell.col), "value": "O"})
                available_moves.append({"available_move": (cell.row, cell.col), "value": "S"})
        return available_moves
    
    # display available moves
    def display_available_moves(self):
        available_moves = self.available_moves()
        print("Available moves:")
        for move in available_moves:
            print(move.get_position(), end = ' ')
        print()
    
    # check if a move is valid
    def check_if_move_is_valid(self, row, col):
        for cell in self.cells:
            if (cell.row == row) and (cell.col == col):
                if cell.value == "_":
                    return True
                else:
                    return False
        return False
    
    # returns a list of neighbours of a cell
    def get_neighbours(self, row, col):
        neighbours = {}
        # check the top left corner cell
        if (row > 1) and (col > 1):
            neighbours.update({"top left": (row - 1, col - 1)})
        else:
            neighbours.update({"top left": None})
        # check the top cell
        if (row > 1):
            neighbours.update({"top": (row - 1, col)})
        else:
            neighbours.update({"top": None})
        # check the top right corner cell
        if (row > 1) and (col < self.width):
            neighbours.update({"top right": (row - 1, col + 1)})
        else:
            neighbours.update({"top right": None})
        # check the left cell
        if (col > 1):
            neighbours.update({"left": (row, col - 1)})
        else:
            neighbours.update({"left": None})
        # check the right cell
        if (col < self.width):
            neighbours.update({"right": (row, col + 1)})
        else:
            neighbours.update({"right": None})
        # check the bottom left corner cell
        if (row < self.height) and (col > 1):
            neighbours.update({"bottom left": (row + 1, col - 1)})
        else:
            neighbours.update({"bottom left": None})
        # check the bottom cell
        if (row < self.height):
            neighbours.update({"bottom": (row + 1, col)})
        else:
            neighbours.update({"bottom": None})
        # check the bottom right corner cell
        if (row < self.height) and (col < self.width):
            neighbours.update({"bottom right": (row + 1, col + 1)})
        else:
            neighbours.update({"bottom right": None})
        return neighbours
    
    # display neighbours of a cell
    def display_neighbours(self, row, col):
        neighbours = self.get_neighbours(row, col)
        print(f"Neighbours of cell ({row}, {col}):")
        for key, value in neighbours.items():
            print(f"{key}: {value}")
        
    # if a move is want to be made, check if the move gives a score
    def check_score_for_move(self, row, col, value):
        # get the neighbours of the current cell
        neighbours = self.get_neighbours(row, col)
        move_with_score = []
        
        if value == "S":
            # check for every direction
            for direction in neighbours:
                # check if the neighbour exists
                if neighbours[direction] != None:
                    # get the cell in the current direction
                    cell_in_direction = self.cells[(neighbours[direction][0] - 1) * self.width + (neighbours[direction][1] - 1)]
                    # check if the cell in the current direction has the value "O", then "S" will be checked
                    if cell_in_direction.get_value() == "O":
                        # get the neighbours of the cell in the current direction
                        neighbours_of_cell_in_direction = self.get_neighbours(cell_in_direction.row, cell_in_direction.col)
                        # check if the neighbour of the cell in the current direction exists
                        if neighbours_of_cell_in_direction[direction] != None:
                            # get the value of the neighbour of the cell in the current direction
                            value_of_cell_direction_direction = self.cells[(neighbours_of_cell_in_direction[direction][0] - 1) * self.width + (neighbours_of_cell_in_direction[direction][1] - 1)].get_value()
                            # check if the value of the neighbour of the cell in the current direction is "S"
                            if value_of_cell_direction_direction == "S":
                                # return {"score": 1, "direction": direction, "path": ((row, col), (neighbours[direction][0], neighbours[direction][1]), (neighbours_of_cell_in_direction[direction][0], neighbours_of_cell_in_direction[direction][1]))}
                                move_with_score.append({"score": 1, "value": value, "cell_to_play": (row, col), "direction": direction, "path": ((row, col), (neighbours[direction][0], neighbours[direction][1]), (neighbours_of_cell_in_direction[direction][0], neighbours_of_cell_in_direction[direction][1]))})
                                
        elif value == "O":
            if neighbours["top left"] != None and neighbours["bottom right"] != None:
                top_left_cell = self.cells[(neighbours["top left"][0] - 1) * self.width + (neighbours["top left"][1] - 1)]
                bottom_right_cell = self.cells[(neighbours["bottom right"][0] - 1) * self.width + (neighbours["bottom right"][1] - 1)]
                if top_left_cell.get_value() == "S" and bottom_right_cell.get_value() == "S":
                    # return {"score": 1, "direction": "top left", "path": ((neighbours["top left"][0], neighbours["top left"][1]), (row, col), (neighbours["bottom right"][0], neighbours["bottom right"][1]))}
                    move_with_score.append({"score": 1, "value": value, "cell_to_play": (row, col), "direction": "top left", "path": ((neighbours["top left"][0], neighbours["top left"][1]), (row, col), (neighbours["bottom right"][0], neighbours["bottom right"][1]))})
                    
            if neighbours["top"] != None and neighbours["bottom"] != None:
                top_cell = self.cells[(neighbours["top"][0] - 1) * self.width + (neighbours["top"][1] - 1)]
                bottom_cell = self.cells[(neighbours["bottom"][0] - 1) * self.width + (neighbours["bottom"][1] - 1)]
                if top_cell.get_value() == "S" and bottom_cell.get_value() == "S":
                    # return {"score": 1, "direction": "top", "path": ((neighbours["top"][0], neighbours["top"][1]), (row, col), (neighbours["bottom"][0], neighbours["bottom"][1]))}
                    move_with_score.append({"score": 1, "value": value, "cell_to_play": (row, col), "direction": "top", "path": ((neighbours["top"][0], neighbours["top"][1]), (row, col), (neighbours["bottom"][0], neighbours["bottom"][1]))})
                    
            
            if neighbours["top right"] != None and neighbours["bottom left"] != None:
                top_right_cell = self.cells[(neighbours["top right"][0] - 1) * self.width + (neighbours["top right"][1] - 1)]
                bottom_left_cell = self.cells[(neighbours["bottom left"][0] - 1) * self.width + (neighbours["bottom left"][1] - 1)]
                if top_right_cell.get_value() == "S" and bottom_left_cell.get_value() == "S":
                    # return {"score": 1, "direction": "top right", "path": ((neighbours["bottom left"][0], neighbours["bottom left"][1]), (row, col), (neighbours["top right"][0], neighbours["top right"][1]))}
                    move_with_score.append({"score": 1, "value": value, "cell_to_play": (row, col), "direction": "top right", "path": ((neighbours["bottom left"][0], neighbours["bottom left"][1]), (row, col), (neighbours["top right"][0], neighbours["top right"][1]))})
            
            if neighbours["left"] != None and neighbours["right"] != None:
                left_cell = self.cells[(neighbours["left"][0] - 1) * self.width + (neighbours["left"][1] - 1)]
                right_cell = self.cells[(neighbours["right"][0] - 1) * self.width + (neighbours["right"][1] - 1)]
                if left_cell.get_value() == "S" and right_cell.get_value() == "S":
                    # return {"score": 1, "direction": "left", "path": ((neighbours["left"][0], neighbours["left"][1]), (row, col), (neighbours["right"][0], neighbours["right"][1]))}
                    move_with_score.append({"score": 1, "value": value, "cell_to_play": (row, col), "direction": "left", "path": ((neighbours["left"][0], neighbours["left"][1]), (row, col), (neighbours["right"][0], neighbours["right"][1]))})
                    
        if len(move_with_score) == 0:
            return None
        else:
            return move_with_score
            
    # get the best move to make
    def get_best_move(self):
        available_moves = self.get_available_moves()
        best_move = None
        best_move_score = -sys.maxsize
        for move in available_moves:
            move_score = self.evaluate(move["available_move"][0], move["available_move"][1], move["value"])["score"]
            if move_score > best_move_score:
                best_move_score = move_score
                best_move = move
        
        if best_move_score == 0:
            random_move = available_moves[randint(0, len(available_moves) - 1)]
            row = random_move["available_move"][0]
            col = random_move["available_move"][1]
            value = random_move["value"]
            return {'row': row, 'col': col, 'value': value, 'score': 0}
        
        row = best_move["available_move"][0]
        col = best_move["available_move"][1]
        value = best_move["value"]
        
        return {'row': row, 'col': col, 'value': value, 'score': best_move_score}
    
    # get the best move to make
    def get_random_move(self):
        available_moves = self.get_available_moves()
        random_move = available_moves[randint(0, len(available_moves) - 1)]
        row = random_move["available_move"][0]
        col = random_move["available_move"][1]
        value = random_move["value"]
        score = self.check_score_for_move(row, col, value)
        if score == None:
            score = 0
        else:
            score = len(score)
        return {'row': row, 'col': col, 'value': value, 'score': score}
    
    def move(self, row, col, value):
        if self.check_if_move_is_valid(row, col):
            self.change_cell_value(row, col, value)
            self.made_moves.append((row, col))
            return True
        else:
            return False
        
    def undo_move(self, row, col):
        self.change_cell_value(row, col, "_")
        
    def is_game_over(self):
        available_moves = self.get_available_moves()
        if len(available_moves) == 0:
            return True
        else:
            return False
        
    def evaluate(self, row, col, value):
        score_for_move = self.check_score_for_move(row, col, value)
        
        if score_for_move != None:
            return {'row': row, 'col': col, 'value': value, 'score': len(score_for_move)}
        
        else:
            return {'row': row, 'col': col, 'value': value, 'score': 0}
        
    def alpha_beta_pruning(self, depth, alpha, beta, maximizing_player, row=None, col=None, value=None):
        if depth == 0 or self.is_game_over():
            return self.evaluate(row, col, value)
        
        if maximizing_player:
            max_eval = -sys.maxsize
            for move in self.get_available_moves():
                self.move(move["available_move"][0], move["available_move"][1], move["value"])
                
                eval = self.alpha_beta_pruning(depth - 1, alpha, beta, False, move["available_move"][0], move["available_move"][1], move["value"])
                
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                self.undo_move(move["available_move"][0], move["available_move"][1])
                if beta <= alpha:
                    break
            return max_eval
        
        else:
            min_eval = sys.maxsize
            for move in self.get_available_moves():
                self.move(move["available_move"][0], move["available_move"][1], move["value"])
                eval = self.alpha_beta_pruning(depth - 1, alpha, beta, True, move["available_move"][0], move["available_move"][1], move["value"])
                
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                self.undo_move(move["available_move"][0], move["available_move"][1])
                if beta <= alpha:
                    break
            return min_eval