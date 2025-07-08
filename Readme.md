# Tic-Tac-Toe AI with Minimax Algorithm

This project implements the classic Tic-Tac-Toe game where you can play against an AI opponent powered by the Minimax algorithm. The AI plays optimally, ensuring it will never lose.

---

## What is Tic-Tac-Toe?

Tic-Tac-Toe is a simple two-player game played on a 3x3 grid. Players take turns placing their marks (X or O) in empty cells. The first player to align three marks horizontally, vertically, or diagonally wins. If the grid is full without a winner, the game ends in a tie.

---

## Project Overview

This project consists of two main files:

- `tictactoe.py`: Contains all the game logic including:
  - Representing the game board.
  - Determining which player's turn it is.
  - Checking for available moves.
  - Checking for a winner or if the game is over.
  - Implementing the Minimax algorithm to select the AI's best move.

- `runner.py`: Provides a graphical interface using `pygame` where you can play against the AI.

---

## Features

- Play against an AI that never loses.
- Graphical interface for an interactive experience.
- Fully implemented Minimax algorithm that looks ahead at all possible moves.
- Clean separation of game logic and interface code.

---

## Installation Instructions

1. **Prerequisites**: You need Python 3 installed on your computer.  
   Check with:
   ```bash
   python3 --version
