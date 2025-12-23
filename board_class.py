
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
    
    def calculate_adjacent_mines(self):

        for r in range(self.rows):
            for c in range(self.cols):
                current_cell = self.grid[r][c]
                
                if not current_cell.mine:
                    mine_count = 0

                    neighbor_coords = self.get_neighbors(r, c)
                    for new_r, new_c in neighbor_coords:

                        neighbor_cell = self.grid[new_r][new_c]

                        if neighbor_cell.mine:
                            mine_count += 1

                    current_cell.adjacent_mines = mine_count


    def place_mines(self, num_mines, row_mine, col_mine):
        num_mines = 0

        def choose_mine_cell():
            row_mine = random.randint(0, self.rows - 1)
            col_mine = random.randint(0, self.cols - 1)
            return row_mine, col_mine

        while num_mines < self.num_mines:
            choose_mine_cell()

            chosen_cells = [] #List to store already chosen cells

            possible_cell = self.grid[row_mine][col_mine]

            if possible_cell not in chosen_cells:
                chosen_cells.append(possible_cell)
            
            elif possible_cell in chosen_cells:
                continue  
