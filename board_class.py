class board:
    def __init__(self, rows, cols, num_mines):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.grid = []
    
    def get_cell_at_position(self):
        for r in range(self.rows):
            for c in range(self.cols):
                cell = self.grid[r][c]

                cell_rect = cell.get_rect()

                if cell_rect.collidepoint(mouse_x, mouse_y): # Define mouse_x, mouse_y variables later
                    return cell         #Return the cell that was clicked based on mouse position
        return None                     #Otherwise, return None if no cell was clicked
    
    def get_neighbors(self, r, c):
        neighbors = []

        for dr in range(-1, 2):
            for dc in range(-1, 2):

                if dr == 0 and dc == 0: #Skips the center cell.
                    continue

                new_r = r + dr
                new_c = c + dc

                is_valid_row = (0 <= new_r < self.rows)
                is_valid_col = (0 <= new_c < self.cols)

                if is_valid_row and is_valid_col:
                    neighbors.append([new_r][new_c])

        return neighbors


    def place_mines(self):
        ...
    
    def calculate_adjacent_mines(self):
        ...
    
