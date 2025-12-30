import tkinter as tk
import time
from constants import *

class Visualizer:
    def __init__(self, root):
        self.cells = [[None]*9 for _ in range(9)]
        frame = tk.Frame(root)
        frame.pack()

        for i in range(9):
            for j in range(9):
                e = tk.Entry(
                    frame,
                    width=2,
                    font=("Arial", 18),
                    justify="center",
                    relief="solid"
                )
                e.grid(row=i, column=j, padx=2, pady=2)
                self.cells[i][j] = e

    def update(self, board, row=None, col=None, backtrack=False):
        for i in range(9):
            for j in range(9):
                val = board.grid[i][j]
                self.cells[i][j].delete(0, tk.END)
                if val != 0:
                    self.cells[i][j].insert(0, str(val))
                self.cells[i][j]["bg"] = "white"
        if row is not None and col is not None:
            self.cells[row][col]["bg"] = "pink" if backtrack else "lightgreen"
            self.cells[row][col].update()

        time.sleep(DELAY)
