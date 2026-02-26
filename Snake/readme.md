# Classic Snake Game 🐍

A modern implementation of the classic Snake game built with Python and Tkinter. Navigate the snake to eat food, grow longer, and achieve the highest score possible!

![Snake Game Demo](snake_demo.gif)

## 🎮 Features

- **Smooth Controls**: Responsive keyboard controls with arrow keys or WASD
- **Progressive Difficulty**: Game speed increases as your score grows
- **Score Tracking**: Real-time score display
- **Game States**: Pause/resume functionality and game over detection
- **Clean Visuals**: Minimalist design with distinct colors for snake head, body, and food
- **Quick Restart**: Press 'R' to restart after game over

## 🎯 How to Play

1. **Start the game**: Run the Python script
2. **Control the snake**: Use arrow keys (↑ ↓ ← →) to change direction
3. **Eat food**: Navigate to the red food square to grow and increase your score
4. **Avoid obstacles**: Don't hit the walls or the snake's own body
5. **Manage speed**: The game gets faster as you eat more food
6. **Pause if needed**: Press SPACE to pause/resume the game

## 📋 Requirements

- Python 3.x
- Tkinter (usually comes pre-installed with Python)

No additional packages are required!

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/snake-game.git
cd snake-game
```
2. Run the game:
```bash
python main.py
```
## 🎮 Controls

| Key | Action |
|-----|--------|
| ↑ / W | Move Up |
| ↓ / S | Move Down |
| ← / A | Move Left |
| → / D | Move Right |
| SPACE | Pause/Resume |
| R | Restart (when game over) |

## 🎯 Game Mechanics

- **Snake Movement**: The snake continuously moves in the current direction
- **Food Consumption**: Eating food increases score and snake length
- **Speed Progression**: Game speed increases with each food eaten (minimum speed cap)
- **Collision Detection**: Game ends if snake hits walls or itself
- **Score Display**: Current score shown in real-time

## 📝 License

This project is open source and available under the [MIT License](../LICENSE).

## 👏 Acknowledgments

- Inspired by the classic Nokia Snake game
- Built with Python's built-in Tkinter library
- Based on the Udemy course: ["Python Game Development"](https://www.udemy.com/course/master-python-game-development/)
