class game:
    def __init__(self, rows, cols, num_mines, cell_size):
        self.rows = rows
        self.cols = cols
        self.num_mines = num_mines
        self.cell_size = cell_size
        self.board = board(rows, cols, num_mines)
        self.cell = cell(...) # Fill in later

    def run(self):
        ... #Main game loop

    def handle_click(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                ...
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.board.get_cell_at_position()
                self.cell.handle_mouse_input()
    #Define mouse_x, mouse_y variables
