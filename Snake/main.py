import tkinter as tk
from snake import SnakeGame
if __name__ == "__main__":
    root = tk.Tk()
    app = SnakeGame(root)
    root.mainloop()