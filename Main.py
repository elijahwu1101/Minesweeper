import pygame
import random
pygame.init()

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
LIGHT_BLUE = (173, 216, 230)
RED = (255, 0, 0)

#Setting up screen
screen_width = 300
screen_height = screen_width
screen = pygame.display.set_mode((screen_width, screen_height))

#Should store data about itself, such as whether it contains a mine, uncovered/covered/flagged, number of adjacent mines
#
class cell:
    def __init__(self, row, col, x, y, size, border_width):
        self.col = col
        self.row = row
        self.size = screen_width // 10
        self.x = x
        self.y = y

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
        return pygame.Rect(
            self.x,
            self.y,
            self.size,
            self.size
        )
        
    def draw(self, screen):
        border_width = 8
        rect = self.get_rect()

        if self.state == "covered":
            pygame.draw.rect(screen, LIGHT_BLUE, rect, border_width) #Drawing a covered cell

        elif self.state == "uncovered":
            pygame.draw.rect(screen, GRAY, rect, border_width)
            if self.mine:
                pygame.draw.circle(screen, BLACK, rect.center, self.size // 2, width=0) #Drawing if a mine is clicked
            
            elif self.adjacent_mines > 0:
                number = str(self.adjacent_mines)
                font = pygame.font.SysFont(None, self.size)
                display_number = font.render(number, True, BLACK)
                screen.blit(screen, (self.x, self.y))

        elif self.state == "flagged":
            pygame.draw.rect(screen, RED, rect, border_width)
        

class board:
    def __init__(self, rows, cols, num_mines):
        self.row = rows
        self.col = cols
        self.num_mines = num_mines

        for r in range(self.row):
            rows = []
            for c in range(self.col):
                ...                     #Instance of cell class 

class game:
    ...


