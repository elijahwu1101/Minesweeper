#Should store data about itself, such as whether it contains a mine, uncovered/covered/flagged, number of adjacent mines
#
class cell:
    def __init__(self, row, col, x, y, size):
        self.col = col
        self.row = row

        self.mine = False        #First set to False, then if cell is selected, change it to True
        self.state = "covered"   #Possible states: flagged, covered, uncovered
        self.adjacent_mines = 0  #Number of mines in cells next to it, integers 0 - 8

    def place_mine(self):        #Later in class board, when placing mines randomly, call this method
        self.mine = True
    
    def reveal(self):
        if self.state == "uncovered" or self.state == "flagged": 
            return "ALREADY_UNCOVERED_OR_FLAGGED"
        
        self.state = "uncovered" #Otherwise, chagne the self.state to uncovered
        
        if self.mine:
            return "MINE_IS_HIT"
        
        elif self.adjacent_mines == 0:   #If there are no adjacent mines, return this value to show keep revealing adjacent cells until it his a cell that has a mine next to it
            return "NO_ADJACENT_MINES"
        
        else:                            #If the cell that has been clicked is one with numbers 1-8. 
            return "CELL_WITH_NUMBER_REVEALED"
    
    def toggle_flag(self):
        if self.state == "covered":
            self.state = "flagged"
        elif self.state == "flagged":
            self.state = "covered"
        else:
            pass        #Don't do anything if the self.state is not covered or flagged (e.g., uncovered --> dont do anything, because its uncovered)
            
    def get_rect(self):
        ...
    
    def draw(self, screen):
        ...
