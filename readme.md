# Python Games Collection 🎮

A collection of classic arcade games built with Python and Tkinter. Currently featuring **Snake** and **Minesweeper** - with more games to come!

## 📋 Overview

This project is a growing collection of classic games implemented in Python using the built-in Tkinter library. Each game features a clean, minimalist design and smooth gameplay mechanics. The collection currently includes:

- **Classic Snake Game** 🐍 - Navigate, eat, and grow
- **Minesweeper** 💣 - Clear the minefield without detonating any mines

## 🎮 Games

### 1. Classic Snake Game
A modern take on the timeless Nokia classic. Control a snake, eat food, and grow while avoiding walls and your own tail.

**Features:**
- Smooth keyboard controls (arrow keys or WASD)
- Progressive difficulty - speed increases with score
- Pause/resume functionality
- Clean visuals with distinct colors
- Quick restart option

### 2. Minesweeper
The classic logic puzzle game where you must clear a minefield without triggering any mines.

**Features:**
- Fully customizable board (5-30 rows/columns, 1-200 mines)
- Left-click to reveal, right-click to flag
- Real-time timer and flag counter
- Guaranteed safe first click
- Visual feedback with explosion effect and numbered cells
- Win detection when all safe cells are revealed

## 📋 Requirements

- **Python 3.x** - Download from [python.org](https://www.python.org/)
- **Tkinter** - Usually comes pre-installed with Python

No additional packages or dependencies required!

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Ahmed122000/Python-Games.git
cd Python-Games
```
2. Navigate to your desired game folder:
   a.snake:
     ```bash
     cd Snake
     ```
   b.MineSweeper:
   ```bash
   cd MineSweeper
   ```
3. Run the game:
```bash
python main.py
```
## 🎮 How to Play

### Snake Game

| Key | Action |
|-----|--------|
| ↑ / W | Move Up |
| ↓ / S | Move Down |
| ← / A | Move Left |
| → / D | Move Right |
| SPACE | Pause/Resume |
| R | Restart (when game over) |

**Objective**: Eat red food squares to grow longer and increase your score. Avoid hitting walls or your own tail. The game speed increases as your score grows!

### Minesweeper

| Action | Description |
|--------|-------------|
| Left Click | Reveal a cell |
| Right Click | Place/remove a flag |
| Restart Button | Start new game |
| SpinBoxes | Adjust board size and mine count |

**Objective**: Clear all safe cells without clicking on any mines. Use numbered cells as clues - they show how many mines are adjacent. Flag cells you suspect contain mines.

## 🎯 Game Mechanics

### Snake Game
- Snake continuously moves in the current direction
- Eating food increases score and snake length
- Game speed progressively increases with score
- Game ends if snake hits walls or itself
- Real-time score display

### Minesweeper
- First click is always safe (and its neighbors won't contain mines)
- Numbers indicate adjacent mine count
- Flag counter shows remaining mines
- Timer starts on first click
- Win by revealing all non-mine cells
- Loss triggers explosion visual effect

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 👏 Acknowledgments

- Inspired by classic arcade games
- Built with Python's built-in Tkinter library
- Based on the Udemy course: ["Python Game Development"](https://www.udemy.com/course/master-python-game-development/)
- Thanks to all contributors and players!

## 🚧 Coming Soon

More classic games are in development! Stay tuned for:
- Tic-Tac-Toe
- Pong
- Tetris
- And more!
