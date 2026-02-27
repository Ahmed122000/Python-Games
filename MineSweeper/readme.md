# Minesweeper Game

A classic Minesweeper game built with Python and tkinter. This implementation features a customizable grid, real-time timer, flagging system, and the traditional Minesweeper gameplay mechanics


## 🎮 Features

- **Smooth Controls**: Responsive keyboard controls with arrow keys or WASD
- **Progressive Difficulty**: Game speed increases as your score grows
- **Score Tracking**: Real-time score display
- **Game States**: Pause/resume functionality and game over detection
- **Clean Visuals**: Minimalist design with distinct colors for snake head, body, and food
- **Quick Restart**: Press 'R' to restart after game over

## 🎯 How to Play
1. **🎮 Classic Minesweeper Gameplay** - Left-click to reveal cells, right-click to flag potential mines
2. **📏 Customizable Board** - Adjust rows (5-30), columns (5-30), and mine count (1-200)
3. **⏱️ Real-time Timer** - Tracks your progress from the first click
4. **🚩 Flag Counter** - Displays remaining mines based on placed flags
5. **🎯 Safe First Click** - First click is guaranteed to be safe (and its neighbors won't contain mines)
6. **🏆 Win Detection** - Automatically detects when all non-mine cells are revealed
7. **💥 Visual Feedback** - Explosion effect when hitting a mine, numbered cells for adjacent mines
8. **🔄 Restart Functionality** - Easy restart with current or new settings

## 📋 Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

No additional packages are required!

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/Ahmed122000/Python-Games.git
cd MineSweeper
```
2. Run the game:
```bash
python main.py
```
## 🎮 Controls

| Key | Action |
|-----|--------|
| Left Click | Reveal a cell |
| Right Click | Place/remove a flag on a cell |
| Restart Button | Start a new game |
| SpinBoxes | Adjust board size and mine count |

## 📝 License

This project is open source and available under the [MIT License](../LICENSE).

## 👏 Acknowledgments

- Built with Python's built-in Tkinter library
- Based on the Udemy course: ["Python Game Development"](https://www.udemy.com/course/master-python-game-development/)
