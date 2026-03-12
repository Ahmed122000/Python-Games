import tkinter as tk
from tkinter import ttk
from TicTacToe import TicTacToe

if __name__ == "__main__":
    root = tk.Tk()
    icon = tk.PhotoImage(file="./.screenshots/tictactoe_icon.png")
    TicTacToe(root)
    root.iconphoto(False, icon)
    root.mainloop()