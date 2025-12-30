class SudokuSolver:
    def solve(self, board, visualizer=None):
        for row in range(9):
            for col in range(9):
                if board.grid[row][col] == 0:
                    for num in range(1, 10):
                        if board.is_valid(row, col, num):
                            board.grid[row][col] = num

                            if visualizer:
                                visualizer.update(board, row, col)
                            
                            if self.solve(board, visualizer):
                                return True

                            board.grid[row][col] = 0  # backtrack
                            if visualizer:
                                visualizer.update(board, row, col, backtrack=True)
                    
                    return False
        return True
