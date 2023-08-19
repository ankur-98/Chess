from pieces import *
from chessboard import ChessBoard

class Game:
    def __init__(self):
        self.board = ChessBoard()
        self.current_color = "white"

    def play(self) -> None:
        """
        Plays the game of chess.

        Alternates between the two players. In each iteration of the loop, prints the current state of the board,
        prompts the current player for a move, validates the move, and updates the board if the move is valid. If the
        move results in checkmate, prints a message and ends the game.
        """
        while True:
            print(self.board)
            print(f"{self.current_color.capitalize()}'s turn:")
            move_from = self.get_input("Enter the row and column of the piece you want to move (e.g., '6 3'): ")
            move_to = self.get_input("Enter the row and column where you want to move the piece (e.g., '4 3'): ")

            # Validate input
            try:
                move_from = tuple(map(int, move_from.split()))
                move_to = tuple(map(int, move_to.split()))
                piece = self.board.get_piece_at(move_from)
                
                if piece and piece.color == self.current_color and move_to in piece.legal_moves(self.board.board):
                    self.board.move_piece(move_from, move_to)
                    if self.board.is_checkmate("white" if self.current_color == "black" else "black"):
                        print("Checkmate!")
                        break
                    self.current_color = "white" if self.current_color == "black" else "black"
                else:
                    print("Invalid move. Try again.")
            except Exception:
                print("Invalid input. Try again.")

    @staticmethod
    def get_input(prompt: str) -> str:
        """
        Prompts the user for input and returns the input as a string.

        Args:
            prompt (str): The prompt to display to the user.

        Returns:
            str: The user's input as a string.
        """
        return input(prompt).strip()


if __name__ == "__main__":
    game = Game()
    game.play()
