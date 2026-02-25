
'''
class represent each cell on the board
row: row number of the cell 
col: column number of the cell
'''
class Cell:
    def __init__(self, row, col):
        self.row = row                  #row number
        self.col = col                  #column number
        self.is_mine = False            #is this cell mine
        self.is_revealed = False        #is this cell revealed 
        self.flagged = False            #??
        self.adjacent = 0               #number of adjacent mine cells