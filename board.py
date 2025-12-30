class SudokuBoard:
    def __init__(self):
        self.grid = [[0]*9 for _ in range(9)]

    def load_puzzle(self, puzzle):
        for i in range(9):
            for j in range(9):
                self.grid[i][j] = puzzle[i][j]

    def is_valid(self, row, col, num):
        if num in self.grid[row]:
            return False

        for i in range(9):
            if self.grid[i][col] == num:
                return False

        box_r = (row // 3) * 3
        box_c = (col // 3) * 3
        for i in range(3):
            for j in range(3):
                if self.grid[box_r+i][box_c+j] == num:
                    return False

        return True
    def is_complete(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return False
        return True
    def is_valid_board(self):
        for r in range(9):
            for c in range(9):
                num = self.grid[r][c]
                if num != 0:
                    self.grid[r][c] = 0
                    if not self.is_valid(r, c, num):
                        self.grid[r][c] = num
                        return False
                    self.grid[r][c] = num
        return True
