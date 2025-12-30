import tkinter as tk
from tkinter import messagebox
from board import SudokuBoard
from solver import SudokuSolver
from visualizer import Visualizer
from puzzles import PUZZLES
root = tk.Tk()
root.title("Sudoku Solver - DFS Backtracking")
board = SudokuBoard()
board.load_puzzle(PUZZLES[0])

visualizer = Visualizer(root)
visualizer.update(board)
solver = SudokuSolver()

def solve_sudoku():
    solver.solve(board, visualizer)


def check_solution():
   
    for i in range(9):
        for j in range(9):
            val = visualizer.cells[i][j].get()
            board.grid[i][j] = int(val) if val.isdigit() else 0

    if not board.is_complete():
        messagebox.showwarning("Sudoku", "Sudoku is not complete yet!")
    elif board.is_valid_board():
        messagebox.showinfo("Sudoku", "🎉 Congratulations! Correct solution.")
    else:
        messagebox.showerror("Sudoku", "❌ Incorrect solution. Try again.")

solve_btn = tk.Button(root, text="Solve", width=15, command=solve_sudoku)
solve_btn.pack(pady=8)
check_btn = tk.Button(root, text="Check Solution", width=15, command=check_solution)
check_btn.pack(pady=5)

root.mainloop()
