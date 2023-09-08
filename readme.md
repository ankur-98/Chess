# Chess Game

This is a simple implementation of the game of chess in Python. It allows two players to take turns making moves on a standard 8x8 chess board until one player is in checkmate.

## Getting Started

To run the game, simply run the `game.py` file in your Python environment. The game will prompt each player to enter their moves in turn, and will validate the moves to ensure they are legal.

## Game Rules

The game follows standard chess rules, with the exception of en passant and castling. These features may be added in a future version.

## Code Structure

The code is structured into three modules: `get_move`, `make_move`, and `game`. 

### `get_move` Module

The `get_move` module handles user input and validation. It contains the following functions:

* `get_input()`: prompts the user for input and returns the input as a tuple of integers representing the row and column.
* `validate_input()`: checks if the input is valid (i.e., within the bounds of the board and corresponds to a piece of the current color).
* `get_piece()`: returns the piece object at the given position.
* `get_legal_moves()`: returns a list of legal moves for the given piece.

### `make_move` Module

The `make_move` module updates the board and checks for checkmate. It contains the following functions:

* `move_piece()`: moves the piece from the `move_from` position to the `move_to` position.
* `is_check()`: checks if the current player is in check.
* `is_checkmate()`: checks if the current player is in checkmate.

### `game` Module

The `game` module ties everything together and runs the game loop. It contains the `Game` class, which has the following methods:

* `__init__()`: initializes the game with a new `ChessBoard` object and sets the current color to "white".
* `play()`: plays the game of chess. Alternates between the two players, prompts for input, validates the input, and updates the board if the move is valid. If the move results in checkmate, prints a message and ends the game.

## Contributing

Contributions are welcome! If you find a bug or have a feature request, please open an issue on GitHub. If you would like to contribute code, please fork the repository and submit a pull request.