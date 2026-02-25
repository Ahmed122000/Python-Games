import tkinter as tk
from mineSweeper import MineSweeper

if __name__ == "__main__":
    root = tk.Tk()
    app = MineSweeper(root, rows=9, cols=9, mines=10)
    root.mainloop()