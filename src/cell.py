class Cell:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.value = "_"
    
    def get_position(self):
        return (self.row, self.col)

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
    
    def __str__(self) -> str:
        return f'Cell: {self.row} x {self.col} = {self.value}'