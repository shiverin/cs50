# 🎯 TicTacToe

#### 📽️ Video Demo: [Watch on YouTube](https://youtu.be/uwBKj4G3nlU)

---

## 📝 Description

**Tic Tac Toe** is a timeless two-player game that is easy to learn but challenging to master. This project is a console-based implementation of Tic Tac Toe using **pure Python**, focusing on clean code structure, usability, and user interaction.

The game allows **two human players** to compete against each other in the terminal by entering their custom names and selecting their preferred symbols (like "X" and "O"). The game then renders a visual 3x3 board and proceeds turn-by-turn, updating the board after each move. It checks for winning conditions across rows, columns, and diagonals, and announces either a winner or a draw when the board is full.

This project was built to demonstrate fundamental programming concepts such as conditionals, loops, functions, user input handling, and data structures. It is ideal for beginners looking to understand how simple games can be built using just Python without any additional libraries or frameworks.

---

## 🎮 Features

* 👥 **Two-player mode**: Play against a friend in real-time on the same machine.
* ✏️ **Custom player setup**: Enter your own name and symbol, making each game feel personalized.
* 🎯 **Accurate winner detection**: The program detects wins horizontally, vertically, and diagonally.
* 📋 **Draw logic**: Detects when the board is full and no player has won.
* 🧠 **Input validation**: Prevents invalid or duplicate moves and guides players accordingly.
* 🧼 **Clear and readable board layout**: The grid is updated dynamically after each move with row and column indices for intuitive play.
* 🔁 **Replayability**: Players can restart the game after each match.
* 📦 **Lightweight**: No external dependencies—just pure Python!

---

## 📂 File Structure

```bash
tic-tac-toe-python/
├── project.py         # Main entry point of the program
├── README.md       # Project documentation
```

All the game logic is contained within `project.py`, making it easy to understand and modify.

---

## 🛠️ Technologies Used

* Python 3.x
* Standard Python libraries (no third-party packages)

---

## 🚀 Getting Started

### 🔧 Installation

To run the game, ensure you have Python installed on your system.```

**Run the game:**

   ```bash
   python project.py
   ```

---

## 🎮 How to Play

1. When you start the game, both players are prompted to enter their names.
2. Each player selects a unique single-character symbol (e.g., `X` or `O`).
3. Players take turns entering the row and column index (from 0 to 2) to make a move.
4. The board is updated and displayed after every move.
5. The game continues until a player wins or the board is full (draw).
6. A message is shown declaring the winner or a tie.

Sample output:

```
Player 1 (Alice - X) vs Player 2 (Bob - O)

   0   1   2
0    |   |
  -----------
1    |   |
  -----------
2    |   |

Alice's turn (X). Enter row and column: 0 1
```

---

## 🧐 Concepts Covered

This project helps reinforce the following programming concepts:

* Function-based program structure
* 2D lists for board management
* Loops and conditional logic
* Input/output handling
* Game state management
* Code modularity and readability

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
